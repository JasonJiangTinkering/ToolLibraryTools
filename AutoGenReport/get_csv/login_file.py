# Load selenium components
from selenium.webdriver.common.by import By


def login(driver):
    # login to tool library
    # find the login form
    password = driver.find_element(By.XPATH, "//input[@name='j_password']")
    username = driver.find_element(By.XPATH, "//input[@name='j_username']")
    # enter username and password
    username.send_keys("Probeyond")
    password.send_keys("w4xgSS7J3abM5zH")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    # fill in the login form

    # submit the login form
