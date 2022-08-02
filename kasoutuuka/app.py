import math
import platform
import re
import time
import csv
import datetime
import PySimpleGUI as sg
import requests
import smtplib, ssl
from email.mime.text import MIMEText
import playsound

sg.theme('Default1')

default_args = {
    'font': ('Helvetica', 30),
}

bitbank_ask = 0
bitbank_bid = 0
bitflyer_ask = 0
bitflyer_bid = 0


            
down = 0

window = sg.Window(title='BitCoin Watcher').Layout(
    [
        [
            sg.Frame(
                "業者別価格",
                [
                    [
                        sg.Frame(
                            "bitbank",
                            [
                                [
                                    sg.Text("bid", size=(4, 1), **default_args),
                                    sg.Text(bitbank_bid, size=(12, 1), background_color="#009fc6", key="_bitbank_bid_", **default_args),
                                    sg.Text("ask", size=(4, 1), **default_args),
                                    sg.Text(bitbank_ask, size=(12, 1), background_color="#db4d50", key="_bitbank_ask_", **default_args),
                                ]
                            ]
                        ),
                    ],
                    [
                        sg.Frame(
                            "bitFlyer",
                            [
                                [
                                    sg.Text("bid", size=(4, 1), **default_args),
                                    sg.Text(bitflyer_bid, size=(12, 1), background_color="#009fc6", key="_bitflyer_bid_", **default_args),
                                    sg.Text("ask", size=(4, 1), **default_args),
                                    sg.Text(bitflyer_ask, size=(12, 1), background_color="#db4d50", key="_bitflyer_ask_", **default_args),
                               
                                ]
                            ]
                        )
                    ]
                ]
            ),
        ]
    ]
)


while True:
    event, value = window.read(timeout=500, timeout_key='_timeout_')
    if event in '_timeout_':
        
        
        
        try:
            # ==================== 価格取得 ====================
            # bitbank
            bitbank = requests.get('https://public.bitbank.cc/btc_jpy/ticker')
            bitbank_ask = int(bitbank.json()['data']['sell'])
            bitbank_bid = int(bitbank.json()['data']['buy'])
            window["_bitbank_ask_"].update(bitbank_ask)
            window["_bitbank_bid_"].update(bitbank_bid)

            # bitFlyer
            bitflyer = requests.get('https://api.bitflyer.com/v1/ticker?product_code=BTC_JPY')
            bitflyer_ask = int(bitflyer.json()['best_ask'])
            bitflyer_bid = int(bitflyer.json()['best_bid'])
            window["_bitflyer_ask_"].update(bitflyer_ask)
            window["_bitflyer_bid_"].update(bitflyer_bid)

          



        except Exception as e:
            print(e)

   