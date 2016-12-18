import requests,bs4
res=requests.get('http://www.baidu.com')
res.raise_for_status()
nostarchSoup=bs4.BeautifulSoup(res.text)
print type(nostarchSoup)
print res.text

elems=nostarchSoup.select('#head')
elems2=nostarchSoup.select('#wrapper')
kw=nostarchSoup.select('#kw')
print kw
print kw[0].attrs
print len(kw)