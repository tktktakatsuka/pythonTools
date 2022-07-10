
# resuests モジュールをインポート
from ast import IsNot
from contextlib import nullcontext
from operator import truediv
import re
from bs4.builder import HTML
import openpyxl
from openpyxl.xml.constants import ACTIVEX, XLSX
from openpyxl.styles import PatternFill
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.chrome.options import Options
import time
import datetime
from selenium.webdriver.common.action_chains import ActionChains
import chromedriver_binary


"""変数を宣言する
#inputWb        : 取得するExcelブックを入力
#inputWs        : 取得するExcelシートを入力
#yoko       : 取得する値のセルを入力
#driverPath : クロムドライバーの格納先を入力  
#yoko       : 検索ワードの読み取り列を入力"""


driverPath = "C:\python\work\shopInfo/chromedriver.exe"
for num in range(1 , 100):#num　+ 1
    """#変数を宣言する
    #resercWord : google検索ワード
    #options    : 画面を見せないときに使う機能
    #URL最初のブラウザ画面"""
 


    options = Options()
    options.add_argument('--headless')
    URL ="https://fortnite-movie-matome.jp/index.html"

    driver = webdriver.Chromedriver = webdriver.Chrome(chrome_options=options,executable_path= driverPath)
    driver.get(URL)  
    driver.maximize_window()
    time.sleep(5)
    driver.close()
