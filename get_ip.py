from urllib import urlopen
from bs4 import BeautifulSoup as bs
import requests

header = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

def getIP():
    requests.Timeout(5)
    url = "http://www.xicidaili.com/nn"
    html = requests.get(url,headers = header)
    bsobj = bs(html.text,'html.parser')
    table = bsobj.find('table',{'id':'ip_list'})
    iplist = table.findAll('tr')[1:]
    pool = []
    print len(iplist)
    for ip in iplist:
        addr = ip.findAll('td')[1].get_text()+':'+ip.findAll('td')[2].get_text()
        if ip.findAll('td')[5].get_text() == 'HTTPS':
            pool.append({'https':"https://"+addr})
        else:
            pool.append({'http':"http://"+addr})
        print pool[-1]
    return pool
    #test whether ip is usable
def testIP(iplist):
    realpool = []
    for ip in iplist:
        try:
            html = requests.get('http://www.ip138.com/',proxies = ip,headers = header,timeout = 5)
        except:
            print 'failed'
        else:
            if html.status_code == 200:
                print 'success'
                realpool.append(ip)
            
    print len(realpool)

testIP(getIP())