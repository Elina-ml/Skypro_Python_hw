from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

driver.find_elements(By.CLASS_NAME, "added-manually")
add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
for _ in range(5):
    add_button.click()

delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")
print(len(delete_buttons))

driver.quit()
