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

#   Função para colocar as ações que faltam Ex: Sapr4, Sapr3
def coloca_ausentes(siglas):
    siglas.append('sapr4'), siglas.append('sapr3'),siglas.append('itub3'),siglas.append('petr3'),siglas.append('sapr4'),
    siglas.append('sapr4'),siglas.append('tiet4'),siglas.append('tiet3'),siglas.append('rpad5'),siglas.append('rpad3'),
    siglas.append('alpa3'),siglas.append('alup3'),siglas.append('alup4'),siglas.append('andg3b'),siglas.append('azev3'),
    siglas.append('briv3'),siglas.append('bgip3'),siglas.append('bees3'),siglas.append('brsr5'),siglas.append('brsr6'),
    siglas.append('bbdc3'),siglas.append('bpac3'),siglas.append('bpac5'),siglas.append('idvl3'),siglas.append('bidi3'),
    siglas.append('bidi11'),siglas.append('bmin3'),siglas.append('bmeb3'),siglas.append('pine3'),siglas.append('sanb3'),
    siglas.append('sanb4'),siglas.append('bdll3'),siglas.append('bttl3'), siglas.append('balm3'),siglas.append('bobr3'),
    siglas.append('brap3'),siglas.append('brkm3'),siglas.append('brkm5'), siglas.append('bfre12'),siglas.append('bsli3'),
    siglas.append('camb3'),siglas.append('cebr5'),siglas.append('cebr6'), siglas.append('cedo3'),siglas.append('ceed3'),
    siglas.append('eeel3'),siglas.append('clsc3'),siglas.append('cepe5'), siglas.append('cepe6'),siglas.append('rani4'),
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
siglas = coloca_ausentes(siglas)
print(siglas)
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
