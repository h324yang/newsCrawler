import requests
from pyquery import PyQuery as pq
token = "http://news.ltn.com.tw/list/focus"
postData = {"page": 1}
res = requests.post(token, data=postData)
q = pq(res.text)
links = [link.attr('href') for link in q('#newslistul li a').items()]

news = requests.get('http://news.ltn.com.tw'+links[0])
news = pq(news.text)
title = news('title').text()
content = news('div.text p').text()
posttime = news('div.text span').text()
print title,'\n',posttime,'\n',content