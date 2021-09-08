from bs4 import BeautifulSoup

import requests

htms_stocks_text = requests.get('https://www.google.com/search?q=stocks+with+option+list&rlz=1C1SQJL_enIN910IN910&oq=stocks+with+option+list&aqs=chrome..69i57j0i13j0i22i30j0i8i13i30l5j0i390l2.10338j0j15&sourceid=chrome&ie=UTF-8').text
soup = BeautifulSoup(htms_stocks_text,'lxml')
price = soup.find('body',class_="srp wf-b")
print(price)