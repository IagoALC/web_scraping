from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#   Configurando o Selenium
path = 'F:\Programação\Python\web_scraping\driver\chromedriver.exe'
driver = webdriver.Chrome(path)
# driver.get('https://statusinvest.com.br/acoes')


#   Método que cria uma lista com todas as empresas
def lista_empresas():
    try:
        #   Selecionando o campo com os links das empresas
        company = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "company-section"))
        )
        all_companys = company.find_elements_by_class_name('company')
        pages = 22  #   Quantidade de páginas contendo empresas
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
        return links
    finally:
        pass


#   Função para pegar todas as siglas separadamente dos links
def separando_siglas(links):
    inicio = 34
    siglas = []
    for link in links:
        siglas.append(link[inicio:])

#   Parte Principal
#links = lista_empresas()
links = ['https://statusinvest.com.br/acoes/btow3', 'https://statusinvest.com.br/acoes/mglu3']
siglas = separando_siglas(links)

stock = ''
selected_stocks = []
while(stock != '1'):
    print('Digite 1 se não quiser mais adicionar ações')
    stock = input('Digite a ação que você deseja(Ex:WEG3): ')
    selected_stocks.append(stock)

for link in links:
    driver.get(link)
