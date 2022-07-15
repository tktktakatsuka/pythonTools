from tkinter import *
from tkinter import ttk

root = Tk()
root.title('My First App')

# ウィジェットの作成
frame1 = ttk.Frame(root, padding=16)
label1 = ttk.Label(frame1, text='検索キーワードを設定してください')
t1 = StringVar()
entry1 = ttk.Entry(frame1, textvariable=t1)

frame2 = ttk.Frame(root, padding=16)
label2 = ttk.Label(frame1, text='出力先のフォルダパスを指定してください（.xlsx）')
t2 = StringVar()
entry2 = ttk.Entry(frame1, textvariable=t2)


button1 = ttk.Button(
    frame1,
    text='OK',
    command=lambda: print('Hello, %s.' % t.get()))

# レイアウト
frame1.pack()
label1.pack()
entry1.pack()


# レイアウト
frame2.pack()
label2.pack()
entry2.pack()

button1.pack()


# ウィンドウの表示開始
root.mainloop()