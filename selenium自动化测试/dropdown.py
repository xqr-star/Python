# 定位下拉框 然后点击
from selenium import webdriver
import time
import os
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
# / \  正则表达式
file = "file:///" + os.path.abspath("E:\BIT—比特\测试\selenium2html\drop_down.html")
driver.get(file)
driver.maximize_window()

# 使用xpath定位
time.sleep(2)
# driver.find_element_by_xpath("//*[@id='ShippingMethod']/option[3]").click()

# 使用css selector 定位
# driver.find_element_by_css_selector("#ShippingMethod > option:nth-child(3)").click()


# 先定位option 然后click点击  for循环判断
options= driver.find_element_by_id("ShippingMethod").find_elements_by_tag_name("option")
# for option in options:
#     # option.get 获取对应的属性
#     if option.get_attribute('value') == '10.69':
#         option.click()

# 或者直接使用数组的定位方式
options[2].click()



time.sleep(2)
driver.quit()
