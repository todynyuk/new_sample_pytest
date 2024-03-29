import logging
import time
import pytest
from pytest_zebrunner import attach_test_run_label, attach_test_run_artifact_reference, attach_test_label
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from pytest_zebrunner import CurrentTestRun

from pages.device_page import verifyChosenParameterInShortCharacteristics, verifyChosenParamInCharacteristicsTitle
from pages.devices_category_page import clear_and_set_sorting_price, click_ok_button, \
    check_is_all_goods_prices_less_than_choosen, click_check_box_filter, verify_is_search_think_present_in_goods_title, \
    check_is_all_goods_available, clickUniversalShowCheckBoxButton, clickLinkMoreAboutDevice, clickDropdownOption, \
    isAllGoodsSortedFromLowToHighPrice, isAllGoodsSortedFromHighToLowPrice, clickBuyButtonByIndex, \
    isAddedToCartGoodsCounterTextPresent, check_chosen_filters_contains_chosen_brands
from pages.main_page import click_universal_category_link
from pages.subcategory_page import click_universal_subcategory_menu_link
from utils.attachments import attach_screenshot
from utils import utils
from utils.utils import solv_multiple_cloudflare

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


@pytest.mark.maintainer("todynyuk")
@pytest.mark.skip(reason="Rozetka have problem with sorting by price")
def testFilterByBrandNameMaxCustomPriceAndAvailable(driver):
    logger.info("Attaching labels, artifacts and artifacts references to test")
    attach_test_label("TestLabel", "Rozetka")
    attach_test_run_artifact_reference("Rozetka", "https://rozetka.com.ua/ua/")
    logger.info("Navigating to url: " + url)
    driver.get(url=url)
    time.sleep(3)
    solv_multiple_cloudflare(driver)
    logger.info("trying to solv cloudflare protection")
    time.sleep(3)
    attach_screenshot(driver)
    click_universal_category_link(driver, "Смартфони")
    logger.info("click to smartphone category")
    attach_screenshot(driver)
    click_universal_subcategory_menu_link("Мобільні", driver)
    logger.info("click to smartphone subcategory")
    attach_screenshot(driver)
    logger.info("Verify if title contains subcategory: '" + "Мобільні" + "'")
    assert str(driver.title).lower().__contains__(("Мобільні").lower())
    clear_and_set_sorting_price(driver, "max", 4000)
    click_ok_button(driver)
    logger.info("click ok button")
    attach_screenshot(driver)
    logger.info("Verify if all goods prices less than chosen: '" + "4000" + "'")
    assert check_is_all_goods_prices_less_than_choosen(driver, 4000), \
        "One or more things have price more than chosen"
    click_check_box_filter(driver, "Sigma")
    logger.info("click check box filter by brand Sigma")
    attach_screenshot(driver)
    assert verify_is_search_think_present_in_goods_title(driver, "Sigma"), \
        "Search result don`t contains chosen brand"
    click_check_box_filter(driver, "Є в наявності")
    logger.info("click check box filter is present")
    attach_screenshot(driver)
    length = check_is_all_goods_available(driver, "Немає в наявності")
    assert length == 0, "One or more goods are not available"
    logger.info("'testFilterByBrandNameMaxCustomPriceAndAvailable' was successfully finished")


@pytest.mark.maintainer("todynyuk")
def testVerifyItemRamMatrixTypeAndProcessor(driver):
    logger.info("Attaching labels, artifacts and artifacts references to test")
    attach_test_label("TestLabel", "Rozetka")
    attach_test_run_artifact_reference("Rozetka", "https://rozetka.com.ua/ua/")
    logger.info("Navigating to url: " + url)
    driver.get(url=url)
    time.sleep(3)
    solv_multiple_cloudflare(driver)
    logger.info("trying to solv cloudflare protection")
    time.sleep(5)
    attach_screenshot(driver)
    click_universal_category_link(driver, "Ноутбуки")
    logger.info("click to laptop category")
    attach_screenshot(driver)
    click_universal_subcategory_menu_link("моноблоки", driver)
    logger.info("click to mono blocks subcategory")
    attach_screenshot(driver)
    click_check_box_filter(driver, "Intel Core i5")
    logger.info("click check box filter Intel Core i5 ")
    attach_screenshot(driver)
    click_check_box_filter(driver, "Моноблок")
    logger.info("click check box filter Monoblock")
    attach_screenshot(driver)
    click_check_box_filter(driver, "8 ГБ")
    logger.info("click check box filter 8Gb")
    attach_screenshot(driver)
    clickUniversalShowCheckBoxButton(driver, "Тип матриці")
    logger.info("click show checkbox button")
    attach_screenshot(driver)
    click_check_box_filter(driver, "IPS")
    logger.info("click check box filter ips")
    attach_screenshot(driver)
    click_check_box_filter(driver, "Новий")
    logger.info("click check box filter new")
    attach_screenshot(driver)
    click_check_box_filter(driver, "Є в наявності")
    logger.info("click check box filter is present")
    attach_screenshot(driver)
    length = check_is_all_goods_available(driver,
                                          "Немає в наявності")
    logger.info("Verify that all goods are  available'""'")
    assert length == 0, "One or more goods are not available"
    clickLinkMoreAboutDevice(driver, 1)
    logger.info("click more about device link")
    attach_screenshot(driver)
    assert verifyChosenParameterInShortCharacteristics(driver, "Intel Core i5"), \
        "Processor name text not contains in about device text"
    assert verifyChosenParameterInShortCharacteristics(driver, "8 ГБ"), \
        "Ram text not contains in about device text"
    assert verifyChosenParameterInShortCharacteristics(driver, "IPS"), \
        "Matrix type text not contains in about device text"
    assert verifyChosenParamInCharacteristicsTitle(driver,
                                                   "Моноблок"), \
        "Computer type text not contains in description device text"
    logger.info("'testVerifyItemRamMatrixTypeAndProcessor' was successfully finished")


