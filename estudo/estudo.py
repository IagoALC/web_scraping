python_programming = driver.find_element_by_link_text('Python Programming').click()
try:
    beginner_python_tutorials = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    beginner_python_tutorials.click()
    get_started = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    get_started.click()
    driver.back()   #   Volta para a página anterior
except:
    driver.quit()


    search = driver.find_element_by_name('s')
    search.send_keys('Test')
    search.send_keys(Keys.RETURN)
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = main.find_elements_by_tag_name('article')
    for article in articles:
        summary = article.find_element_by_class_name('entry-summary');
        print(summary.text)

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
