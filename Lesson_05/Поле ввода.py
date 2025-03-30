from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get('http://the-internet.herokuapp.com/inputs')
wait = WebDriverWait(driver, 10)

search_box = driver.find_element(By.CSS_SELECTOR, 'input_type="number"')
search_box.send_keys('1000')
search_box.clear()
search_box.send_keys('999')

driver.quit()
