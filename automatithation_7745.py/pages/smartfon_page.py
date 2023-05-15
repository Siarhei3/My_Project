import time

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class choose_smartfon_page(Base):
    base_url = 'https://7745.by/catalog/smartfony-na-android'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators
    sale_check_box = '/html/body/div[2]/div[1]/div[4]/div/div[2]/div[1]/div[1]/form/div[1]/div[2]'
    price = '//*[@id="catalog-filter-form"]/div[2]/div[2]/div[1]/div[2]/input'
    choose_xiaomi = '//*[@id="catalog-filter-form"]/div[3]/div[2]/div[1]/label/span[1]/span'
    choose_sumsung = '/html/body/div[2]/div[1]/div[4]/div/div[2]/div[1]/div[1]/form/div[3]/div[2]/div[2]/label/span[2]'
    year_made = '/html/body/div[2]/div[1]/div[4]/div/div[2]/div[1]/div[1]/form/div[4]/div[2]/div[2]/div[1]/label'
    button_product = '//*[@id="catalog-filter-form"]/div[45]/button[1]'
    card_button = '//*[@id="panel"]/div[1]/div[4]/div/div[2]/div[2]/div[6]/div[1]/div[2]/div/div[2]/div[2]/div[1]/button'
    main_card = '//*[@id="cart-link"]/div/div[1]/div'
    close_city_window = '/html/body/div[2]/div[5]/div[14]/div/div[2]/form/button'
    name = '//*[@id="cart[user][fio]"]'
    phone = '//*[@id="cart_user_phone"]'
    email = '//*[@id="cart[user][mail]"]'
    icon_7755 = '//*[@id="panel"]/div[1]/div[2]/div/div[1]/a'
# Geters
    def get_sale_check_box(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sale_check_box)))

    def get_price_product_smart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_choose_xiaomi(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_xiaomi)))

    def get_choose_sumsung(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_sumsung)))

    def get_year_made(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.year_made)))

    def get_button_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_product)))

    def get_card_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.card_button)))

    def get_main_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_card)))

    def get_close_city_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_city_window)))

    def get_input_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_input_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_input_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_icon_7755(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.icon_7755)))

# Actions
    def click_sale_check_box(self):
        self.get_sale_check_box().click()
        print('click sale check box')

    def input_price_max(self, price_max):
        self.get_price_product_smart().send_keys(price_max)
        print("Click price Smartfon")

    def click_choose_xiaomi(self):
        self.get_choose_xiaomi().click()
        print("Click chose XIAOMI")
    def click_choose_sumsung(self):
        self.get_choose_sumsung().click()
        print("Click chose SUMSUNG")
    def click_year_made(self):
        self.get_year_made().click()
        print("Click year made")
    def click_button_product(self):
        self.get_button_product().click()
        print("Click button product")
    def click_card_button(self):
        self.get_card_button().click()
        print("Click card button")
    def click_main_card(self):
        self.get_card_button().click()
        print("Click main card")
    def click_close_city_window(self):
        self.get_close_city_window().click()
        print('click close city window')

    def input_name(self, name):
        self.get_input_name().send_keys(name)
        print("Input name")

    def input_phone(self, phone):
        self.get_input_phone().send_keys(phone)
        print("input phone")

    def input_email(self, email):
        self.get_input_email().send_keys(email)
        print("input email")

    def click_icon_7755(self):
        self.get_icon_7755().click()
        print('click icon 7755')

# Autorithation
    def autorithation_smartfon_page(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.click_sale_check_box()
        self.input_price_max('800')
        self.click_choose_xiaomi()
        self.click_choose_sumsung()
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
        self.click_year_made()
        self.click_button_product()
        self.click_card_button()
        time.sleep(2)
        self.click_main_card()
        self.click_close_city_window()
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
        self.input_name('Siarhei')
        self.input_phone('296472712')
        self.input_email('sergerio@mail.com')
        self.click_icon_7755()



