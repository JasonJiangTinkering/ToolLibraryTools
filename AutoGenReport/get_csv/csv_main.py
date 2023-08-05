# Load selenium components
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from . import login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os


def get_csv_runner(file_location):
    # Establish chrome driver and go to report site URL
    url = "https://universityheights.myturn.com/library/orgInventory/list"
    options = webdriver.ChromeOptions()
    options.add_argument(f"download.default_directory={file_location}")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    # login to tool library
    login.login(driver)
    # Click the "Export to CSV" button
    export_to_csv = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@data-extension='csv']"))
    )
    # export_to_csv = driver.find_element(By.XPATH, "//a[@data-extension='csv']")
    export_to_csv.click()
    # Move the file to the correct location
    os.rename(
        "C:\\Users\\Jason Jiang\\Downloads\\list-items-export.csv",
        "C:\\Users\\Jason Jiang\\Documents\\ToolLibraryTools\\AutoGenReport",
    )
    # hold the program open
    while True:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
