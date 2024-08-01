from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()

driver.get("https://humanbenchmark.com/tests/verbal-memory")

word_list = []

start_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@class="css-de05nr e19owgy710"]'))
)
start_button.click()

seen_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'SEEN')]"))
)
new_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'NEW')]"))
)

while True:
    word_div = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'word'))
    )
    word = word_div.text

    if word in word_list:
        try:
            seen_button.click()
        except Exception as e:
            print("An error occurred while clicking SEEN button:", str(e))
    else:
        try:
            new_button.click()
            word_list.append(word)
        except Exception as e:
            print("An error occurred while clicking NEW button:", str(e))

    sleep(1)
