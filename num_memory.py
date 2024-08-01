from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome()

driver.get("https://humanbenchmark.com/tests/number-memory")

actions = ActionChains(driver)

start_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@class="css-de05nr e19owgy710"]'))
)

start_button.click()

while True:
    num_div = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'big-number'))
    )

    num = num_div.text

    text_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="text"][pattern="[0-9]*"]'))
        )

    text_box.send_keys(str(num))

    text_box.send_keys(Keys.RETURN)

    actions.send_keys(Keys.RETURN).perform()