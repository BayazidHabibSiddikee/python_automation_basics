#2048
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time, random


bro = webdriver.Edge()
bro.get('https://gabrielecirulli.github.io/2048/')
bro.maximize_window()
WebDriverWait(bro,10)
bro.minimize_window()
bro.maximize_window()
browser = bro.find_element('tag name','html')
time.sleep(3)
def play():
    n=0
    while True:
        for i in [Keys.UP,Keys.RIGHT,Keys.LEFT,Keys.DOWN,Keys.RIGHT,Keys.RIGHT,Keys.UP,Keys.UP]:
            '''
        browser.send_keys(Keys.UP)
        time.sleep(0.0025)
        browser.send_keys(Keys.RIGHT)
        time.sleep(0.005)
        browser.send_keys(Keys.DOWN)
        time.sleep(0.0025)
        browser.send_keys(Keys.LEFT)
        #time.sleep(0.005)'''
            browser.send_keys(random.choice(i))
            time.sleep(0.0025)
        try:
            b= WebDriverWait(bro,0.005).until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Play Again']")))
            #b = bro.find_element(By.CLASS_NAME, "Play Again")
            if b.is_displayed():
                b.click()
                time.sleep(5)
                #bro.minimize_window()
                time.sleep(1)
                #bro.maximize_window()
                n+=1
                if n==3:
                    break
        except:
            pass


try:
    play()
except Exception as e:
    print(e)
time.sleep(6)
bro.quit()
    
