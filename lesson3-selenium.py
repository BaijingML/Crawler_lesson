import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.set_page_load_timeout(30)

# 有多少页商品

browser.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=1&s=1&click=0')

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
page_info = browser.find_element_by_css_selector('#J_topPage > span > i')
print(type(page_info))
print(page_info.text)
