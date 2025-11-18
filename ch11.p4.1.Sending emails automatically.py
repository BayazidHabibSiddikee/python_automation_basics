import sys, time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#browser = webdriver.Edge()

def message():
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get('https://m.kuku.lu/en.php')
        #wait
    wait = WebDriverWait(browser,20)
    
    button = browser.find_element(By.XPATH, "//a[normalize-space()='Create an address automatically']")
    button.click()
    time.sleep(3)
    confirm = browser.find_element(By.XPATH, "//a[normalize-space()='Yes']")
    confirm.click()
    time.sleep(3)
    butt = browser.find_element(By.XPATH, "//a[normalize-space()='Create new message']")
    butt.click()
    time.sleep(3)
    try:
        recipient_input = browser.find_element(By.XPATH, '//label[text()="Recipient:"]/following-sibling::input')
        recipient_input.clear()
        name =input("Enter recipants email:")
        recipient_input.send_keys('name')
    except Exception as e:
        print('There is a problem '+e)
        sys.exit()

#browser.get('')
message()




