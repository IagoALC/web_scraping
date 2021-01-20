from urllib import response

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import time

'''url = 'https://statusinvest.com.br/acoes'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
req = Request(url, headers=headers)
response = urlopen(req)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
company_divs = soup.find('a', {'class': 'company card mt-0 mb-3 ml-1 mr-1 d-flex flex-column waves-effect'})
a = company_divs['href']
print(a)'''

path = 'F:\Programação\Python\web_scraping\driver\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://statusinvest.com.br/acoes')
pages = 22  # Quantidade de páginas do total de empresas
try:
    company = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "company-section"))
    )
    all_companys = company.find_elements_by_class_name('company')
    pages = 22
    for each_company in all_companys:
        print(each_company.get_attribute('href'))
    chevron_right = company.find_element_by_link_text('chevron_right')
    chevron_right.send_keys(Keys.SPACE)
    time.sleep(1)
    company = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "company-section"))
    )
    all_companys = company.find_elements_by_class_name('company')
    print('teste')
    print(all_companys[0].get_attribute('href'))

finally:
    driver.quit()
