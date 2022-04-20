from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps ={
    "platformName": "Android",
    "udid": "287860acb13f7ece",
    "app": "/Users/classting/apk/com.Classting.apk",
    "automationName": "Appium",
    "newCommandTimeout": 300,
    "appPackage": "com.Classting",
    "appActivity": ".MainActivity"
}

driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)

driver.implicitly_wait(5)

login = driver.find_element(By.XPATH,
                            "//android.widget.TextView[@text = '로그인']")

login.click()

driver.implicitly_wait(5)

email_signin = driver.find_element(By.XPATH,
                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ImageView")

email_signin.click()

driver.implicitly_wait(5)

email = driver.find_element(By.XPATH,
                            "//android.view.View[1]/android.widget.EditText")

email.send_keys("teacher04@sharklasers.com")

password = driver.find_element(By.XPATH,
                               "//android.view.View[2]/android.widget.EditText")
password.send_keys("a1234567")

email_signin1 = driver.find_element(By.XPATH,
                             "//android.widget.Button[@text = '이메일로 로그인']")

email_signin1.click()

driver.implicitly_wait(10)
