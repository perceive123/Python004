from selenium import webdriver
from time import sleep

driver=webdriver.Chrome(r'D:\software\谷歌浏览器驱动\chromedriver_win32\chromedriver.exe')
driver.implicitly_wait(10)#设置等待元素出现的时间
driver.get('https://processon.com')
#点击登录
eles=driver.find_elements_by_class_name('nav-item')
eles[4].click()
#睡眠1秒
sleep(1)
#输入用户名
ele=driver.find_element_by_id('login_email')
ele.send_keys('******')
#输入密码
ele=driver.find_element_by_id('login_password')
ele.send_keys('******')
#点击立即登录
ele=driver.find_element_by_id('signin_btn')
ele.click()

# driver.close()

