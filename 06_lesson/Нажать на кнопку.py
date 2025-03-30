from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/ajax")

driver.implicitly_wait(20)
driver.find_element(By.ID, "ajaxButton").click()
element = driver.find_elements(By.CSS_SELECTOR, "bg-success")

driver.quit()
