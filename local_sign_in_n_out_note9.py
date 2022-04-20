from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


desired_cap ={
    "platformName": "Android",
    "udid": "287860acb13f7ece",
    "app": "/Users/classting/apk/com.Classting.apk",
    "automationName": "Appium",
    "newCommandTimeout": 300,
    "appPackage": "com.Classting",
    "appActivity": ".MainActivity",
    "noReset": "true"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

# 1.메인화면 로그인 버튼 클릭
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,"//android.widget.TextView[@text = '로그인']")))

login = driver.find_element(By.XPATH,
                            "//android.widget.TextView[@text = '로그인']")
login.click()

# 2.이메일로 로그인 클릭
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,
                                                                "//android.widget.TextView[@text = '이메일로 로그인']")))
email_signin = driver.find_element(By.XPATH,
                            "//android.widget.TextView[@text = '이메일로 로그인']")

email_signin.click()

# 3.이메일 / 비밀번호 입력하고 로그인 클릭
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,"//android.view.View[1]/android.widget.EditText")))

email = driver.find_element(By.XPATH,
                            "//android.view.View[1]/android.widget.EditText")

email.send_keys("teacher04@sharklasers.com")

password = driver.find_element(By.XPATH, "//android.view.View[2]/android.widget.EditText")
password.send_keys("a1234567")

email_signin1 = driver.find_element(By.XPATH, "//android.widget.Button[@text = '이메일로 로그인']")
email_signin1.click()

driver.implicitly_wait(10)
time.sleep(10)

# 4.MY탭 클릭
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,"//android.widget.TextView[@text = 'MY']")))
my = driver.find_element(By.XPATH, "//android.widget.TextView[@text = 'MY']")
actions = ActionChains(driver)
actions.move_to_element(my).click(my).perform()
time.sleep(10)

# 5.우측 상단 설정 버튼 클릭
setting_btn = driver.find_element(By.XPATH, "//android.view.ViewGroup[2]/android.widget.ImageView")
actions.move_to_element(setting_btn).click(setting_btn).perform()
time.sleep(10)

# 6.화면 아래로 스크롤
driver.swipe(start_x=574, start_y=1896, end_x=562, end_y=938, duration=300)

#driver.swipe(start_x=574, start_y=1896, end_x=562, end_y=938, duration=300)

# 7.로그아웃 버튼 클릭
logout = driver.find_element(By.XPATH, "//android.widget.TextView[@text = '로그아웃']")
actions.move_to_element(logout).click(logout).perform()
time.sleep(10)

driver.quit()

