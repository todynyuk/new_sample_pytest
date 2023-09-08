from selenium.webdriver.common.by import By
import time
import re
from selenium.webdriver.common.action_chains import ActionChains
from locators.elements_page_locators import DevicePageLocators


def verify_device_short_characteristic(driver, param):
    action = ActionChains(driver)
    element = driver.find_element(By.XPATH, "//ul[@class='tabs__list']")
    action.move_to_element(element).perform()
    short_characteristic = driver.find_element(By.XPATH, DevicePageLocators.SHORT_CHARACTERISTICS_TITLE).text
    return short_characteristic.__contains__(str(param))


def get_device_short_characteristic(driver):
    return driver.find_element(By.XPATH, DevicePageLocators.SHORT_CHARACTERISTICS_TITLE).text


def get_chosen_product_price(driver):
    time.sleep(3)
    chosen_product_price = re.sub(r'\D', '', driver.find_element(By.XPATH, DevicePageLocators.PRODUCT_PRICE).text)
    return chosen_product_price


def verifyChosenParameterInShortCharacteristics(driver, param):
    time.sleep(3)
    driver.execute_script("arguments[0].scrollIntoView();",
                          driver.find_element(By.XPATH, DevicePageLocators.SHORT_CHARACTERISTIC))
    short_characteristic = driver.find_element(By.XPATH, DevicePageLocators.SHORT_CHARACTERISTIC).text
    return short_characteristic.__contains__(str(param))


def verifyChosenParamInCharacteristicsTitle(driver, param):
    short_characteristic = driver.find_element(By.XPATH, DevicePageLocators.SHORT_CHARACTERISTICS_TITLE).text
    return short_characteristic.__contains__(str(param))
