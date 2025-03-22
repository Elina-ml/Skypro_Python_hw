from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/login')

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="username"]')))
search_box = driver.find_element(By.CSS_SELECTOR, 'input_type="text"_name="username"_id="username"')
search_box.send_keys('tomsmith')
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
search_box = driver.find_element(By.CSS_SELECTOR, 'input_type="password"_name="password"_id="password"')
search_box.send_keys('SuperSecretPassword!')
add_button = driver.find_element(By.CSS_SELECTOR, 'button[type=" Login"]')
add_button.click()

driver.quit()
