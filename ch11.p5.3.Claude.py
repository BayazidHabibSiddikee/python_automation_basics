#!/usr/bin/env python3
"""
Image Site Downloader
A flexible program to download images from photo-sharing sites.
Supports multiple sites and search functionality.
"""

import os
import re
import json
import time
import requests
from urllib.parse import urljoin, urlparse, parse_qs
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Optional
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup

@dataclass
class ImageInfo:
    """Data class to hold image information"""
    url: str
    filename: str
    title: str = ""
    description: str = ""

class BaseSiteDownloader:
    """Base class for site-specific downloaders"""
    
    def __init__(self, download_dir: str = "downloads"):
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(exist_ok=True)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def search_images(self, query: str, limit: int = 20) -> List[ImageInfo]:
        """Search for images on the site. Override in subclasses."""
        raise NotImplementedError("Subclasses must implement search_images")
    
    def download_image(self, image_info: ImageInfo) -> bool:
        """Download a single image"""
        try:
            response = self.session.get(image_info.url, timeout=30)
            response.raise_for_status()
            
            # Create category subdirectory
            category_dir = self.download_dir / self.get_safe_filename(image_info.title or "images")
            category_dir.mkdir(exist_ok=True)
            
            # Save image
            file_path = category_dir / image_info.filename
            with open(file_path, 'wb') as f:
                f.write(response.content)
            
            print(f"Downloaded: {image_info.filename}")
            return True
            
        except Exception as e:
            print(f"Error downloading {image_info.url}: {e}")
            return False
    
    def get_safe_filename(self, filename: str) -> str:
        """Convert string to safe filename"""
        # Remove invalid characters
        filename = re.sub(r'[<>:"/\\|?*]', '', filename)
        # Replace spaces with underscores
        filename = re.sub(r'\s+', '_', filename)
        # Limit length
        return filename[:50] if len(filename) > 50 else filename
    
    def download_images(self, images: List[ImageInfo], max_workers: int = 5) -> int:
        """Download multiple images concurrently"""
        success_count = 0
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_image = {executor.submit(self.download_image, img): img for img in images}
            
            for future in as_completed(future_to_image):
                if future.result():
                    success_count += 1
                time.sleep(0.1)  # Be respectful to the server
        
        return success_count

class UnsplashDownloader(BaseSiteDownloader):
    """Downloader for Unsplash (using their API)"""
    
    def __init__(self, download_dir: str = "downloads", api_key: str = None):
        super().__init__(download_dir)
        self.api_key = api_key
        self.base_url = "https://api.unsplash.com"
    
    def search_images(self, query: str, limit: int = 20) -> List[ImageInfo]:
        """Search Unsplash for images"""
        if not self.api_key:
            print("Unsplash API key required. Get one at https://unsplash.com/developers")
            return []
        
        images = []
        per_page = min(limit, 30)  # Unsplash API limit
        
        try:
            headers = {"Authorization": f"Client-ID {self.api_key}"}
            params = {
                "query": query,
                "per_page": per_page,
                "orientation": "all"
            }
            
            response = self.session.get(
                f"{self.base_url}/search/photos",
                headers=headers,
                params=params
            )
            response.raise_for_status()
            
            data = response.json()
            
            for photo in data.get('results', []):
                # Use regular quality for faster downloads
                image_url = photo['urls']['regular']
                filename = f"{photo['id']}.jpg"
                
                images.append(ImageInfo(
                    url=image_url,
                    filename=filename,
                    title=query,
                    description=photo.get('description', '') or photo.get('alt_description', '')
                ))
            
            print(f"Found {len(images)} images for '{query}'")
            
        except Exception as e:
            print(f"Error searching Unsplash: {e}")
        
        return images

