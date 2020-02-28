#嘿嘿嘿
import urllib.request
import os

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

##def get_page(self,url):
##
##    if 
##    html = url_open(url).decode('utf-8')
##    a = html.find('current-comment-page')+23
##    b = html.find(']',a)
##    return html[a:b]
def get_page_index():
    page_index = []
    
    lastOne=['5','4','3','2','1','0','z','y','x','w','=']
    for four in lastOne:
        third = ['k','g','c','Y','U','Q','M','I','E','A']
        if four == '=':
            
            for three in third:
                str = three + four
                second = ['z','j','T','D']
                
                for two in second:
                    str = two + str
                    first = ['N','M']
                    
                    for one in first:
                        str = one + str
                        page_index.append(str)
        else:
            third2 = ['U','Q','M','I','E','A']
            for three2 in third2:
                str = 'MT'+three2+four
                page_index.append(str)
                
    return page_index

def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')

    while a != -1:
        b = html.find('.jpg',a ,a+255)
        if b != -1:
            img_addrs.append('https:'+html[a+9:b+4]) # 'img src='为9个偏移  '.jpg'为4个偏移
        else:
            b = a+9
        a = html.find('img src=', b)

    return img_addrs


def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)
        print(img_addrs)

def download_mm(folder = 'xxoo', pages = 1):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'
##    page_num = get_page(url)
    
    page_num = get_page_index()
    
##    'MTQw'
    
    for i in page_num:
##        page_num -= i
        page_url = url + 'MjAyMDAyMDQt'+ i + '#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)



if __name__ == '__main__':
    download_mm()
