from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
from PIL import Image
import pytesseract
from pyquery import PyQuery as pq
import requests
from requests.exceptions import RequestException
import os
import random

def download_img(url):
    response=requests.get(url)
    try:
        if response.status_code==200:
            return response.content
        return None
    except RequestException:
        return None

def save_image(content):
    path_name= 'D:/imgfile/' + str(random.randint(1, 5000000)) + '.jpg'
    if not os.path.exists(path_name):
        with open(path_name,'wb') as f:
            f.write(content)
            f.close()
    return path_name

def img_ocr(img_path):
    img = Image.open(img_path)
    text = pytesseract.image_to_string(img)
    return text

def comp_class1(driver, url):
    bs_info = {}
    driver.get(url)
    content = driver.page_source.encode('utf-8')
    doc = pq(content)
    bs_info['BS_PROP'] = doc('body > div.company_intro > div.wrap_intro > div.intro_down_wrap > div > table > tbody > tr:nth-child(2) > td.td_c2').text()
    bs_info['BS_AREA'] = doc('body > div.company_intro > div.wrap_intro > div.intro_down_wrap > div > table > tbody > tr.tr_l4 > td.td_c1').text()
    img_url = doc('body > div.company_intro > div.wrap_intro > div.intro_down_wrap > div > table > tbody > tr.tr_l4 > td.td_c3 > img').attr('src')
    content = download_img(img_url)
    img_path = save_image(content)
    bs_info['BS_CONTACT'] = img_ocr(img_path)
    bs_info['BS_ADDR'] = doc('body > div.company_intro > div.wrap_intro > div.intro_down_wrap > div > table > tbody > tr.tr_l6 > td.td_c1 > span').text()
    print(bs_info)


def comp_class2(driver, url):
    bs_info = {}
    driver.get(url)
    content = driver.page_source.encode('utf-8')
    doc = pq(content)
    bs_info['BS_PROP'] = doc('body > div.wb-main > div.wb-content > div.wrap > div.basicMsg > ul > li:nth-child(5)').text()
    bs_info['BS_AREA'] = doc('body > div.wb-main > div.wb-content > div.wrap > div.basicMsg > ul > li:nth-child(9) > div > a').text()
    bs_info['BS_ADDR'] = doc('body > div.wb-main > div.wb-content > div.wrap > div.basicMsg > ul > li.compony.cleafix > div > var').text()
    bs_info['BS_CONTACT'] = doc('body > div.wb-main > div.wb-content > div.wrap > div.basicMsg > ul > li:nth-child(4) > span').text()
    bs_info['BS_WEB'] = doc('body > div.wb-main > div.wb-content > div.wrap > div.basicMsg > ul > li:nth-child(6) > a').attr('href')
    # 去掉那些官网就是58页面的公司网址
    if bs_info['BS_WEB'].split('/')[2] == 'qy.58.com':
        bs_info['BS_WEB'] = ''
    else:
        pass
    print(bs_info)

browser = webdriver.Chrome()
browser.set_page_load_timeout(30)
comp_class2(browser, 'http://qy.58.com/55377397323790/?PGTID=0d302408-0006-61ee-8938-8363140f2728&ClickID=3')