class GenericSiteDownloader(BaseSiteDownloader):
    """Generic downloader for sites using web scraping"""
    
    def __init__(self, download_dir: str = "downloads"):
        super().__init__(download_dir)
    
    def search_images(self, query: str, limit: int = 20) -> List[ImageInfo]:
        """Generic image search using web scraping"""
        print("Note: This is a demonstration of generic scraping.")
        print("For production use, consider using official APIs or ensure compliance with site terms.")
        
        images = []
        
        # Example: Search using a generic image search approach
        # This would need to be customized for specific sites
        search_url = f"https://www.example-image-site.com/search?q={query}"
        
        try:
            response = self.session.get(search_url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Generic selectors - these would need site-specific customization
            img_tags = soup.find_all('img', limit=limit)
            
            for i, img in enumerate(img_tags):
                src = img.get('src') or img.get('data-src')
                if src and self.is_valid_image_url(src):
                    # Convert relative URLs to absolute
                    if src.startswith('//'):
                        src = 'https:' + src
                    elif src.startswith('/'):
                        src = urljoin(search_url, src)
                    
                    # Generate filename
                    filename = f"{query}_{i+1}.jpg"
                    
                    images.append(ImageInfo(
                        url=src,
                        filename=self.get_safe_filename(filename),
                        title=query,
                        description=img.get('alt', '')
                    ))
            
        except Exception as e:
            print(f"Error in generic search: {e}")
        
        return images
    
    def is_valid_image_url(self, url: str) -> bool:
        """Check if URL appears to be a valid image"""
        if not url:
            return False
        
        # Check for common image extensions
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp']
        url_lower = url.lower()
        
        return any(ext in url_lower for ext in image_extensions)

class FlickrDownloader(BaseSiteDownloader):
    """Downloader for Flickr (requires API key)"""
    
    def __init__(self, download_dir: str = "downloads", api_key: str = None):
        super().__init__(download_dir)
        self.api_key = api_key
        self.base_url = "https://www.flickr.com/services/rest/"
    
    def search_images(self, query: str, limit: int = 20) -> List[ImageInfo]:
        """Search Flickr for images"""
        if not self.api_key:
            print("Flickr API key required. Get one at https://www.flickr.com/services/api/")
            return []
        
        images = []
        per_page = min(limit, 100)  # Flickr API limit
        
        try:
            params = {
                'method': 'flickr.photos.search',
                'api_key': self.api_key,
                'text': query,
                'per_page': per_page,
                'format': 'json',
                'nojsoncallback': 1,
                'safe_search': 1,
                'content_type': 1  # Photos only
            }
            
            response = self.session.get(self.base_url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('stat') == 'ok':
                photos = data.get('photos', {}).get('photo', [])
                
                for photo in photos:
                    # Construct image URL
                    image_url = f"https://farm{photo['farm']}.staticflickr.com/{photo['server']}/{photo['id']}_{photo['secret']}_b.jpg"
                    filename = f"{photo['id']}.jpg"
                    
                    images.append(ImageInfo(
                        url=image_url,
                        filename=filename,
                        title=query,
                        description=photo.get('title', '')
                    ))
                
                print(f"Found {len(images)} images for '{query}'")
            else:
                print(f"Flickr API error: {data.get('message', 'Unknown error')}")
                
        except Exception as e:
            print(f"Error searching Flickr: {e}")
        
        return images

class ImageDownloadManager:
    """Main manager class for downloading images"""
    
    def __init__(self, download_dir: str = "downloads"):
        self.download_dir = download_dir
        self.downloaders = {
            'unsplash': UnsplashDownloader,
            'flickr': FlickrDownloader,
            'generic': GenericSiteDownloader
        }
    
    def download_from_site(self, site: str, query: str, limit: int = 20, api_key: str = None) -> int:
        """Download images from a specific site"""
        if site not in self.downloaders:
            print(f"Unsupported site: {site}")
            print(f"Available sites: {', '.join(self.downloaders.keys())}")
            return 0
        
        # Initialize downloader
        downloader_class = self.downloaders[site]
        if site in ['unsplash', 'flickr']:
            downloader = downloader_class(self.download_dir, api_key)
        else:
            downloader = downloader_class(self.download_dir)
        
        # Search for images
        print(f"Searching {site} for '{query}'...")
        images = downloader.search_images(query, limit)
        
        if not images:
            print("No images found.")
            return 0
        
        # Download images
        print(f"Starting download of {len(images)} images...")
        success_count = downloader.download_images(images)
        
        print(f"Successfully downloaded {success_count}/{len(images)} images to {self.download_dir}")
        return success_count

def main():
    """Main function with command-line interface"""
    parser = argparse.ArgumentParser(description='Download images from photo-sharing sites')
    parser.add_argument('site', choices=['unsplash', 'flickr', 'generic'], 
                       help='Photo site to download from')
    parser.add_argument('query', help='Search query')
    parser.add_argument('--limit', type=int, default=20, help='Maximum number of images to download')
    parser.add_argument('--api-key', help='API key for the service (if required)')
    parser.add_argument('--download-dir', default='downloads', help='Directory to save images')
    
    args = parser.parse_args()
    
    # Create download manager
    manager = ImageDownloadManager(args.download_dir)
    
    # Download images
    success_count = manager.download_from_site(
        args.site, 
        args.query, 
        args.limit,
        args.api_key
    )
    
    if success_count > 0:
        print(f"\nDownload completed! Check the '{args.download_dir}' directory.")
    else:
        print("\nNo images were downloaded.")

if __name__ == "__main__":
    # Example usage if run directly
    if len(os.sys.argv) == 1:
        print("Image Site Downloader")
        print("===================")
        print()
        print("Usage examples:")
        print("  python image_downloader.py unsplash 'nature' --limit 10 --api-key YOUR_KEY")
        print("  python image_downloader.py flickr 'landscape' --limit 15 --api-key YOUR_KEY")
        print("  python image_downloader.py generic 'cats' --limit 5")
        print()
        print("To get started:")
        print("1. For Unsplash: Get API key at https://unsplash.com/developers")
        print("2. For Flickr: Get API key at https://www.flickr.com/services/api/")
        print("3. Generic scraping works without API keys but may have limitations")
        print()
        
        # Demo with generic downloader
        manager = ImageDownloadManager("demo_downloads")
        print("Running demo with generic downloader...")
        # manager.download_from_site('generic', 'example', 3)
    else:
        main()
