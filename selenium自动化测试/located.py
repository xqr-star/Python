# 元素的定位的学习
# 一个元素有很多的属性，可以根据这些不同的属性来学习

# 导入驱动包

from selenium import webdriver
# from datetime import time
import time

# 获取驱动 定义了变量 但是变量没有具体的类型
driver = webdriver.Chrome()
url = "https://www.baidu.com/"
driver.get(url) # 打开浏览器

# 用id 来定位百度搜索框 id是全局唯一 所以在同一个页面里面不可能都相同的id元素
# driver.find_element_by_id("kw").send_keys("高飞")
# 定位百度一下这个按钮 用id定位
# driver.find_element_by_id("su").click()
# 使用前提必须保证class是全局唯一的
# driver.find_element_by_class_name("btn self-btn bg s_btn btn_h btnhover").click()



# 使用link-text定位 没有 id name
# driver.find_element_by_link_text("新闻").click()

# 使用 partial-link_text 来定位元素
# driver.find_element_by_partial_link_text("hao").click()

# 使用tag_name定位  必须保证全局唯一
# driver.find_element_by_tag_name("input").send_keys("高飞")
# driver.find_element_by_tag_name("input").click()

# 使用xpath 来定位 xpath里面双引号的内容替换为单引号即可
# 如果没有显示的展现出来id name 等等的属性 那么可以xpath 确定xml语言文档中某部分的位置
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("解淇茹")
# driver.find_element_by_xpath("//*[@id='su'']").click()


# 用css selector来定位
# driver.find_element_by_css_selector("#kw").send_keys("BAT")
# driver.find_element_by_css_selector("#su").click()
# time.sleep(6)

# 清除输入框的内容 clear
# driver.find_element_by_css_selector("#kw").clear()
# driver.find_element_by_css_selector("#kw").send_keys("觉醒年代")
# driver.find_element_by_css_selector("#su").click()

# sumbit 提交  如果元素的type是submit 那么可以使用submit代替click来做
# driver.find_element_by_css_selector("#su").submit()

# text获取文本内容
text = driver.find_element_by_id("s-top-left").text
print(text)

# 等待反应
time.sleep(5) # 固定等待的时间



# 关闭浏览器
driver.quit()    #在关闭浏览器的同时清理一些缓存和一些无效的数据
# driver.close()   #仅仅是关闭浏览器的框框


