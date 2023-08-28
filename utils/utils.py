from pytest_zebrunner import attach_test_screenshot
from selenium.webdriver.common.by import By


def pass_cloudflare(driver):
    frame = driver.find_element(by=By.XPATH, value="//iframe[@title='Widget containing a Cloudflare security challenge']")
    driver.switch_to.frame(frame)
    driver.find_element(by=By.XPATH, value="//label[@class='ctp-checkbox-label']").click()

def attach_screenshot(driver):
    driver.save_screenshot("screenshot.png")
    attach_test_screenshot("screenshot.png")