#正则表达式
import urllib.request
import os
import re


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def get_img(html):
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
##    r'<img src="([^"]+\.jpg)"'
##    r'<img class="BDE_Image" src="([^"]+\.jpg)"'
    imglist = re.findall(p,html)
##    for each in imglist:
##        print(each)
##    for each in imglist:
##        filename = each.split('/')[-1]
##        urllib.request.urlretrieve(each,filename,None)
    print(imglist)
    return imglist

def save_imgs(folder, imglist):
    for each in imglist:
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)
        print(imglist)

def download_pic(folder = 'tiebaPic5'):
    os.mkdir(folder)
    os.chdir(folder)
    url = "http://tieba.baidu.com/p/6474836525"
##    "http://tieba.baidu.com/p/6468365167"
##    "http://tieba.baidu.com/f?ie=utf-8&kw=%E5%BC%A0%E5%AD%90%E6%9E%AB&fr=search"
    
    html = url_open(url).decode('utf-8')
    imglist = get_img(html)
    save_imgs(folder, imglist)


if __name__ == '__main__':
     download_pic()
