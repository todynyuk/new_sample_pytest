from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


def click_universal_subcategory_menu_link(sub_category, driver):
    time.sleep(5)
    button = driver.find_element(By.PARTIAL_LINK_TEXT, f"{sub_category}")
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(button).click(button).perform()
    time.sleep(3)
