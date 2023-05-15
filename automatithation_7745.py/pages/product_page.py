import time

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class product_page(Base):
    base_url = 'https://7745.by/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
# Locators
    main_burger_button = '//*[@id="panel"]/div[1]/div[2]/div/div[2]/a/span[1]'
    electronic_prod = '//*[@id="panel"]/div[1]/div[3]/div/ul/li[3]'
    smart_android = '/html/body/div[2]/div[1]/div[3]/div/div[3]/div[2]/ul[1]/li/ul/li[2]/a'
    main_word = '//*[@id="panel"]/div[1]/div[4]/div/div[2]/div[2]/h1'

# Geters
    def get_main_burger_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_burger_button)))
    def get_electronic_prod(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.electronic_prod)))
    def get_smart_android(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smart_android)))
    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

# Actions
    def click_main_burger_button(self):
        self.get_main_burger_button().click()
        print('click Main burger menu')

    def click_electronic_prod(self):
        self.get_electronic_prod().click()
        print('click electronic product')

    def click_smart_android(self):
        self.get_smart_android().click()
        print('click smart android')
# Autorithation
    def autorithation_product(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_main_burger_button()
        self.click_electronic_prod()
        self.click_smart_android()
        self.assert_word(self.get_main_word(), 'Смартфоны на Android')


