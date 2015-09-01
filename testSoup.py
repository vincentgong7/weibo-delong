# -*- coding: utf-8 -*-
__author__ = 'vincentgong'
from bs4 import BeautifulSoup
import re


content = open('/Users/vincentgong/Documents/workspaces/Pyworks/weibo-master/page1-source1.txt').read()
# tmp = re.findall(r"[0-9]+<\\/strong><span class=\\.S_txt2\\.>微博", content);
tmp = re.findall(r"<!--feed内容-->.+<!--翻页-->", content);
if len(tmp)==1:
    text = tmp[0].replace('\\n','').replace('\\"','"').replace('\\/','/')
    itemList = []
    soup = BeautifulSoup(text)
    # <div  tbinfo="ouid=5148876354" action-type="feed_list_item" diss-data=""  mid="3845905055192972"  class="WB_cardwrap WB_feed_type S_bg2 ">
    itemList = soup.find_all("div", class_="WB_cardwrap WB_feed_type S_bg2 ")
    # print len(itemList)
    for item in itemList:
        WB = str(item)
        # mid_tmp = re.findall(r"mid=(\d+)", WB)
        # mid = mid_tmp[0][4:]
        # text = ''.join(re.findall(r"<div class=.WB_text[^>]*>(.*?)<.div>",WB)).strip()
        WB_text = ''.join(re.findall(r"WB\_text[^>]*>(.*?)</div", WB)).strip()
        # WB_source = ''.join(re.findall(r'WB\_text[^>]*>.*nofollow\\">(.*?)<', WB))  # checked
        WB_forward = re.findall(r'收藏.*?(\d+)', WB)[-1]  # checked
        WB_pinlun = re.findall(r'评论.*?(\d+)', WB)[-1]  # checked
        WB_count = re.findall(r'转发.*?(\d+)', WB)[-1]  # checked
        WB_like = ''.join(re.findall(r'WB\_text[^>]*>.*praised.*?\(([0-9]*)', WB))  # checked
        # WB_mid = ''.join(re.findall(r' mid=\\"([0-9]*)', WB))
        # WB_wid = re.findall(r'mid=(\d*).*?转发', WB)[-1] # checked
        WB_wid = re.findall(r'mid=.*?(\d*)', WB)[-1]  # checked
        WB_name = ''.join(re.findall(r'nick-name=\\"([^"]*)\\"', WB))
        WB_uid = ''.join(re.findall(r'fuid=([^"]*)\\"', WB))  # checked
        WB_timestamp = re.findall(r'date=\\"([^"]*)\\"', WB)[-1]  # checked
