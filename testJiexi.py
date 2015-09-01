# -*- coding: utf-8 -*-
__author__ = 'vincentgong'

import json
import re

def jiexi(content):
    tmp = re.findall(r'pl\.content\.homeFeed\.index.*html\":\"(.*)\"}\)', content)
    # for tmp_r in tmp:
    # content = content.replace(tmp_r, 's')
    max = 0
    for i in tmp:
        if max < len(i):
            max = len(i)
            content = i
    content = content.replace('WB_detail', 'WB_detailWB_detail')
    # get all things
    WB_single = re.findall(r"WB\_detail(.+?)WB\_detail", content)
    # for i in range(0,len(WB_single)):
    # {'text': 微博信息内容, 'count': 转发数, 'wid': 微博ID, 'name': 微博作者的用户信息字段, 'uid': 用户UID,
    #  'nick': 用户昵称, 'self': u['self'], 'timestamp': 微博创建时间, 'source': 微博来源,
    #  'location': 用户所在地, 'country_code': u['country_code'],
    #  'province_code': 用户所在省级ID, 'city_code': 用户所在城市ID, 'geo': 地理信息字段,
    #  'emotionurl': u['emotionurl'], 'emotiontype': u['emotiontype']
    # })
    # {'text': u['text'], 'count': u['reposts_count'], 'wid': u['id'], 'name': u['user']['name'],
    #  'uid': u['user']['id'],
    #  'nick': u['user']['screen_name'], 'self': 'null', 'timestamp': u['created_at'], 'source': u['source'],
    #  'location': u['user']['location'], 'country_code': '',
    #  'province_code': u['user']['province'], 'city_code': u['user']['city'], 'geo': u['geo'],
    #  # 'emotionurl': u['emotionurl'], 'emotiontype': u['emotiontype']
    #  'link': u['user']['id']
    # })
    user = []
    for WB in WB_single:
        # print(' ')
        # print(WB)
        # print(' ')
        WB_text = ''.join(re.findall(r"WB\_text[^>]*>(.*?)<\\/div", WB)).replace('\\n', '').replace('\\"', '"').replace(
            '\\/', '/').strip()  #.lstrip('\\n').strip()
        # if WB_text inclued WB_media_expand is miniPage !!!!!!
        WB_geo = ''.join(re.findall(r"place.{13}?(.+).title", WB_text)).strip()
        if not '_' in WB_geo:
            WB_geo = WB_geo[1:]
        print(WB_geo)

        WB_geo_title = ''.join(re.findall(r"place.+title..?(.+)..href", WB_text)).strip()
        print(WB_geo_title)

        WB_source = ''.join(re.findall(r'WB\_text[^>]*>.*nofollow\\">(.*?)<', WB))  # checked

        WB_collect = 0
        WB_collect_tmp = re.findall(r'搜藏.*?(\d+)', WB)
        if len(WB_collect_tmp) >0:
            WB_collect = re.findall(r'搜藏.*?(\d+)', WB)[0]  # checked

        WB_comment = re.findall(r'评论.*?(\d+)', WB)[0]  # checked
        WB_forward = re.findall(r'转发.*?(\d+)', WB)[0]  # checked
        WB_like = ''.join(re.findall(r'WB\_text[^>]*>.*praised.*?\(([0-9]*)', WB))  # checked
        # WB_like = re.findall(r'W_icon.icon_praised_b."><..i> <em>(\d+)<..em>', WB)[0] # checked
        #print(WB_like)
        # WB_mid = ''.join(re.findall(r' mid=\\"([0-9]*)', WB))
        # WB_wid = re.findall(r'mid=(\d*).*?转发', WB)[-1] # checked
        WB_wid = re.findall(r'mid=.*?(\d*)', WB)[0]  # checked
        WB_name = ''.join(re.findall(r'nick-name=\\"([^"]*)\\"', WB))
        WB_uid = ''.join(re.findall(r'fuid=([^"]*)\\"', WB))  # checked
        WB_timestamp = re.findall(r'date=\\"([^"]*)\\"', WB)[0]  # checked
        user.append({'text': WB_text, 'collected_count': WB_collect, 'mid': WB_wid, 'name': WB_name,
                     'uid': WB_uid, 'nick': WB_name, 'self': 'dontknow', 'timestamp': WB_timestamp, 'source': WB_source,
                     'location': 'null', 'country_code': '', 'province_code': 'null', 'city_code': 'null',
                     'geo': WB_geo, 'geo_title': WB_geo_title,
                     'link': WB_uid, 'forward': WB_forward, 'like': WB_like, 'comment': WB_comment})
    return user



def writefile(self,filename,content):
    fw = file(filename,'w')
    fw.write(content)
    fw.close()

content = open('/Users/vincentgong/Documents/workspaces/Pyworks/weibo-master/output/5148876354/page1-source1.txt').read()
result = json.dumps(jiexi(content))
print result