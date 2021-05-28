# 多层框架和窗口的定位
from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
file = "file:///" + os.path.abspath("E:\BIT—比特\测试\selenium2html\\frame.html")
driver.get(file)
driver.maximize_window()

# 想要做到的事情是在 内层的frame里面进行文本搜索
# 整个页面的布局是 html 里面嵌套 iframe 在嵌套html 里面再iframe


# 但是首先需要切换到内层的页面 最外面的页面是没有百度搜索输入框的
# 切换层级  由于是一层套一层的
driver.switch_to.frame("f1")
driver.switch_to.frame("f2")
# 最简单的做法  由于不管前端的框架是如何做到一层层的套 id是不会改变的
driver.find_element_by_id("kw").send_keys("张杰")
driver.find_element_by_id("su").submit()

time.sleep(2)
# 定位到网页写的click的弹出框 可以发现click是在f1中的
# 那么是否可以再次又内存跳到外层来定位呢？ -- 不可以
# 只能回到默认的页面去定位 再去定位到f1
driver.switch_to.default_content()
driver.switch_to.frame("f1")
driver.find_element_by_link_text("click").click()
# 如果出现了alert弹出框那么说明定位成功了


time.sleep(2)
driver.quit()
