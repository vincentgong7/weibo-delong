#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2013
# Gmail:liuzheng712
#
from getWeiboPage import getWeiboPage
import timeit
import Lweibo
import urllib2
from Celestine import Celestine
import time
import os
import sys

uid_list = []
number_of_pages_to_crawl = -1
start_crawl_uid = ''
interval = 3

def apiExample():
    # API 参考 http://open.weibo.com/wiki/%E5%BE%AE%E5%8D%9AAPI
    # 使用参考 https://github.com/lxyu/weibo
    api = Lweibo.useAPI()
    print api.get('statuses/user_timeline')
    print api.post('statuses/update', status='test from my api')

def simuLogin():
    # 模拟登陆的功能扩展待完善
    simu = Lweibo.simu()

    print(len(uid_list))

    getAllWeibo(uid_list,'output/')
    # print simu.detail('http://weibo.com/kaifulee')

def getAllWeibo(uidList, outputFolder):
    celia = Celestine(uidList, outputFolder, number_of_pages_to_crawl, interval)
    celia.start()

def get_uid(filename, start_uid = ''):
    start_uid_read = False
    fread = file(filename)
    for line in fread:
        line = line.rstrip('\n')
        if start_uid != '' and start_uid_read is False:
            if start_uid != line:
                continue
            else:
                start_uid_read = True
                uid_list.append(line)
                print line
        else:
            uid_list.append(line)
            print line

if __name__ == '__main__':
    #apiExample()
    start = timeit.default_timer()

    #python crawler.py number_of_pages_to_crawl start_crawl_uid interval
    number_of_pages_to_crawl = 1
    start_crawl_uid = ''
    interval = 1

    if len(sys.argv) == 4:
        number_of_pages_to_crawl = int(sys.argv[1])
        start_crawl_uid = sys.argv[2]
        interval = int(sys.argv[3])

    # uid file or specify the uid
    # uid_list = ['hngsjc,http://www.weibo.com/hngsjc?']
    get_uid('uid.txt', start_crawl_uid)

    print number_of_pages_to_crawl
    print start_crawl_uid
    print interval

    simuLogin()
    stop = timeit.default_timer()
    print('running time: ' + str(stop - start))



