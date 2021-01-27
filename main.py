from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

#   Configurando o Selenium
path = 'F:\Programação\Python\web_scraping\driver\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://statusinvest.com.br/acoes')


#   Função que cria uma lista com todas as empresas
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
    return siglas

#   Função para pegar os dados das ações
def pega_dados(selected_stocks):
    lista_resultados = []
    resultados = {}
    total_indicadores = 4  # GUARDA QUANTAS SESSÕES DE INDICADORES EXISTEM
    for link in selected_stocks:
        driver.get(f'https://statusinvest.com.br/acoes/{link}')
        try:
            #   LOCALIZANDO CLASSE COM OS INDICADORES
            todos_indicadores = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'today-historical-container'))
            )

            #   LOCALIZANDO CADA INDICADOR
            valuation = todos_indicadores.find_elements_by_class_name('justify-start')
            resultados['AÇÃO'] = link.upper()
            for i in range(total_indicadores):
                dados = valuation[i].find_elements_by_tag_name('strong')
                titulos = valuation[i].find_elements_by_tag_name('h3')

                for contagem in range(len(dados)):
                    resultados[titulos[contagem].text] = dados[contagem].text

        finally:
            lista_resultados.append(resultados)
            resultados = {}
    driver.quit()
    df = pd.DataFrame(lista_resultados)
    df.to_csv('F:\Downloads\Dados_fundamentalistas.csv', sep=';', encoding='utf-8-sig', index=False)


#   Parte Principal
links = lista_empresas()

siglas = separando_siglas(links)
#siglas = coloca_ausentes(siglas)
stock = ''
selected_stocks = []
while(stock != '1'):
    i = 0  # iterador
    print('Digite 1 se não quiser mais adicionar ações')
    stock = input('Digite a ação que você deseja(Ex:WEG3): ')
    for sigla in siglas:
        if(stock == sigla):
            i += 1
    if(i > 0):
        selected_stocks.append(stock)
    elif(i == 0) and (stock != '1'):
        print('Essa ação não existe')
pega_dados(selected_stocks)
