# 层级的定位  下拉列表
# 为什么我的整个网页没有显示的效果??？
from selenium import webdriver
import time
import os
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
# / \  正则表达式
file = "file:///" + os.path.abspath("E:\BIT—比特\测试\selenium2html\level_locate.html")
driver.get(file)
driver.maximize_window()

driver.find_element_by_link_text("Link1").click()
# 定位下拉列表特定的元素 把鼠标放到整个元素让元素高亮展示
# 先定位到ul 在定位 anoter
ele = driver.find_element_by_id("dropdown1").find_element_by_link_text("Another action")

ActionChains(driver).move_to_element(ele).perform()

time.sleep(3)

driver.quit()