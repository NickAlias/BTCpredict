# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 11:35:29 2019

@author: whalter86
"""
import urllib.request 

#options = weboptions('Timeout', 60, 'ContentType', 'json');
#Range = 'compact';

API_Key='ZHTC3MH0FYL275ZQ';
function="DIGITAL_CURRENCY_DAILY"
symbol="BTC"
market="USD"
url = "https://www.alphavantage.co/query?function=" + function+"&symbol="+symbol+"&market="+market+"&apikey="+API_Key+"datatype=csv"
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')
#%%
print(type(text))
print(text)

#file_name="BTC_Kurs.csv"
#urllib.request.urlretrieve(url, file_name)