from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

print("Website Title:", driver.title)

driver.quit()
