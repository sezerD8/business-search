from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.chrome.options import Options
import time


def search(text):
    options = Options()
    options.add_argument("--headless")
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service,options=options)
    data = []

    try:
        driver.get('https://www.google.com/maps')
        time.sleep(5)
        
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(text)
        search_box.send_keys(Keys.ENTER)
        time.sleep(5)

        company_frame = driver.find_element(By.CLASS_NAME, "m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd")
        scroll_origin = ScrollOrigin.from_element(company_frame)
        
        while True:
            search_companies = driver.find_elements(By.CLASS_NAME, "UaQhfb.fontBodyMedium")
            for company in search_companies:
                company_name = company.text
                if company_name not in data:
                    data.append(company_name)
            
            ActionChains(driver).scroll_from_origin(scroll_origin, 0, 2000).perform()
            time.sleep(1)

            try:
                driver.find_element(By.CLASS_NAME, "HlvSq")
                break 
            except:
                pass 

    except Exception as e:
        print("Hata oluştu:", e)
    
    finally:
        time.sleep(3)
        driver.quit()
    return data
