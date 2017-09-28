# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 21:09:41 2017

@author: Administrator
"""

import urllib2
from urllib2 import urlopen
from urllib2 import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import time
import random
import csv
import io
import math


CountNo = 0             #存储抓取网页的个数
pageBreakNo = 200       #每多少页存储在一个文件里


#------------------------------------------------------------------------------
# Function findStr(startStr, orgStr, endStr)
# 查找在orgStr中，startStr与endStr之间的字符串
# Input：
#   startStr --- 起始字符串
#   orgStr   --- 被搜索的字符串
#   endStr   --- 结束字符串
# Return：
#   rtnStr   --- 返回在orgStr中，startStr与endStr之间的字符串
#------------------------------------------------------------------------------
def findStr(startStr, orgStr, endStr):
#    print startStr
#    print endStr
    startLoc = orgStr.find(startStr.encode('utf-8')) + len(startStr.encode('utf-8'))
    endLoc = orgStr.find(endStr.encode('utf-8'), startLoc)
#    print (startLoc, endLoc)
    if startLoc != -1 and endLoc != -1:
        rtnStr = orgStr[startLoc:endLoc].strip()
    else:
        rtnStr = ''
    return rtnStr

#------------------------------------------------------------------------------
def handleLinks(pageUrl):
    global CountNo
    
    try:
        html = urlopen("http://sh.lianjia.com"+pageUrl) 
    except urllib2.URLError, e:
        print("Url Error!!!!\n")
        time.sleep(60)
        return ['']
    else:    
        bsObj = BeautifulSoup(html)
        
        price = bsObj.find("div", {"class":"price"})
        price = findStr(u'<div class=\"mainInfo bold\">', str(price), u'<span')
        
        introContent = bsObj.find("div", {"class":"introContent"})
        room = findStr(u'房屋户型：</span>', str(introContent), u'</li>')
        area = findStr(u'建筑面积：</span>', str(introContent), u'平</li>')    
        floor = findStr(u'所在楼层：</span>', str(introContent), u'</li>')
        orientation = findStr(u'朝向：</span>', str(introContent), u'</li>') 
        elavatorRate = findStr(u'梯户比例：</span>', str(introContent), u'</li>')   
        decorate = findStr(u'装修情况：</span>', str(introContent), u'</li>')  
        roomType = findStr(u'房屋类型：</span>', str(introContent), u'</li>') 
        if u'商住'.encode('utf-8') != roomType:
            duration = findStr(u'房本年限：</span>', str(introContent), u'</li>') 
        else:
            duration = '---'
            
        aroundInfo = bsObj.find("table", {"class":"aroundInfo "})
        buildDate = findStr(u'>年代：</span>', str(aroundInfo), u'</td>')  
        residence = findStr(u'html">', str(aroundInfo), u'</a>')
        indexNo = findStr(u'房源编号：', str(aroundInfo), u'</span>')
        
        aroundjs_content = bsObj.find("div", {"class":"around js_content"})   
        if None == aroundjs_content:
            longitude=''
            latitude=''
        else:
            longitude = aroundjs_content["longitude"]
            latitude = aroundjs_content["latitude"]

        CountNo = CountNo + 1
        print str(CountNo) + " " + indexNo
    #    print price + ' '+ room + 's ' + area + ' ' + floor + ' ' + orientation + ' ' + elavatorRate + ' ' + decorate + ' ' + roomType + ' ' + duration + ' ' + buildDate + ' ' + residence + ' ' + longitude + ' ' + latitude
        return [indexNo, price, room, area, floor, orientation, elavatorRate, decorate, roomType, duration, buildDate, residence, longitude, latitude]
#------------------------------------------------------------------------------
    
#------------------------------------------------------------------------------
html = urlopen("http://sh.lianjia.com/ershoufang/") 
bsObj = BeautifulSoup(html)
nameList = bsObj.findAll("strong")   
maxCount = int(math.ceil(int(nameList[1].get_text())/20)) + 1
#------------------------------------------------------------------------------    

fileName = str(time.strftime('%Y%m%d',time.localtime(time.time())))

#------------------------------------------------------------------------------
for i in range(1, (maxCount + 1)):
    pages = set()
    fileNo = int(math.ceil(i/pageBreakNo))
    FILE_BOJECT = open("%s_%.0f.csv" % (fileName, fileNo), "ab")
    writer=csv.writer(FILE_BOJECT)   
    html = None
    print "File: %s_%.0f.csv, TotalPage: %d, PageNo: %d" % (fileName, fileNo, maxCount, i)
    try:
        html = urlopen("http://sh.lianjia.com/ershoufang/d"+str(i), timeout=5) 
    except urllib2.URLError, e:
        print("Url Error!!!!\n")
        time.sleep(60)
    else:
        bsObj = BeautifulSoup(html)
        
        nameList = bsObj.findAll("strong")   
        maxCount = int(math.ceil(int(nameList[1].get_text())/20)) + 1
        
    
        linkList = bsObj.findAll(href=re.compile("\/ershoufang\/sh[0-9]+\.html"))
        for link in linkList:
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                    #我们遇到了新页面
                    newPage = link.attrs['href']        
                    estateContent = handleLinks(newPage)
                    pages.add(newPage)
                    writer.writerow(estateContent)
    #                print newPage
        FILE_BOJECT.close() 
        time.sleep(1)
#------------------------------------------------------------------------------    




