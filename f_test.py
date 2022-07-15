from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://localhost:8000")


browser_title = driver.title

assert "The install worked successfully! Congratulations!" in browser_title

driver.close()
driver.quit()