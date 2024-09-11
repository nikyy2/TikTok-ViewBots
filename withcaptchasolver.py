import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytesseract
from PIL import Image
import pyautogui
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

screenshot_filename = "captcha.png"

screenshot_path = os.path.join(current_directory, screenshot_filename)

x, y, width, height = 197, 540, 280, 162

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text.strip()

link_request = input("link: ")

chrome_options = uc.ChromeOptions()

driver = uc.Chrome(options=chrome_options)
driver.set_window_size(600, 900)

try:
    driver.get("https://zefoy.com/")
    sleep(3)
    
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save(screenshot_path)
    print(f"Captcha.png saved at {screenshot_path}")
    
    sleep(1)
    
    image_path = 'captcha.png'
    extracted_text = extract_text_from_image(image_path)
    print(f"Captchaaaaaaaa: {extracted_text}")
    enter_captcha = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/form/div/div/div/input')
    enter_captcha.send_keys(extracted_text)
    
    sleep(1)
    submit_captcha = WebDriverWait(driver, 45).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[2]/form/div/div/div/div/button'))
    )
    submit_captcha.click()
    
    sleep(1)
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
