import os
try:
    import requests,colorama,prettytable
except:
    os.system("pip install undetected-chromedriver")
    os.system("pip install selenium")
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

link_request = input("link: ")

chrome_options = uc.ChromeOptions()

driver = uc.Chrome(options=chrome_options)
driver.set_window_size(600, 900)

try:
    driver.get("https://zefoy.com/")
    sleep(3)

    click1 = WebDriverWait(driver, 45).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div[2]/div/div/div[6]/div/button'))
    )
    click1.click()
    sleep(2)

    input_link = driver.find_element(By.XPATH, '/html/body/div[10]/div/form/div/input')
    input_link.send_keys(link_request)
    sleep(5)

    while True:
        try:
            click2 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/div/form/div/div/button'))
            )
            click2.click()
            sleep(2)

            click3 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/div/div/div[1]/div/form/button'))
            )
            click3.click()
            sleep(2)
            print("+1000 auras")

        except Exception as e:
            pass

except Exception as e:
    pass
