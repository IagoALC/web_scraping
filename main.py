from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

path = 'F:\Programação\Python\web_scraping\driver\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://statusinvest.com.br/acoes')
try:
    company = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "company-section"))
    )
    company_divs = company.find_element_by_class_name('w-lg-16_6')
    print(company_divs)
    chevron_right = company.find_element_by_link_text('chevron_right')
    chevron_right.send_keys(Keys.SPACE)
except:
    driver