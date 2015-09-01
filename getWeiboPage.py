__author__ = 'vincentgong'

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import sys
import time
import Lweibo
import json
import os

reload(sys)
sys.setdefaultencoding('utf-8')

class getWeiboPage:



    def __init__(self,uid, uidURL, outputFolder):

        self.body = {
            '__rnd':'',
            '_k':'',
            '_t':'0',
            'count':'50',
            'end_id':'',
            'max_id':'',
            'page':1,
            'pagebar':'',
            'pre_page':0,
            'uid':''}

        # uid_list = []
        # charset = 'utf8'
        self.body['uid'] = uid
        self.outputFolder = outputFolder
        self.uidURL = uidURL

        if not os.path.isdir(outputFolder):
            os.makedirs(outputFolder)

    def get_firstpage(self):
        self.body['pre_page'] = self.body['page']-1
        url = self.get_url() + urllib.urlencode(self.body)
        print('URL 1:' + str(url))
        print ''
        req = urllib2.Request(url)
        result = urllib2.urlopen(req)
        text = result.read()
        self.writefile(self.outputFolder + '/page'+ str(self.body['page'])+'-source1.txt',text)
        self.writefile(self.outputFolder + '/page'+str(self.body['page'])+'-result1.txt',eval("u'''"+text+"'''"))
        self.writefile(self.outputFolder + '/page'+ str(self.body['page'])+'-json1.txt',json.dumps(Lweibo.jiexi(text)))
        return text

    def get_secondpage(self):
        self.body['count'] = '15'
    #   self.body['end_id'] = '3490160379905732'
    #   self.body['max_id'] = '3487344294660278'
        self.body['pagebar'] = '0'
        self.body['pre_page'] = self.body['page']

        url = self.get_url() +urllib.urlencode(self.body)
        print('URL 2:' + str(url))
        print ''
        req = urllib2.Request(url)
        result = urllib2.urlopen(req)
        text = result.read()
        # self.writefile(self.outputFolder + '/page'+str(self.body['page'])+'-source2.txt',text)
        # self.writefile(self.outputFolder + '/page'+str(self.body['page'])+'-result2.txt',eval("u'''"+text+"'''"))
        self.writefile(self.outputFolder + '/page'+ str(self.body['page'])+'-json2.txt',json.dumps(Lweibo.jiexi(text)))
        return text

    def get_thirdpage(self):
        self.body['count'] = '15'
        self.body['pagebar'] = '1'
        self.body['pre_page'] = self.body['page']

        url = self.get_url() +urllib.urlencode(self.body)
        print('URL 3:' + str(url))
        print ''
        req = urllib2.Request(url)
        result = urllib2.urlopen(req)
        text = result.read()
        # self.writefile(self.outputFolder + '/page'+str(self.body['page'])+'-source3.txt',text)
        # self.writefile(self.outputFolder + '/page'+ str(self.body['page'])+'-result3.txt',eval("u'''"+text+"'''"))
        self.writefile(self.outputFolder + '/page'+ str(self.body['page'])+'-json3.txt',json.dumps(Lweibo.jiexi(text)))
        return text

    def get_url(self):
        # for normal users
        url = 'http://weibo.com/' + self.body['uid'] + '?'

        # for gov users
        # url = 'http://www.weibo.com/p/' + self.body['uid'] + '/home?'

        #
        # url = 'http://weibo.com/' + uid + '?from=otherprofile&wvr=3.6&loc=tagweibo'

        # url = self.uidURL
        return url

    def get_uid(self,filename):
        fread = file(filename)
        for line in fread:
            getWeiboPage.uid_list.append(line)
            #print line
            time.sleep(1)

    def writefile(self,filename,content):
        fw = file(filename,'w')
        fw.write(content)
        fw.close()