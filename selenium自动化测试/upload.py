from selenium import webdriver
import time
import os

# 搜索一个单词是否在html原生代码中存在 ctrl+f
# 获取浏览器的驱动
driver = webdriver.Chrome()
file = "file:///" + os.path.abspath("E:\BIT—比特\测试\selenium2html/upload.html")
driver.get(file)
driver.maximize_window()

# driver.find_element_by_tag_name("input").click()
# 上传操作 定位并且发送send_keys即可
driver.find_element_by_tag_name("input").send_keys("C:/Users/11596\Pictures\联想锁屏壁纸/8490175.jpg")
time.sleep(2)

driver.quit()
