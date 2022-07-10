from tkinter.tix import NoteBook
from tracemalloc import start
import pyautogui
import time
from tkinter import messagebox
import random
import sys
import signal
import re


###
# 変数を定義する
# fileName  　　 :　ファイルパス
# startMessageBox　: strart時のメッセージボックスのコメント
# endErrorMessageBox　: 処理を異常終了するコメント
# endInfoMessageBox　: 処理を正常終了するコメント
# endIOErrorMessageBox　: 処理を終了するコメント
# sep              : 区切り文字
# randomTime　　 : 120-130のランダムな時間
###

fileName = 'English.txt'
startMessageBox = '①処理を開始します。画面右下が「あ」から「A」になっていることを確認してください'+ '\r\n' + '②メッセージボックスにカーソルを合わせて「enter」を入力してください' + '\r\n' +  '実行時に「あ」にしていなかった場合「いいえ」を押してください'
endErrorMessageBox = '処理を終了します。「あ」にしてからもう一度実行してください'
endInfoMessageBox =  'ファイルをすべて読み込みました'
endIOErrorMessageBox = 'English.txtを閉じてから実行してください'
sep = '[.?]'



###処理
# 処理開始のアナウンスをする。
# 最初のメッセージではいを押した場合に処理開始
# 現在のポインタをクリックする。
# ファイルを開いてすべてのもじれつを取得する。###


#処理開始のアナウンスをする。
ret = messagebox.askyesno('処理開始',startMessageBox )
if ret == False:
    #いいえを押したときに処理を終了する。
    messagebox.showinfo('終了',endErrorMessageBox)
    sys.exit()


time.sleep(1)
#クリックする
pyautogui.click()
pyautogui.hotkey('hanja')


try:
    #ファイルを開く UTF-8 読み取り専用
    file = open(fileName, encoding="utf-8", mode="r")
except IOError:
    #例外発生時の処理
    print ('cannot open' + fileName)
    #いいえを押したときに処理を終了する。
    messagebox.showinfo('終了',endIOErrorMessageBox)
    sys.exit()

#「.」区切りで分割し全角空白は半角空白に置換してリストに格納
datalist = file.read()
splitedDatalist = re.split(sep,datalist)
#書き込みカウンター
i=0

print("処理を開始します")
print("中断 : pause")
print("強制終了 : ctrl + c を押してください")

#すべて要素分ループする
for data in splitedDatalist:
    #乱数の範囲 120秒から130のうちどれかが選出される
    randomTime = random.randint(3, 10)
    
    
    pyautogui.write(data)
    time.sleep(5)
    #書き込み件数をカウントアップ
    i += 1  
    time.sleep(1)
    pyautogui.press('enter')
    print(data+" を送信しました")
    print(str(i) +"件送信しました")
    print(str(randomTime)+ "秒後に送信します")
    time.sleep(randomTime)

#処理を終了する。
messagebox.showinfo('終了',endInfoMessageBox)