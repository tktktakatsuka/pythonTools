import datetime

import re


'''
content = "【SALE】1543"
pattern = '【.*】'
result = print(re.search(pattern, str(content)))
'''

time_now = datetime.datetime.now()
year = time_now.strftime("%Y")
month = time_now.strftime("%m").lstrip("0")
day = time_now.strftime("%d").lstrip("0")
date_without_0 = year + "/" + month + "/" + day
print (month)



'''


subtraction =int(executeMonth) - int(arrivalMonth)

if(subtraction <= -9):
    #9か月以上離れていた時
    print (str(subtraction) + "時間差分があります。")
    
    
'''

