# -*- coding: utf-8 -*-
# @Filename : kugou.py
# @Functions : 爬取酷狗TOP500的数据->https://www.kugou.com/yy/rank/home/1-8888.html
# @Time : 2022/12/23 11:01
# @Author : Mixue Lin
# @Email : m15528382598@163.com
import os
import pprint

import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

def get_info(url,header,data):
    wb_data = requests.get(url,headers=header)
    soup = BeautifulSoup(wb_data.text,'html.parser')
    ranks = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_num')
    titles = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > a')
    times = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span')
    for rank,title,time in zip(ranks,titles,times):
        data["rank"].append(rank.get_text().strip())
        data["singer"].append((title.get_text().split('-')[1]).strip())
        data["song"].append((title.get_text().split('-')[0]).strip())
        data["time"].append(time.get_text().strip())

if __name__=="__main__":
    # 请求头
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(num)) for num in range(1,25)]
    # 储存采集到的数据
    data = {"rank":[],"singer":[],"song":[],"time":[]}
    for url in urls:
        get_info(url,header,data)
        # time.sleep(1)
    data = pd.DataFrame(data)
    data.to_csv(os.getcwd() + "\output.csv",index=False)
