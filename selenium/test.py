import urllib;
import re;

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    print  html
    reg = r'src="(.+?\.png)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    print imglist
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.png' % x)
        x+=1


html = getHtml("http://huaban.com/search/?q=%E7%89%9B%E4%BB%94%E8%A3%A4&category=beauty")

print getImg(html);