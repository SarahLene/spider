# -*- coding: utf-8 -*-
# @Filename : doupocangqiong.py
# @Functions : 爬取《斗破苍穹》全文小说->http://caissayl.com/book/128/
# @Time : 2022/12/23 14:06
# @Author : Mixue Lin
# @Email : m15528382598@163.com
import os
import pprint
import re

import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

def get_info(url,header,file_path):
    with open(file_path, 'a', encoding='GBK') as fo:
        res = requests.get(url,headers=header)
        if res.status_code == 200:
            contents = re.findall('\s{4}[\u4e00-\u9fa5，。；：”“？！、]+',res.text,re.S)
            head = re.findall('第[一二三四五六七八九]+章\s[\u4e00-\u9fa5]+</h1>',res.text,re.S)
            try:
                head = head[0][:-5]
            except IndexError:
                head = " "
            # soup = BeautifulSoup(res.text, 'html.parser')
            # heads = soup.select('#content > div.page-header.text-center > h1')
            # contents = soup.select('#BookText')
            # pprint.pprint(heads[0].get_text().strip())
            # pprint.pprint()
            fo.write(head + '\n')
            for content in contents:
                content = content.strip()
                # print()
                # print(content)
                fo.write(content+'\n')
            fo.write('\n\n\n\n')
        else:
            pass


if __name__=="__main__":
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    urls = ['http://caissayl.com/book/128/{}.html'.format(str(num)) for num in range(0,1625)]
    FILE_PATH = os.getcwd()+"\doupocangqiong.txt"
    for url in urls:
        get_info(url,header,FILE_PATH)
        # break
        time.sleep(1)
