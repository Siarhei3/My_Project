import time

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class login_page(Base):
    base_url = 'https://7745.by/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

      #Locators
    registration_button_1 = '//*[@id="panel"]/div[5]/div[6]/div/div[2]/div/div/form/div[4]/button'
    icon_login = '/html/body/div[2]/div[1]/div[2]/div/div[3]/div[4]/div/div'
    user_name = '/html/body/div[2]/div[5]/div[4]/div/div[2]/form/div[1]/input'
    user_phone = '/html/body/div[2]/div[5]/div[4]/div/div[2]/form/div[2]/div[2]/input'
    user_emeil = '/html/body/div[2]/div[5]/div[4]/div/div[2]/form/div[3]/input'
    user_password = '/html/body/div[2]/div[5]/div[4]/div/div[2]/form/div[4]/input'
    user_password_2 = '/html/body/div[2]/div[5]/div[4]/div/div[2]/form/div[5]/input'
    # capcha = '//div[@class="recaptcha-checkbox-checkmark"]'
    accept_check_box = '//*[@id="accepted_offer-6928"]'
    regist_button = '/html/body/div[2]/div[5]/div[4]/div/div[2]/form/div[7]/input'

    #Geters
    def get_icon_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.icon_login)))
    def get_registration_button_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.registration_button_1)))
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))
    def get_user_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_phone)))
    def get_user_emeil(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_emeil)))
    def get_user_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_password)))
    def get_user_password_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_password_2)))
    # def get_capcha(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.capcha)))
    def get_accept_check_box(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.accept_check_box)))
    def get_regist_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.regist_button)))


    # Actions
    def click_icon_login(self):
        self.get_icon_login().click()
        print('click icon login')

    def click_registration_button_1(self):
        self.get_registration_button_1().click()
        print("click button registr_1")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("INPUT user name")

    def input_user_phone(self, user_phone):
        self.get_user_phone().send_keys(user_phone)
        print("INPUT user_phone")

    def input_user_emeil(self, user_emeil):
        self.get_user_emeil().send_keys(user_emeil)
        print("INPUT user name")

    def input_user_password(self, user_password):
        self.get_user_password().send_keys(user_password)
        print("INPUT PASSWORD")

    def input_user_password_2(self, user_password_2):
        self.get_user_password_2().send_keys(user_password_2)
        print("INPUT USER PASSWORD 2")

    # def click_capcha(self):
    #     self.get_capcha().click()
    #     print("CLICK capcha")

    def click_accept_check_box(self):
        self.get_accept_check_box().click()
        print('Click check box')

    def click_regist_button(self):
        self.get_regist_button().click()
        print('Click registr button')

    # Methods
    def autorithation(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.click_icon_login()
        self.click_registration_button_1()
        self.input_user_name('Siarhei')
        self.input_user_phone('291039932')
        self.input_user_emeil('feloc69470@carpetra.com')
        self.input_user_password('123AD321!')
        self.input_user_password_2('123AD321!')
        self.click_accept_check_box()
        self.click_regist_button()
        # self.click_capcha()

