from selenium import webdriver
from bs4 import BeautifulSoup as soups
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
from tqdm import tqdm
import socket

base_dir = 'C:\\Users\\AI\\OneDrive - 광운대학교\\crawl_img'

def crawlling_from_chrome(input_string, save_dir):

    driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

    elem = driver.find_element_by_name("q")

    elem.send_keys(input_string)
    elem.send_keys(Keys.RETURN)

    SCROLL_PAUSE_TIME = 2

    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height

    images = driver.find_elements_by_css_selector('.rg_i.Q4LuWd')
    count = 1
    time.sleep(3)
    for image in tqdm(images):
        try:
            if input_string == 'forest fire image' and count < 200:
                count += 1
                continue
            image.click()
            time.sleep(1)
            imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img').get_attribute('src')
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            socket.setdefaulttimeout(10)
            try:
                urllib.request.urlretrieve(imgUrl, os.path.join(save_directory + save_dir, time.strftime("%d_%H%M%S") + '_' + str(count) + ".jpg"))
            except:
                print('skip download cause timeout 10s')
                continue
            time.sleep(1)
            count += 1
        except:
            pass

save_directory = base_dir + '\\datasets\\fire\\'

driver = webdriver.Chrome()

# [][0]: keyword, [][1]: directory
search_keyword_list = [#('burning building photo', 'building'),
                       #('building on fire', 'building'),
                       #('burning car image', 'car'),
                       #('vehicle fire pictures', 'car'),
                       ('forest fire image', 'mountain')
                      ]


translate_language_list = ['', 'korean', 'japanese', 'chinese',
                           'spanish', 'german', 'russian',
                           'portugal', 'greek', 'italy',
                           'indonesia', 'french', 'vietnam',
                           'poland', 'thailand'
                           ]


for input in search_keyword_list:
    first_english = True
    for lang in translate_language_list:
        if first_english:
            result = input[0]
            first_english = False
        else:
            time.sleep(0.5)
            driver.get('https://www.google.com/search?q=translate+english+to+'+lang)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="tw-source-text-ta"]').send_keys(input[0])
            time.sleep(1)
            result = driver.find_element_by_xpath('//*[@id="tw-target-text"]/span').text
            time.sleep(1)
            print(input[0], ' -> ',  result, ' ('+lang+')')

        crawlling_from_chrome(result, input[1])






