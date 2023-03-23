import AndroidDriverInit
from appium.webdriver.common.appiumby import AppiumBy
import time

driver = AndroidDriverInit.driver

def SampleTest():
    el = driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.RelativeLayout/android.widget.TextView[1]')
    el.click()
    time.sleep(5)
    assert "100 %" in driver.page_source