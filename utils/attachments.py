from pytest_zebrunner import attach_test_screenshot


def attach_screenshot(driver):
    driver.save_screenshot("screenshot.png")
    attach_test_screenshot("screenshot.png")
