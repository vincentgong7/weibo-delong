# -*- coding: utf-8 -*-
__author__ = 'vincentgong'
import re
import time
from getWeiboPage import getWeiboPage

class Celestine:
     def __init__(self, uidList, outputFolder, wantpages, interval, startcrawlpage):
         self.uidList = uidList
         self.outputFolder = outputFolder
         self.wantpages = wantpages
         self.interval = interval
         self.startcrawlpage = startcrawlpage

     def getTotalPost(self, html):
         tmp = re.findall(r"[0-9]+<\\/strong><span class=\\.S_txt2\\.>微博", html);
         # print html
         result = tmp[0][:tmp[0].index('<')]
         print ('Parsed total posts: ' + str(result))
         return result

     def getTotalPage(self, html):
         tmp = re.findall(r"page=[0-9]+#feedtop.. suda-uatrack=..key=tblog_profile_v6&value=weibo_page..>第&nbsp;[0-9]+&nbsp;页", html);
         result = tmp[0][5:tmp[0].index('#')]
         print ('Parsed total pages: ' + str(result))
         return result

     def writefile(self,filename,content):
        fw = file(filename,'w')
        fw.write(content)
        fw.close()

     def start(self):
         for userInfo in self.uidList:
             time.sleep(5)
             try:
                 uid = userInfo.split(',')[0]
                 print('Start crawling uid: ')
                 print(uid)
                 uidURL = userInfo.split(',')[1]
                 print(uidURL)
                 print ''
                 gwp = getWeiboPage(uid, uidURL, self.outputFolder + '/' + str(uid))
                 gwp.body['page'] = 1;

                 html1 = gwp.get_firstpage()
                 est_totalPost = 0
                 est_totalPost = int(self.getTotalPost(html1))

                 if est_totalPost <= 15:
                     continue

                 if est_totalPost > 15:
                     html2 = gwp.get_secondpage();
                     if est_totalPost <= 30 :
                         continue

                 if est_totalPost > 30:
                     html3 = gwp.get_thirdpage();
                     if est_totalPost <= 45:
                         continue

                 totalPages = 0
                 totalPages = int(self.getTotalPage(html3))

                 if self.startcrawlpage <3 or self.startcrawlpage > totalPages:
                     self.startcrawlpage = 2

                 if self.wantpages>0:
                     if totalPages >= self.wantpages + self.startcrawlpage:
                         totalPages = self.wantpages + self.startcrawlpage

                 for page in range(self.startcrawlpage, totalPages+1):
                    gwp.body['pre_page'] = page-1;
                    gwp.body['page'] = page;
                    print page
                    '''
                    gwp.get_firstpage();
                    gwp.get_secondpage();
                    gwp.get_thirdpage();'''

             except BaseException:
                 self.writefile('./fail_log.txt', uid)
                 break