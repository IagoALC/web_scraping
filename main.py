from urllib import response

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = 'F:\Programação\Python\web_scraping\driver\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://statusinvest.com.br/acoes')
pages = 22  # Quantidade de páginas do total de empresas

try:
    #   Selecionando o campo com os links das empresas
    company = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "company-section"))
    )
    all_companys = company.find_elements_by_class_name('company')
    pages = 22
    links = []

    #   Loops para pegar o link de todas as empresas em todas as páginas
    for page in range(pages):
        for each_company in all_companys:
            links.append(each_company.get_attribute('href'))
        chevron_right = company.find_element_by_link_text('chevron_right')
        chevron_right.send_keys(Keys.SPACE)
        time.sleep(1)
        company = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "company-section"))
        )
        all_companys = company.find_elements_by_class_name('company')
    print(links)
    print(len(links))
finally:
    driver.quit()
