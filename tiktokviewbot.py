import os
try:
    import undetected_chromedriver,selenium,requests
except:
    os.system("pip install undetected_chromedriver")
    os.system("pip install selenium")
    os.system("pip install setuptools")
    os.system("pip install requests")
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


os.system('cls')

print("made by @nikymetaa on discord")
link_request = input("link: ")

chrome_options = uc.ChromeOptions()

driver = uc.Chrome(options=chrome_options)
driver.set_window_size(600, 900)

def get_captcha():
    try:
        sleep(5)
        image_element = driver.find_element(By.CSS_SELECTOR, "body > div.noscriptcheck > div.ua-check > form > div > div > img")
        image_element.screenshot("image.png")
        ocr_result = ocr_from_image("./image.png")
        print("Captcha: " + ocr_result["ParsedResults"][0]["ParsedText"])
        sleep(3)
        return ocr_result["ParsedResults"][0]["ParsedText"]
    except Exception as e:
        print(e)

def ocr_from_image(image_path):
    try:
        url = "https://api.ocr.space/parse/image"
        payload = {
            "language": "eng",
            "isOverlayRequired": False,
            "scale": True,
            "isTable": False,
            "filetype": "png"
        }
        headers = {
            "apikey": "K87899142388957" 
        }

        with open(image_path, "rb") as image_file:
            files = {
                "file": image_file
            }
            response = requests.post(url, data=payload, headers=headers, files=files)

        if response.status_code == 200:
            return response.json()
        else:
            return None

    except Exception as e:
        print(e)

def solve_captcha():
    try:
        print("Solving CAPTCHA...")
        
        captcha = get_captcha()
        
        captcha_input = driver.find_element(By.CSS_SELECTOR, "body > div.noscriptcheck > div.ua-check > form > div > div > div > input")
        captcha_input.send_keys(captcha)
    
    except Exception as e:
        print(e)

try:
    driver.get("https://zefoy.com/")
    sleep(3)
    solve_captcha()

    try:
        click1 = WebDriverWait(driver, 45).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div[2]/div/div/div[6]/div/button'))
        )
        if not click1.is_enabled():
            print("Button is disabled - service is not updated")
            return
        click1.click()
     except:
        print("Button is disabled - service is not updated")
        return
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
