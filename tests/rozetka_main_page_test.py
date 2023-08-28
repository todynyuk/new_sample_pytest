import logging
import time
import pytest
from pytest_zebrunner import *
from pytest_zebrunner import CurrentTestRun
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from selenium.webdriver.common.by import By
from pages.main_page import set_search_input, click_search_button, verify_wrong_search_request
from utils import utils

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)
attach_test_run_label("TestRunLabel1", "PyTest")
attach_test_run_label("TestRunLabel2", "Zebrunner")
attach_test_run_artifact_reference("Zebrunner", "https://zebrunner.com/")
attach_test_run_artifact_reference("PyTest", "https://docs.pytest.org/en/latest/")
attach_test_run_artifact_reference("PyTest Zebrunner agent", "https://zebrunner.com/documentation/reporting/pytest/")
CurrentTestRun.set_locale("en_US")
CurrentTestRun.set_build("TR build version")

url = "https://rozetka.com.ua/ua/"
search_correct_value = "Agm A9"


@pytest.mark.maintainer("todynyuk")
def test_correct_search(driver):
    driver.get(url=url)
    time.sleep(3)
    utils.pass_cloudflare(driver)
    time.sleep(3)
    utils.pass_cloudflare(driver)
    time.sleep(3)
    utils.attach_screenshot(driver)
    driver.find_element(by=By.XPATH, value="//input[contains(@class,'search-form__input')]").send_keys(
        search_correct_value)
    utils.attach_screenshot(driver)
    driver.find_element(by=By.XPATH, value="//button[contains(@class,'button_color_green')]").click()
    time.sleep(2)
    utils.attach_screenshot(driver)
    title_text = driver.find_element(by=By.XPATH, value="(//span[@class='goods-tile__title'])[1]").text
    assert str(title_text).lower().__contains__(search_correct_value.lower()), "Search text not" \
                                                                               " contains in all " \
                                                                               "goods title texts"


@pytest.mark.maintainer("todynyuk")
def test_rozetka_correct_search(driver):
    logger.info("Attaching labels, artifacts and artifacts references to test")
    attach_test_label("TestLabel", "Rozetka")
    attach_test_run_artifact_reference("Rozetka", "https://rozetka.com.ua/ua/")
    logger.info("Navigating to url: " + url)
    driver.get(url=url)
    time.sleep(3)
    utils.pass_cloudflare(driver)
    time.sleep(3)
    utils.pass_cloudflare(driver)
    time.sleep(3)
    utils.attach_screenshot(driver)
    logger.info("Performing search with value: " + search_correct_value)
    set_search_input(driver, search_correct_value)
    click_search_button(driver)
    utils.attach_screenshot(driver)
    logger.info("Verify first search result contains: '" + search_correct_value + "'")
    goods_title_text = driver.find_element(By.XPATH, f"//span[@class='goods-tile__title'][{1}]").text
    logger.info(goods_title_text)
    assert str(goods_title_text.lower()).__contains__(
        search_correct_value.lower()), "Device description not contains search_value"
    logger.info("'test_rozetka_correct_search' was successfully finished")


@pytest.mark.maintainer("todynyuk")
def test_rozetka_incorrect_search(driver):
    logger.info("Attaching labels, artifacts and artifacts references to test")
    attach_test_label("TestLabel", "Rozetka")
    attach_test_run_artifact_reference("Rozetka", "https://rozetka.com.ua/ua/")
    logger.info("Navigating to url: " + url)
    driver.get(url=url)
    time.sleep(3)
    utils.pass_cloudflare(driver)
    time.sleep(3)
    utils.attach_screenshot(driver)
    logger.info("Performing search with value: " + "hgvhvg")
    set_search_input(driver, "hgvhvg")
    click_search_button(driver)
    utils.attach_screenshot(driver)
    logger.info("Verify not_found_text is present")
    assert verify_wrong_search_request(driver), "Wrong request text isn`t presented"
    logger.info("'test_rozetka_incorrect_search' was successfully finished")
