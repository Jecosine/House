from urllib import urlopen
from bs4 import BeautifulSoup as bs
import requests

import time
import math
records = 0
def print_f(count):
    rate =(count//1000 == 0) and 1 or count//1000
    print "|"+rate*'>'+(10-rate)*'-'+'|  ' + str(count) + "\b"*(14+int(math.log(count,10)+1)),
def fuck_data():
    global records
    content = ""
    page = 31
    url = "http://cq.zu.fang.com/house/i"+str(page)+"-s31/"
    html = requests.get(url)
    while html.status_code == 200:
        bsobj = bs(html.text,'html.parser')
        content += deal_data_single(bsobj)
        page += 1
        time.sleep(0.5)
        html = requests.get(url)
    print page,html.status_code
    f = open('a.html','wb')
    f.write(content)
    f.close()
        

def deal_data_single(bsobj):
    #get data each page
    global records
    links = bsobj.findAll('dl',{'class':"list hiddenMap rel"})
    records += len(links)
    data = ""
    for link in links:
        data += str(link)+'\n\r\n'
        print_f(records)
    return data

fuck_data()