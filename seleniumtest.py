# from selenium import webdriver
# browser  =webdriver.Chrome()
# type(browser)
# browser.get('http://www.baidu.com')

#带有类名bookcover 的元素，tag_name属性将它的标签名打印出来
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('http://inventwithpython.com')
# try:
#     elem = browser.find_element_by_class_name('bookcover')
#     print('Found <%s> element with that class name!' % (elem.tag_name))
# except:
#     print('Was not able to find an element with that name.')

# 点击页面 click()
# from selenium import webdriver

# browser = webdriver.Chrome()

# browser.get('http:///inventwithpython.com')

# linkEleme = browser.find_element_by_link_text('Read It Online')
# type(linkEleme)
# linkEleme.click()

#submit()方法调用，send_keys()方法
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com')
# emailElem = browser.find_element_by_id('Email')
# emailElem.send_keys('not_my_real_email@gmail.com')
# passwordElem = browser.find_elemen_by_id('password')
# passwordElem.send_keys('12345')
# passwordElem.submit()

#  selenium模块，针对不能用字符串值输入的键盘击键 selenium.webdriver.common.keys

#