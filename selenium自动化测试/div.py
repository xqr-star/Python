from selenium import webdriver
import time
import os

# 搜索一个单词是否在html原生代码中存在 ctrl+f
# 获取浏览器的驱动
driver = webdriver.Chrome()
file = "file:///" + os.path.abspath("E:\BIT—比特\测试\selenium2html/modal.html")
driver.get(file)
driver.maximize_window()

# 定位点击的链接
div1 = driver.find_element_by_class_name("span6")
div1.find_element_by_tag_name("a").click()
# div1.find_element_by_id("show_modal").click()
time.sleep(2)

div2 = div1.find_element_by_class_name("modal-body")
div2.find_element_by_link_text("click me").click()
time.sleep(2)

div3 = div1.find_element_by_class_name("modal-footer")

# 或者是定位到所有的button元素 然后使用数组的方式
buttons = div3.find_elements_by_tag_name("button")
buttons[0].click()
# div3.find_element_by_class_name("btn").click()




# # 这样的写法其实还是在主页面上找没有进入到div里面
# driver.find_element_by_class_name("modal-body").click()
# time.sleep(2)
# driver.find_element_by_class_name()
#
# # 定位到div 然后点击button按钮
# div = driver.find_element_by_class_name("modal-footer")
# div.find_element_by_class_name("btn").click()




time.sleep(2)
driver.quit()

