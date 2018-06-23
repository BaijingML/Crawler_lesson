import time
from selenium import webdriver
import xlrd
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from PIL import Image
import pytesseract
from pyquery import PyQuery as pq
import requests
from requests.exceptions import RequestException
import os
import random
from aip import AipOcr

def data_read(original_data_path):
    data_workbook = xlrd.open_workbook(original_data_path)
    sheet_names = data_workbook.sheet_names()
    company_names = []
    for sheet_name in sheet_names:
        sheet = data_workbook.sheet_by_name(sheet_name)
        company_names.extend(sheet.col_values(0)[1:])
    return company_names


def check_character(check_str):
    '校验字符是否为汉字、数字、英文'
    for ch in check_str.decode('utf-8'):
        if (u'\u4e00' <= ch <= u'\u9fa5') & (u'\u0041' <= ch <= u'\u005a') & (u'\u0030' <= ch <= u'\u0039'):
            pass
        else:
            check_str.remove(ch)
    return check_str

def img_ocr(img_path):
    APP_ID = '11402252'
    API_KEY = 'U46QcVKl6CGv5h4VYYIqWPrT'
    SECRET_KEY = 'ym7LZhEnEerDS38vTKKpIO6s8hLWWgDW '
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    def get_file_content_gray(img_path):
        img = Image.open(img_path)
        img = img.convert('L')
        img.save(img_path.split('.')[0] + 'gray.jpg', 'jpeg')
        filePath = img_path.split('.')[0] + 'gray.jpg'
        with open(filePath, 'rb') as fp:
            return fp.read()
    def get_file_content_rgb(img_path):
        img = Image.open(img_path)
        img = img.convert('RGB')
        img.save(img_path.split('.')[0] + 'rgb.jpg', 'jpeg')
        filePath = img_path.split('.')[0] + 'rgb.jpg'
        with open(filePath, 'rb') as fp:
            return fp.read()

    image_gray = get_file_content_gray(img_path)
    img_info_gray = client.webImage(image_gray)
    image_rgb = get_file_content_rgb(img_path)
    img_info_rgb = client.webImage(image_rgb)
    print(img_info_gray['words_result'][0]['words'], img_info_rgb['words_result'][0]['words'])
    if len(img_info_gray['words_result'][0]['words']) >= len(img_info_rgb['words_result'][0]['words']):
        return img_info_gray['words_result'][0]['words']
    else:
        return img_info_rgb['words_result'][0]['words']
    #text = pytesseract.image_to_string(img)
    #if len(text) != 11 or len(text) !=


def data_write(data_dict, original_data_path, companies):
    df = pd.read_excel(original_data_path)
    for i, company_name in enumerate(companies):
        company_data = data_dict[company_name]
        for j, detail_str in enumerate(company_data):
            df.iloc[i, j + 1] = detail_str
    df.to_excel(original_data_path, index=False)


def set_search_url(name):
    if name:
       search_url = SEARCH_URL + name + '&final=1&jump=1'
       return search_url
    else:
        return None

def search_company(driver, url1):
    driver.get(url1)
    content = driver.page_source.encode('utf-8')
    doc = pq(content)
    time.sleep(3)
    url2 = doc('#list_con > li:nth-child(1) > div.item_con.job_comp > div > a').attr('href')
    driver.get(url2)
    comp_content = driver.page_source.encode('utf-8')
    comp_doc = pq(comp_content)
    time.sleep(3)
    driver.quit()
    return comp_doc

def download_img(url):
    response=requests.get(url)
    try:
        if response.status_code==200:
            return response.content
        return None
    except RequestException:
        return None

def save_image(content):
    path_name= 'D:/imgfile/' + str(random.randint(1, 5000000)) + '.gif'
    if not os.path.exists(path_name):
        with open(path_name,'wb') as f:
            f.write(content)
            f.close()
    return path_name

