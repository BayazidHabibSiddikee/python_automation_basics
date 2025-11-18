#!/usr/bin/env python3
import requests, os, bs4, threading

os.makedirs('xkcd-comics', exist_ok=True)

def download(start, endd):
    for urlnum in range(start, endd):
        try:
            print(f"Downloading page http://xkcd.com/{urlnum}...")
            res = requests.get(f'http://xkcd.com/{urlnum}')
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, "html.parser")

            # Find the image from URL
            comicelem = soup.select('#comic img')
            if not comicelem:
                print(f"No comic found on page {urlnum}")
                continue

            comicurl = comicelem[0].get('src')
            if comicurl.startswith('//'):
                comicurl = 'https:' + comicurl

            # Download the image
            print(f'Downloading {comicurl}')
            imgres = requests.get(comicurl)
            imgres.raise_for_status()

            # Save the image
            imgfile = open(os.path.join('xkcd-comics', os.path.basename(comicurl)), 'wb')
            for chunk in imgres.iter_content(100000):
                imgfile.write(chunk)
            imgfile.close()
        except Exception as e:
            print(f"Failed to download {urlnum}: {e}")

# Create and start threads
downloadt = []
for i in range(0, 1400, 100):
    downloadthread = threading.Thread(target=download, args=(i, i+100))
    downloadt.append(downloadthread)
    downloadthread.start()

# Wait for all threads to finish
for downloadthread in downloadt:
    downloadthread.join()

print('done')
