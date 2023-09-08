from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import re

from locators.elements_page_locators import ShoppingBasketLocators


def get_goods_description_text_by_index(driver, index):
    xpath = f"//a[@data-testid='title'][{index}]"
    goods_title_text = driver.find_element(By.XPATH, xpath).text
    return goods_title_text


def getDevicePriceText(driver, index):
    xpath = f"//p[@data-testid='cost'][{index}]"
    return int(re.sub(r'\D', '', driver.find_element(By.XPATH, xpath).text))


def set_goods_count_value(driver, count):
    universal_price_input_value = driver.find_element(By.XPATH,
                                                      "//input[@data-testid='cart-counter-input']")
    universal_price_input_value.clear()
    time.sleep(2)
    universal_price_input_value.send_keys(count)


def getSumPriceText(driver):
    return int(
        re.sub(r'\D', '', driver.find_element(By.XPATH, ShoppingBasketLocators.SUM_PRICE_TEXT).text))


def isBasketEmptyStatusTextPresent(driver):
    try:
        time.sleep(2)
        driver.find_element(By.XPATH, ShoppingBasketLocators.EMPTY_STATUS_TEXT)
        time.sleep(2)
    except NoSuchElementException:
        time.sleep(2)
        return False
    return True


def getGoodsInCartListSize(driver):
    goods_in_cart_title_price = []
    for elem in driver.find_elements(By.XPATH, ShoppingBasketLocators.GOODS_IN_CART_TITLE_PRICE):
        goods_in_cart_title_price.append(elem.text)
    return goods_in_cart_title_price.__len__()
