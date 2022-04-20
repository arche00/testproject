from addons.element_extensions import ElementExtensions
from addons.swipe_and_find_element import SwipeAndFindElement
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: daily_all
    Package: TestProject.Generated.Tests.DailyAll
    Test: iOS_signOut
    Generated by: TJ Kim (arche0840@gmail.com)
    Generated on 04/19/2022, 05:33:32
"""


@pytest.fixture()
def driver():
    capabilities = {
        "platformName": "iOS",
        "udid": "c86c210c6e6c2f7778c0ea589dc1612db565a23d",
        "bundleId": "com.classting.iphone",
    }
    driver = webdriver.Remote(token="GeWPVxkDL49XzPz0Z4AaKh44m8er7fCFzgldZlXcyQg1",
                              project_name="daily_all",
                              job_name="iOS_signOut",
                              desired_capabilities=capabilities)
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """This test was auto generated from steps of the 'check_sign_in' test."""

    # 1. Launch the app
    driver.launch_app()

    # 2. Click 'MY1'
    my1 = driver.find_element(By.XPATH,
                              "//XCUIElementTypeStaticText[@value = 'MY']\n")
    my1.click()

    # 3. Tap '수직 스크롤 막대, 1페이지' at '10'% width and '10'% height
    _1_ = (MobileBy.ACCESSIBILITY_ID, "수직 스크롤 막대, 1페이지")
    driver.addons().execute(
        ElementExtensions.relativetapios(
            horizontal=10,
            vertical=10), *_1_)

    # 4. Swipe 'DOWN' at Most '[NONE]' Times Until Element is Displayed
    _ = (MobileBy.ACCESSIBILITY_ID, "로그아웃")
    driver.addons().execute(
        SwipeAndFindElement.swipeuntilelementiosvertical(
            direction="DOWN",
            amountOfSwipes=0), *_)

    # 5. Click '로그아웃'
    step_settings = StepSettings(sleep_time=5000,
                                 sleep_timing_type=SleepTimingType.After)
    with DriverStepSettings(driver, step_settings):
        _ = driver.find_element(By.XPATH,
                                "//XCUIElementTypeOther[7]/XCUIElementTypeOther")
        _.click()