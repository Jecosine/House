from urllib import urlopen
from bs4 import BeautifulSoup as bs
from Untitled import print_f
import requests
#from get_ip import get_pool

import time
import random
import math,os
records = 0
pool = []

url = "http://cq.esf.fang.com/house/i31"

header = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    'Referer':url
}


def fuck_data():
    global pool
    global records
    global url
    content = ""
    page = 31
    fileno = '1'
    url = "http://cq.esf.fang.com/house/i"+str(page+30)
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    #html = requests.get(url,headers = header)
    while True:
        if fileno>10:
            break
        if records > 10000:
            print "file %s start" % fileno
            fileno += 1
            records = 0
            f = open(fileno+'.html','wb')
            f.write(content)
            content = ""
            f.close()

        #html = requests.get(url,headers = header,proxies = pool[random.randrange(len(pool))])
        try:
            html = s.get(url,headers = header)
        except:
            page += 1
            save_process()
            continue
        else:
            if html.status_code <> 200:
                break
            bsobj = bs(html.text,'html.parser')
            content += deal_data_single(bsobj)
            page += 1
            save_process()
            time.sleep(1)
            url = "http://cq.esf.fang.com/house/i"+str(page+30)

def deal_data_single(bsobj):
    #get data each page
    global records
    links = bsobj.findAll('dl',{'class':"clearfix"})
    records += len(links)
    data = ""
    for link in links:
        data += str(link)+'\n\r\n'
        #print_f(records,1000)
    print records
    return data

def save_process():
    f = open("saved.txt",'wb')
    f.write(str(records))
    f.close()

def retrieve_data():
    if os.path.exists('saved.txt'):
        f = open("saved.txt",'rb')
        content = f.read()
        f.close()
        return int(content)
    else:
        return 1

#pool = get_pool()
random.seed(time.time())
fuck_data()
