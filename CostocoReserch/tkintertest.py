from tkinter import *
from tkinter import ttk


if __name__ == '__main__':
    root = Tk()
    root.title('コストコ履歴調査')
    iconfile = 'sample.ico'
    root.iconbitmap(default=iconfile)
    root.geometry("600x350+500+300") 



    #検索ページ番号の指定
    frame1 = ttk.Frame(root, padding=16)
    label1 = ttk.Label(frame1, text='検索するページ数を指定してください')
    researchWord = StringVar()
    entry1 = ttk.Entry(frame1, textvariable=researchWord)
    frame1.pack()
    label1.pack()
    entry1.pack()

    #出力先ファイル名の指定
    frame2 = ttk.Frame(root, padding=16)
    label2 = ttk.Label(frame2, text='出力先のファイル名を指定してください'+ '\n' +'（ex:data.xlsx）')
    outputFile = StringVar()
    entry2 = ttk.Entry(frame2, textvariable=outputFile)
    frame2.pack()
    label2.pack()
    entry2.pack()

    #メールアドレス指定
    frame3 = ttk.Frame(root, padding=16)
    label3 = ttk.Label(frame3, text='mailAddress')
    mailAddress = StringVar()
    entry3 = ttk.Entry(frame3, textvariable=mailAddress)
    frame3.pack()
    label3.pack()
    entry3.pack()

    #Password指定
    frame4 = ttk.Frame(root, padding=16)
    label4 = ttk.Label(frame4, text='Password')
    password = StringVar()
    entry4 = ttk.Entry(frame4, textvariable=password)
    frame4.pack()
    label4.pack()
    entry4.pack()

    #ボタン設定
    button1 = ttk.Button(
        text='OK',
        command=lambda: print())
    button1.pack()

    # ウィンドウの表示開始
    root.mainloop()