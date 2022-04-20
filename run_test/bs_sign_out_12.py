from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pytest



userName = "tjkim_yip4Mu"
accessKey = "cAa6AHTxytDE459jqjK6"

desired_caps ={
    "platformName": "Android",
    "udid": "287860acb13f7ece",
    "build": "Python Android",
    "device": "Samsung Galaxy S22",
    "app": "bs://14d7731f7be7c293d90c4b886c013ef94b888ee2",
    "browserstack.networkLogs": 'true',
    "browserstack.timezone": 'Seoul',
    #"app": "/Users/classting/apk/com.Classting.apk",
    "language": "ko",
    "locale": "kr",
    "automationName": "Appium",
    "appPackage": "com.Classting",
    "appActivity": ".MainActivity",
    "noReset": "true"
}

#driver = webdriver.Remote("https://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_caps)
driver = webdriver.Remote("https://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_caps)


time.sleep(10)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,"//android.widget.TextView[@text = 'MY']")))

my = driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'MY']")

actions = ActionChains(driver)
actions.move_to_element(my).click(my).perform()
#actions.perform()

time.sleep(10)

setting_btn = driver.find_element(By.XPATH, "//android.view.ViewGroup[2]/android.widget.ImageView")

actions.move_to_element(setting_btn).click(setting_btn).perform()

time.sleep(10)

driver.swipe(start_x=574, start_y=1896, end_x=562, end_y=938, duration=300)

#driver.swipe(start_x=574, start_y=1896, end_x=562, end_y=938, duration=300)

logout = driver.find_element(By.XPATH, "//android.widget.TextView[@text = '로그아웃']")

actions.move_to_element(logout).click(logout).perform()

time.sleep(10)


driver.quit()