def comp_class1(driver, url):
    bs_info = {}
    driver.get(url)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    content = driver.page_source.encode('utf-8')
    doc = pq(content)
    bs_info['BS_PROP'] = doc('body > div.company_intro > div.wrap_intro > div.intro_down_wrap > div > table > tbody > tr:nth-child(2) > td.td_c2').text()
    bs_info['BS_AREA'] = doc('body > div.company_intro > div.wrap_intro > div.intro_down_wrap > div > table > tbody > tr.tr_l4 > td.td_c1').text()
    img_url = doc('body > div.company_intro > div.wrap_intro > div.intro_down_wrap > div > table > tbody > tr.tr_l4 > td.td_c3 > img').attr('src')
    content = download_img(img_url)
    img_path = save_image(content)
    bs_info['BS_CONTACT'] = img_ocr(img_path)
    bs_info['BS_ADDR'] = doc('body > div.company_intro > div.wrap_intro > div.intro_down_wrap > div > table > tbody > tr.tr_l6 > td.td_c1 > span').text()
    bs_info['BS_PERSON'] = doc('body > div.company_intro > div.wrap_intro > div.intro_down_wrap > div > table > tbody > tr:nth-child(2) > td.td_c3').text()
    bs_info['BS_CONTACT_PERSON'] = doc('body > div.company_intro > div.wrap_intro > div.intro_down_wrap > div > table > tbody > tr.tr_l4 > td.td_c2').text()
    browser.quit()
    print(bs_info)
    return bs_info

def comp_class2(driver, url):
    bs_info = {}
    driver.get(url)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    content = driver.page_source.encode('utf-8')
    doc = pq(content)
    bs_info['BS_PROP'] = doc('body > div.wb-main > div.wb-content > div.wrap > div.basicMsg > ul > li:nth-child(5)').text()
    bs_info['BS_AREA'] = doc('body > div.wb-main > div.wb-content > div.wrap > div.basicMsg > ul > li:nth-child(9) > div > a').text()
    bs_info['BS_ADDR'] = doc('body > div.wb-main > div.wb-content > div.wrap > div.basicMsg > ul > li.compony.cleafix > div > var').text()

    # 有些电话也是由图片展示的，所以这个地方需要改动

    bs_info['BS_CONTACT'] = doc('body > div.wb-main > div.wb-content > div.wrap > div.basicMsg > ul > li:nth-child(4) > span').text()
    bs_info['BS_WEB'] = doc('body > div.wb-main > div.wb-content > div.wrap > div.basicMsg > ul > li:nth-child(6) > a').attr('href')
    # 去掉那些官网就是58页面的公司网址
    if bs_info['BS_WEB'].split('/')[2] == 'qy.58.com':
        bs_info['BS_WEB'] = ''
    else:
        pass
    browser.quit()
    print(bs_info)
    return bs_info

def comp_class3(driver, url):
    bs_info = {}
    driver.get(url)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 滚动到底部
    time.sleep(2)
    content = driver.page_source.encode('utf-8')# 网页的全部html
    doc = pq(content)
    ul_content=doc('.mod-box').html()
    doc1=pq(ul_content).find('li').find('span')
    bs_info['BS_Name']=doc1.eq(0).text()
    bs_info['BS_CONTACT_PERSON']=doc1.eq(1).text()
    bs_info['BS_CONTACT']=[]
    bs_info['BS_CONTACT'].append(doc1.eq(4).text())
    bs_info['BS_CONTACT'].append(doc1.eq(5).text())
    bs_info['BS_QQ']=doc1.eq(6).text()
    bs_info['BS_ADDR'] = doc1.eq(7).text()
    browser.quit()
    print(bs_info)
    return bs_info


#def comp_sparser(comp_doc):



browser = webdriver.Chrome()
browser.set_page_load_timeout(30)

#url1 = set_search_url('四川凡科商务咨询有限公司')
#comp_doc = search_company(browser, url1)
#print(comp_doc)
#comp_dict = comp_sparser(comp_doc)
comp_info = comp_class1(browser,'http://qy.58.com/mq/44157128721943')
#comp_class2(browser, 'http://qy.58.com/55377397323790/?PGTID=0d302408-0006-61ee-8938-8363140f2728&ClickID=3')
#comp_class3(browser, 'http://t5838988073332240.5858.com/')
