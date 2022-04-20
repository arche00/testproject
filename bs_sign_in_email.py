from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import time
import pytest



userName = "jio_ct7MvC"
accessKey = "8TRmABuRz78SsyGvic7k"

desired_caps ={
    "platformName": "Android",
    "udid": "287860acb13f7ece",
    "build": "Python 0419",
    "device": "Samsung Galaxy S22",
    "app": "bs://14d7731f7be7c293d90c4b886c013ef94b888ee2",
    "browserstack.networkLogs": 'true',
    "language": "ko",
    "locale": "kr",
    "automationName": "Appium",
    "noReset": "true"
}

#driver = webdriver.Remote("https://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_caps)
driver = webdriver.Remote("https://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_caps)


#driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_cap)

#driver.implicitly_wait(10)

#wait = WebDriverWait(driver, 10)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//android.widget.TextView[@text = '로그인']")))

login = driver.find_element(By.XPATH,"//android.widget.TextView[@text = '로그인']")

login.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,"//android.widget.TextView[@text = '이메일로 로그인']")))

#wait = WebDriverWait(driver, 10)

email_signin = driver.find_element(By.XPATH,"//android.widget.TextView[@text = '이메일로 로그인']")

email_signin.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,"//android.view.View[1]/android.widget.EditText")))



email = driver.find_element(By.XPATH,"//android.view.View[1]/android.widget.EditText")


email.send_keys("teacher04@sharklasers.com")

password = driver.find_element(By.XPATH,"//android.view.View[2]/android.widget.EditText")
password.send_keys("a1234567")

email_signin1 = driver.find_element(By.XPATH,"//android.widget.Button[@text = '이메일로 로그인']")

email_signin1.click()

time.sleep(10)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,"//android.widget.TextView[@text = 'MY']")))

my = driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'MY']")

TouchAction(driver).tap(my).perform()
TouchAction(driver).tap(my).perform()


time.sleep(10)

setting_btn = driver.find_element(By.XPATH, "//android.view.ViewGroup[2]/android.widget.ImageView")

TouchAction(driver).tap(setting_btn).perform()

time.sleep(10)

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import time
import pytest



userName = "jio_ct7MvC"
accessKey = "8TRmABuRz78SsyGvic7k"

desired_caps ={
    "platformName": "Android",
    "udid": "287860acb13f7ece",
    "build": "Python Android",
    "device": "Samsung Galaxy S22",
    "app": "bs://14d7731f7be7c293d90c4b886c013ef94b888ee2",
    "browserstack.networkLogs": 'true',
    #"app": "/Users/classting/apk/com.Classting.apk",
    "language": "ko",
    "locale": "kr",
    "automationName": "Appium",
    "appPackage": "com.Classting",
    "appActivity": ".MainActivity"
}

#driver = webdriver.Remote("https://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_caps)
driver = webdriver.Remote("https://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_caps)


#driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_cap)

#driver.implicitly_wait(10)

#wait = WebDriverWait(driver, 10)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//android.widget.TextView[@text = '로그인']")))

login = driver.find_element(By.XPATH,"//android.widget.TextView[@text = '로그인']")

login.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,"//android.widget.TextView[@text = '이메일로 로그인']")))

#wait = WebDriverWait(driver, 10)

email_signin = driver.find_element(By.XPATH,"//android.widget.TextView[@text = '이메일로 로그인']")

email_signin.click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,"//android.view.View[1]/android.widget.EditText")))



email = driver.find_element(By.XPATH,"//android.view.View[1]/android.widget.EditText")


email.send_keys("teacher04@sharklasers.com")

password = driver.find_element(By.XPATH,"//android.view.View[2]/android.widget.EditText")
password.send_keys("a1234567")

email_signin1 = driver.find_element(By.XPATH,"//android.widget.Button[@text = '이메일로 로그인']")

email_signin1.click()

time.sleep(10)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,"//android.widget.TextView[@text = 'MY']")))

my = driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'MY']")

TouchAction(driver).tap(my).perform()
TouchAction(driver).tap(my).perform()


time.sleep(10)

setting_btn = driver.find_element(By.XPATH, "//android.view.ViewGroup[2]/android.widget.ImageView")

TouchAction(driver).tap(setting_btn).perform()

time.sleep(10)

driver.swipe(start_x=574, start_y=1896, end_x=562, end_y=938, duration=300)

driver.swipe(start_x=574, start_y=1896, end_x=562, end_y=938, duration=300)

logout = driver.find_element(By.XPATH, "//android.widget.TextView[@text = '로그아웃']")

TouchAction(driver).tap(logout).perform()

time.sleep(10)


#driver.implicitly_wait(10)


driver.swipe(start_x=574, start_y=1896, end_x=562, end_y=938, duration=300)

driver.swipe(start_x=574, start_y=1896, end_x=562, end_y=938, duration=300)

logout = driver.find_element(By.XPATH, "//android.widget.TextView[@text = '로그아웃']")

TouchAction(driver).tap(logout).perform()

time.sleep(10)





#driver.implicitly_wait(10)