@pytest.mark.maintainer("todynyuk")
@pytest.mark.skip(reason="Rozetka have problem with sorting by price")
def testVerifySortByPrice(driver):
    logger.info("Attaching labels, artifacts and artifacts references to test")
    attach_test_label("TestLabel", "Rozetka")
    attach_test_run_artifact_reference("Rozetka", "https://rozetka.com.ua/ua/")
    logger.info("Navigating to url: " + url)
    driver.get(url=url)
    time.sleep(3)
    solv_multiple_cloudflare(driver)
    logger.info("trying to solv cloudflare protection")
    time.sleep(3)
    attach_screenshot(driver)
    click_universal_category_link(driver, "Смартфони")
    logger.info("click to smartphone category")
    attach_screenshot(driver)
    click_universal_subcategory_menu_link("Мобільні", driver)
    logger.info("click to smartphone subcategory")
    attach_screenshot(driver)
    clickDropdownOption(driver, "Від дешевих до дорогих")
    logger.info("click filter from low to high price")
    attach_screenshot(driver)
    is_good_prices_low_to_hight = isAllGoodsSortedFromLowToHighPrice(driver)
    assert is_good_prices_low_to_hight, "One or more prices not sorted from low to high price"
    clickDropdownOption(driver, "Від дорогих до дешевих")
    logger.info("click filter from high to low price")
    attach_screenshot(driver)
    is_good_prices_hight_to_low = isAllGoodsSortedFromHighToLowPrice(driver)
    assert is_good_prices_hight_to_low, "One or more prices not sorted from high to low price"
    logger.info("'testVerifySortByPrice' was successfully finished")


@pytest.mark.maintainer("todynyuk")
def testAddingAndCountGoodsInBasket(driver):
    logger.info("Attaching labels, artifacts and artifacts references to test")
    attach_test_label("TestLabel", "Rozetka")
    attach_test_run_artifact_reference("Rozetka", "https://rozetka.com.ua/ua/")
    logger.info("Navigating to url: " + url)
    driver.get(url=url)
    utils.pass_cloudflare(driver)
    solv_multiple_cloudflare(driver)
    logger.info("trying to solv cloudflare protection")
    attach_screenshot(driver)
    click_universal_category_link(driver, "Смартфони")
    logger.info("click to smartphone category")
    attach_screenshot(driver)
    click_universal_subcategory_menu_link("Смартфони", driver)
    logger.info("click to smartphone subcategory")
    attach_screenshot(driver)
    assert isAddedToCartGoodsCounterTextPresent(driver) == False, \
        "Cart Goods Counter Text isn't presented"

    clickBuyButtonByIndex(driver, 1)
    logger.info("click more about device link")
    attach_screenshot(driver)
    assert isAddedToCartGoodsCounterTextPresent(driver) != False, \
        "Cart Goods Counter Text isn't presented"
    logger.info("'testAddingAndCountGoodsInBasket' was successfully finished")


@pytest.mark.maintainer("todynyuk")
def test_choose_brands_and_check(driver):
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
    click_check_box_filter(driver, "Huawei")
    logger.info("click check box filter by brand Huawei")
    attach_screenshot(driver)
    click_check_box_filter(driver, "Infinix")
    logger.info("click check box filter by brand Infinix")
    attach_screenshot(driver)
    click_check_box_filter(driver, "Motorola")
    logger.info("click check box filter by brand Motorola")
    attach_screenshot(driver)
    assert check_chosen_filters_contains_chosen_brands(driver, "Huawei"), \
        "List chosen parameters not contains this parameter"
    assert check_chosen_filters_contains_chosen_brands(driver, "Infinix"), \
        "List chosen parameters not contains this parameter"
    assert check_chosen_filters_contains_chosen_brands(driver, "Motorola"), \
        "List chosen parameters not contains this parameter"
    logger.info("'test_choose_brands_and_check' was successfully finished")
