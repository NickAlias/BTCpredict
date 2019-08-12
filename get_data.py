# -*- coding: utf-8 -*-
import urllib.request 


API_Key='ZHTC3MH0FYL275ZQ';
function="DIGITAL_CURRENCY_DAILY"
symbol="BTC"
market="USD"
url = "https://www.alphavantage.co/query?function=" + function+"&symbol="+symbol+"&market="+market+"&apikey="+API_Key+"datatype=csv"
file_name="BTC_Kurs.csv"
urllib.request.urlretrieve(url, file_name)