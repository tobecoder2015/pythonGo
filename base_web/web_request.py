import requests
res=requests.get('http://inventwithpython.com/')
# print res.content
print res.status_code
print res.headers
print res.cookies
print res.encoding


res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
   print 'there was a problem :{}'.format(exc.message)


res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playfile=open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(10000):
    playfile.write(chunk)
playfile.close()