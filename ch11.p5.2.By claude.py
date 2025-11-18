import webbrowser, os, requests, sys, bs4, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the program
browser = webdriver.Edge()
browser.maximize_window()

try:
    #site = 'https://www.coffeemanga.art/home'
    site = 'https://www.webtoons.com/en/'
    res = requests.get(site)
    browser.get(site)
    res.raise_for_status()  # This will raise an exception if status is not 200
except Exception as e:
    print(f"Error with first site: {e}")
    try:
        site = 'https://www.webtoons.com/en/'
        res = requests.get(site)
        browser.get(site)
        res.raise_for_status()
    except Exception as e2:
        print(f"Error with second site: {e2}")
        browser.quit()
        sys.exit()

wait = WebDriverWait(browser, 25)

try:
    # Wait for and click the search button (the one with "Search" text inside span.blind)
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[@class='blind' and text()='Search']]")))
    search_button.click()
    time.sleep(2)
    
    # Now look for the search input area that should appear
    search_area = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search_area")))
    
    # Find the search input field (you'll need to look for the actual input element)
    # This might be something like:
    # search_input = browser.find_element(By.CSS_SELECTOR, ".search_area input[type='text']")
    # search_input.send_keys("your search term")
    # search_input.send_keys(Keys.ENTER)
    
    # Get page source for BeautifulSoup after the search interaction
    soup = bs4.BeautifulSoup(browser.page_source, 'html.parser')
    
    # Find search-related elements
    search_elements = soup.select('.search_area')
    print(f"Found {len(search_elements)} search area elements")
    
    # Print the search area HTML for debugging
    if search_elements:
        print("Search area HTML:")
        print(search_elements[0].prettify())
    
    print("\nPage title:", soup.title.text if soup.title else "No title found")
    
except Exception as e:
    print(f"Error during scraping: {e}")
finally:
    # Always close the browser
    browser.quit()
