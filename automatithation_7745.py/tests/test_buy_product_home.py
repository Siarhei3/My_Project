import time

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from pages.registration_page import login_page
from pages.product_page import product_page
from pages.smartfon_page import choose_smartfon_page
from pages.card_pages import card_product_page


def test_login():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #добавление расширения к chromedriver
    # options.add_argument(r'--load-extension=C:\Users\37529\AppData\Local\Google\Chrome\User Data\Default\Extensions\caahalkghnhbabknipmconmbicpkcopl\0.0.0.2_0')
    options.add_experimental_option("detach", True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    action = ActionChains(driver)

    print("START Test")

    # login = login_page(driver)
    # login.autorithation()

    # pp = product_page(driver)
    # pp.autorithation_product()

    smartpage = choose_smartfon_page(driver)
    smartpage.autorithation_smartfon_page()

    # cardpage = card_product_page(driver)
    # cardpage.autorithation_main_card()



