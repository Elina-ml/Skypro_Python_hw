from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
add_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer > p > button")))
add_button.click()

driver.quit()
