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

