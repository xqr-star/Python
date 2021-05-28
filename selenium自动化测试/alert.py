# alert 事件
# 必须要把alert 关闭以后才可以进行点击其他的地方
# 为什么我的弹框也不弹出来  适合bootstrap 有什么关系吗 还是什么原因呢？
# 引入的bootstrap框架不合适 导致问题出现了
from selenium import webdriver
import time
import os

from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
file = "file:///" + os.path.abspath("E:\BIT—比特\测试\selenium2html/alert.html")
driver.get(file)
driver.maximize_window()

driver.find_element_by_id("tooltip").click()

time.sleep(5)
# 关闭alert的弹框

# 第一步 得到了操作弹框的句柄
alert = driver.switch_to.alert
# 第二步 关闭弹框
alert.accept()

time.sleep(2)
driver.quit()
