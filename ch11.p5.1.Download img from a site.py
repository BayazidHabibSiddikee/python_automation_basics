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
    site = 'https://www.webtoons.com/en'
    res = requests.get(site)
    browser.get(site)
    res.raise_for_status()
except Exception as e:
    print(f"Error accessing site: {e}")
    browser.quit()
    sys.exit()

wait = WebDriverWait(browser, 25)

try:
    # Click the search button
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[@class='blind' and text()='Search']]")))
    element.click()
    time.sleep(2)
    
    # Wait for search input field to appear and enter search term
    search_input = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "input_search_txtKeyword")))
    search_term = 'Lookism'  # input("Name the manga:")
    search_input.clear()
    search_input.send_keys(search_term)
    
    # Wait a moment for autocomplete suggestions to appear
    time.sleep(2)
    
    # Press Enter to search
    search_input.send_keys(Keys.ENTER)
    time.sleep(3)
    
    # Get page source after search
    soup = bs4.BeautifulSoup(browser.page_source, 'html.parser')
    
    # Look for search results or autocomplete suggestions
    search_results = soup.select('.ly_autocomplete')
    if search_results:
        print("Found autocomplete suggestions:")
        for result in search_results:
            print(result.get_text(strip=True))
    
    # Also look for actual search results on the page
    search_items = soup.select('.search_result_item, .card_item, .item')
    if search_items:
        print(f"\nFound {len(search_items)} search results:")
        for item in search_items[:5]:  # Show first 5 results
            title = item.select_one('.subj, .title, h3')
            if title:
                print(f"- {title.get_text(strip=True)}")
    
    print(f"\nSearch completed for: {search_term}")
    print(f"Current URL: {browser.current_url}")



    #Agai me
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search series or creators']")))
    search_button.send_keys(search_term)
    time.sleep(1)
    search_button.send_keys(Keys.RETURN)
    browser.send_keys(Keys.ENTER)
    
except Exception as e:
    print(f"Error during search: {e}")
    
finally:
    # Keep browser open for a moment to see results
    time.sleep(5)
    #browser.quit()
