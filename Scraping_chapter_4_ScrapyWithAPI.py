from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import json
import re

random.seed(datetime.datetime.now())
anonuserlinkIP = [ ]
InternalLinks = [ ]
InvalidLinks=[]

def getInternalLinks(bsObj):
    for link in bsObj.findAll('a',href=re.compile('^(/wiki/)((?!:).)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in InternalLinks:
                InternalLinks.append(link.attrs['href'])
    return InternalLinks

def getCountry(ip):
    ipCountry='http://freegeoip.net/json/'+ip
    response=urlopen(ipCountry).read().decode('utf-8')
    responseJson=json.loads(response)
    return responseJson.get("country_name")



#这一部分，包含了getCity函数
def getIp(Title):
    newTitle=Title.replace('/wiki/','')
    IPurl='https://en.wikipedia.org/w/index.php?title='+newTitle+'&action=history'
    IPhtml=urlopen(IPurl)
    IPbsObj=BeautifulSoup(IPhtml,'html.parser')
    for ip in IPbsObj.findAll('a',{'class':'mw-userlink mw-anonuserlink'}):
        if ip.get_text() not in anonuserlinkIP:
            anonuserlinkIP.append(ip.get_text())
            Country = getCountry ( ip.get_text() )
            print ( '-----------' )
            print ( ip.get_text() + '  is from  ' + Country )
            print(datetime.datetime.now())
    return anonuserlinkIP


newurl='/wiki/Mao_Zedong'

while len(newurl)>0:
    if newurl not in InvalidLinks:
        InvalidLinks.append(newurl)
        html=urlopen('https://en.wikipedia.org'+newurl)
        bsObj=BeautifulSoup(html,'html.parser')
        links=getInternalLinks(bsObj)
        newurl = links[random.randint(0,len(links)-1)]
        for link in links:
            getIp(link)
    else:
        newurl = links[random.randint(0,len(links)-1)]






