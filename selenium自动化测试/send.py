# alert 事件中如果弹出的对话框 是一个要求输入内容的东西、
# 那么做法和思路原理都是
# 首先获取操作的句柄 然后在里面send——keys即可
from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
file = "file:///" + os.path.abspath("E:\BIT—比特\测试\selenium2html/send.html")
driver.get(file)
driver.maximize_window()

time.sleep(2)
# driver.find_element_by_link_text("请点击").click()
driver.find_element_by_tag_name("input").click()


time.sleep(3)
# 获取操作alert的句柄、
alert = driver.switch_to.alert
alert.send_keys("世界，解淇茹会加油的")

# 确认弹出框并且关闭弹出框
alert.accept()
# 取消弹出框
# alert.dismiss()

time.sleep(2)
driver.quit()