import logging
import time

import pytest
from pytest_zebrunner import attach_test_run_label, attach_test_run_artifact_reference, attach_test_label
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from pytest_zebrunner import CurrentTestRun

from pages.devices_category_page import getSmartphonePriceText, get_goods_title_text_by_index, clickBuyButtonByIndex, \
    get_goods_description_text_by_index, clickOnShoppingBasketButton
from pages.main_page import click_universal_category_link
from pages.shopping_basket_page import isBasketEmptyStatusTextPresent, getGoodsInCartListSize, getDevicePriceText, \
    set_goods_count_value, getSumPriceText
from pages.subcategory_page import click_universal_subcategory_menu_link
from utils.attachments import attach_screenshot
from utils.utils import solv_multiple_cloudflare

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)

attach_test_run_label("TestRunLabelRunName", "PyTest")
attach_test_run_label("TestRunLabelResourceName", "Rozetka")

attach_test_run_artifact_reference("Rozetka", "https://rozetka.com.ua/ua/")

CurrentTestRun.set_locale("en_US")
CurrentTestRun.set_build("TR build version")

url = "https://rozetka.com.ua/ua/"


@pytest.mark.maintainer("todynyuk")
def testUsualPriceItemAndInBasket(driver):
    logger.info("Attaching labels, artifacts and artifacts references to test")
    attach_test_label("TestLabel", "Rozetka")
    attach_test_run_artifact_reference("Rozetka", "https://rozetka.com.ua/ua/")
    logger.info("Navigating to url: " + url)
    driver.get(url=url)
    solv_multiple_cloudflare(driver)
    attach_screenshot(driver)
    click_universal_category_link(driver, "Смартфони")
    logger.info("click to smartphone category")
    attach_screenshot(driver)
    click_universal_subcategory_menu_link("Смартфони", driver)
    logger.info("click to smartphone subcategory")
    attach_screenshot(driver)
    smartphone_price = getSmartphonePriceText(driver, 1)
    short_characteristics = get_goods_title_text_by_index(driver, 1)
    driver.implicitly_wait(2)
    clickBuyButtonByIndex(driver, 1)
    logger.info("click more about device link")
    attach_screenshot(driver)
    clickOnShoppingBasketButton(driver)
    logger.info("click on shopping basket button")
    attach_screenshot(driver)
    item_card_description_text = get_goods_description_text_by_index(driver, 1)
    assert str(short_characteristics).__contains__(
        item_card_description_text), "Device Short_characteristics not equals"
    shopping_basket_item_price = getDevicePriceText(driver, 1)
    assert smartphone_price == shopping_basket_item_price, "Prices are not equals"
    set_goods_count_value(driver, 3)
    logger.info("set goods count value")
    attach_screenshot(driver)
    smartphone_price_multiply = (smartphone_price * 3)
    time.sleep(2)
    assert smartphone_price_multiply == getSumPriceText(driver), "Prices are not equals"
    logger.info("'testUsualPriceItemAndInBasket' was successfully finished")


@pytest.mark.maintainer("todynyuk")
def testAddGoodsInBasketAndCheckItEmpty(driver):
    logger.info("Attaching labels, artifacts and artifacts references to test")
    attach_test_label("TestLabel", "Rozetka")
    attach_test_run_artifact_reference("Rozetka", "https://rozetka.com.ua/ua/")
    logger.info("Navigating to url: " + url)
    driver.get(url=url)
    solv_multiple_cloudflare(driver)
    logger.info("trying to solv cloudflare protection")
    attach_screenshot(driver)
    click_universal_category_link(driver, "Смартфони")
    logger.info("click to smartphone category")
    attach_screenshot(driver)
    click_universal_subcategory_menu_link("Смартфони", driver)
    logger.info("click to smartphone subcategory")
    attach_screenshot(driver)
    clickBuyButtonByIndex(driver, 1)
    logger.info("click buy button by first index")
    attach_screenshot(driver)
    clickOnShoppingBasketButton(driver)
    logger.info("click on shopping basket button")
    attach_screenshot(driver)
    assert isBasketEmptyStatusTextPresent(driver) == False, \
        "Basket empty status text is presented"
    goods_in_shopping_basket_count = getGoodsInCartListSize(driver)
    logger.info("get goods list size in basket")
    assert goods_in_shopping_basket_count > 0, "Basket is empty"
    logger.info("'testAddGoodsInBasketAndCheckItEmpty' was successfully finished")
