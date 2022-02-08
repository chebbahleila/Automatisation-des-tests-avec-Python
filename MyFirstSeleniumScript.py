from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\leila\\automatisation_py\\selenium_webdriver\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://www.facebook.com")
driver.maximize_windows()
driver.implicitly_wait(20)
driver.get_screenshot_as_file("facebook.png")
driver.quit()