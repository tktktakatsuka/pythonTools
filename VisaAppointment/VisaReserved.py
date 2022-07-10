import re
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
import lxml.html
import logging
import random
import pyautogui

import sys
import os
from PIL import Image
import pyocr
import pyocr.builders
from plyer import notification



"""変数を宣言する
#inputWb        : 取得するExcelブックを入力
#inputWs        : 取得するExcelシートを入力
#yoko       : 取得する値のセルを入力
#driverPath : クロムドライバーの格納先を入力  
#yoko       : 検索ワードの読み取り列を入力"""


driverPath = "C:\\python\work\\VisaAppointment\\chromedriver.exe"
browserPath = "https://ie.ambafrance.org/How-to-book-an-appointment-How-to-cancel-my-appointment"
options = Options()
user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
                  ]
options = webdriver.ChromeOptions()
options.add_argument('--user-agent=' + user_agent[random.randrange(0, len(user_agent), 1)])
#options.add_argument('--headless')

for num in range(5):
    driver = webdriver.Chromedriver = webdriver.Chrome(executable_path= driverPath , chrome_options=options)
    driver.get(browserPath)
    driver.maximize_window()

    time.sleep(2)
    #クッキーが出たらクリックする。
    xpath= '//*[@id="tarteaucitronPersonalize2"]'
    if xpath is None:
        pass
    else:
        elem_login_btn = driver.find_element_by_xpath(xpath)
        elem_login_btn.click()
        time.sleep(5)


    #ONLINE BOOKING SYSTEMをクリックする
    xpath= '//*[@id="main"]/div/div[2]/div[3]/center[2]/div/strong/strong/a'
    elem_login_btn = driver.find_element_by_xpath(xpath)
    elem_login_btn.click()
    time.sleep(5)


    #全てのウィンドウハンドルを取得
    allHandles = driver.window_handles
    driver.switch_to.window(allHandles[1])

    #①Booking an appointmentをクリックする
    driver.execute_script("javascript:parent.parent.ComposantMenuFrameset.SelectItem2Menu1(0,0,false)")
    time.sleep(3)   

    waitTime = 1
    # (100, 200)の位置にマウスカーソルを移動
    pyautogui.moveTo(900,500)
    # クリック
    time.sleep(waitTime)
    pyautogui.click()
    time.sleep(waitTime)
    pyautogui.press("tab")
    time.sleep(waitTime)
    pyautogui.press("space")
    time.sleep(waitTime)
    pyautogui.press("tab")
    time.sleep(waitTime)
    pyautogui.press("tab")
    time.sleep(waitTime)
    pyautogui.press("enter")
    time.sleep(waitTime)

    #画像取得
    pyautogui.keyDown('alt')
    pyautogui.keyDown('printscreen')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('printscreen')
    time.sleep(waitTime)
    pyautogui.press("enter")
    time.sleep(waitTime)
    time.sleep(waitTime)

    #切断
    driver.quit
    time.sleep(waitTime)


    #実行プログラム選択画面
    pyautogui.keyDown('winleft')
    pyautogui.keyDown('r')
    pyautogui.keyUp('winleft')
    pyautogui.keyUp('r')
    time.sleep(waitTime)

    #enter
    pyautogui.typewrite('mspaint')
    pyautogui.press("enter")
    time.sleep(waitTime)

    #貼り付け
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('v')
    time.sleep(waitTime)

    #保存
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('s')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('s')
    time.sleep(waitTime)

    #ファイル名書込み
    pyautogui.typewrite('test.png')
    time.sleep(waitTime)
    pyautogui.press("enter")
    time.sleep(waitTime)
    pyautogui.press("tab")
    time.sleep(waitTime)
    pyautogui.press("enter")
    time.sleep(waitTime)

    #ペイント終了
    pyautogui.keyDown('alt')
    time.sleep(waitTime)
    pyautogui.keyDown('f4')
    pyautogui.keyUp('alt')
    time.sleep(waitTime)
    pyautogui.keyUp('f4')
    time.sleep(waitTime)

    TESSERACT_PATH = 'C:\\python\work\\VisaAppointment\\Tesseract-OCR'
    TESSDATA_PATH = 'C:\\python\work\\VisaAppointment\\Tesseract-OCR\\tessdata'

    os.environ["PATH"] += os.pathsep + TESSERACT_PATH
    os.environ["TESSDATA_PREFIX"] = TESSDATA_PATH

    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    # The tools are returned in the recommended order of usage
    tool = tools[0]
    print("Will use tool '%s'" % (tool.get_name()))
    # Ex: Will use tool 'libtesseract'
    langs = tool.get_available_languages()
    print("Available languages: %s" % ", ".join(langs))
    lang = langs[0]
    print("Will use lang '%s'" % (lang))

    fname = "test.png"
    txt = tool.image_to_string(
        Image.open("C:\\python\work\\VisaAppointment\\test.png"),
        lang="eng",
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )
    print( txt )



    #通知処理
    if "We are currently at full capacity. Please try again later" in txt:
        notification.notify(
        title="Pythonで通知",
        message="ここにメッセージを書きます",
        app_name="アプリの名前",
        app_icon="C:\\python\\work\\VisaAppointment\\ReserveOK.ico",
        timeout=3
    )


