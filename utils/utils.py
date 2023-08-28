from pytest_zebrunner import attach_test_screenshot
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


def pass_cloudflare(driver):
    frame = driver.find_element(by=By.XPATH,
                                value="//iframe[@title='Widget containing a Cloudflare security challenge']")
    driver.switch_to.frame(frame)
    driver.find_element(by=By.XPATH, value="//label[@class='ctp-checkbox-label']").click()


def attach_screenshot(driver):
    driver.save_screenshot("screenshot.png")
    attach_test_screenshot("screenshot.png")


def isElementPresent(driver, xpath):
    try:
        time.sleep(2)
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

def solv_multiple_cloudflare(driver):
    time.sleep(3)
    pass_cloudflare(driver)
    time.sleep(2)
    while True:
        if isElementPresent(driver, "//input[contains(@class,'search-form__input')]"):
            break
        else:
            pass_cloudflare(driver)
            time.sleep(3)
