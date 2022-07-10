
import os
# resuests モジュールをインポート
from operator import truediv
from bs4.builder import HTML
from openpyxl.xml.constants import ACTIVEX, XLSX
from openpyxl.styles import PatternFill
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.chrome.options import Options
import time
import random
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl

from selenium.webdriver.common.action_chains import ActionChains


'''
excellsetting
'''



#%%
"""
driversetting
"""
config_ini = configparser.ConfigParser()
base = os.path.dirname(os.path.abspath(__file__))
path = os.getcwd()
config_ini.read(path+'\\'+'Costco.ini', encoding='utf-8')
var2 = config_ini.get('DEFAULT', 'Driverpath')
options = Options()
user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
                  ]
options = webdriver.ChromeOptions()
options.add_argument('--user-agent=' + user_agent[random.randrange(0, len(user_agent), 1)])
driver = webdriver.Chromedriver = webdriver.Chrome(executable_path= var2 , chrome_options=options)
#%%
'''
URLを開く
'''
URL ="https://www.costco.co.jp/login"
time.sleep(2)
#URLを開く
driver.get(URL)


'''
login処理
'''
# ページ上のすべての要素が読み込まれるまで待機（15秒でタイムアウト判定）
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
#メールアドレスを記入
mail     = driver.find_element_by_xpath('//*[@id="j_username"]')
password = driver.find_element_by_xpath('//*[@id="j_password"]')
mail.clear()
password.clear()
mail.send_keys('tomoko.tomoko.0909@gmail.com')
password.send_keys('costco1qaz')
time.sleep(3)
xpath = '//*[@id="loginSubmit"]'
elem = driver.find_element_by_xpath(xpath)
elem.click()

time.sleep(30)

'''
2つめのタブを開く
'''
#time.sleep(60)
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)

# 新しいタブを作成する
driver.execute_script("window.open()")
# 新しいタブに切り替える
driver.switch_to.window(driver.window_handles[1])
# 新しいタブでURLアクセス
driver.get('https://www.costco.co.jp/my-account/orders')
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)

'''
soupに解析させる
'''
#カレントページを取得する
html =driver.page_source.encode('utf-8')
#読み込む情報を解析する。
soup = BeautifulSoup(html, 'html.parser') 
#指定のクラスを リストで取得する。
taglist = soup.select("[class*='order-history__list-item']")


'''
情報抽出
'''
for item in taglist:
    '''
    アイテム変数定義
    '''

    print(item)
