import time
import hmac
from requests import Request, Session


ts = int(time.time() * 1000)
request = Request('GET', 'https://ftx.com/api/markets')
prepared = request.prepare()
signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode()
signature = hmac.new('YOUR_API_SECRET'.encode(), signature_payload, 'sha256').hexdigest()

request.headers['FTX-KEY'] = '8c77Ww0-nIy1dfbjShPAeAeTtN6S8TOy38j2btaO'
request.headers['FTX-SIGN'] = signature
request.headers['FTX-TS'] = str(ts)

#取得する
r = Session().send(prepared)
rJson = r.json()

#絞る
resultKey = 'result'

for ticker in rJson[resultKey]:
    if ticker['name'] == 'BTC/USD':
        print(ticker['ask'])
    if ticker['name'] == 'BTC/USD':
        print(ticker['bid'])
    if ticker['name'] == 'USD/JPY':
        print(ticker['ask'])
    if ticker['name'] == 'USD/JPY':
        print(ticker['bid'])
