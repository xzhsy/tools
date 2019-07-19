#!/usr/bin/python2
# -*- coding:UTF-8 -*-
import sys
import os
import smtplib
import re

from email.header import Header
from email.mime.text import MIMEText
from urllib2 import Request
from urllib2 import urlopen

phone = {'User-Agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36'}
pc = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
mobile = re.compile(r'http://m.')

class siteCheck(object):
    def __init__(self,url):

        self.url = url



    def sendmail(self):
        mail_host = 'mail.asiainfo.com'
        mail_user = 'hanchang@asiainfo.com'
        mail_pass = 'Xzhsy@019'

        sender = 'hanchang@asiainfo.com'
        receivers = ['2665185155@qq.com','1277567324@qq.com']

        mail_msg = """
        <p> 监控网址。。。</p>
        <p><a href="%s">异常网址url：%s </a></p>
        """ % (self.url,self.url)
        message = MIMEText(mail_msg,'html','utf-8')
        message['From'] = Header("自动监控", 'utf-8')
        message['To'] = Header("告警邮件", 'utf-8')

        subject = '网址异常告警'
        message['Subject']=Header(subject,'utf-8')

        try:
            smtp = smtplib.SMTP()
            smtp.connect(mail_host)
            smtp.login(mail_user,mail_pass)
            #  采用本地服务器posttfix或sedmail发信时，未绑定域名将被邮件服务商拒收，
            #smtp = smtplib.SMTP("localhost")
            smtp.sendmail(sender,receivers,message.as_string())
            print("发送成功")
        except smtplib.SMTPException as e:
            print("发送失败：%s" % e)

    def check(self):
        # print(self.url)
        if mobile.findall(self.url) != 0:
            ua = phone
        else:
            ua = pc
        # print(ua)
        req = Request(self.url, headers=ua)
        r = urlopen(req)
        print(r.getcode())
        print(r.geturl())
        if r.getcode() != 200:
             self.sendmail()

if __name__=="__main__":
    urllist=['http://m.mdpda.com/','http://www.mallb2b.com/product/1pros83a737d0/']
    for i in urllist:
        check=siteCheck(i)
        check.check()
        # check.sendmail()