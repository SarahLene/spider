# -*- coding: utf-8 -*-
# @Filename : qidianzhongwenwang.py
# @Functions : 爬虫起点中文网的全部作品信息->https://www.qidian.com/all/page1/
# @Time : 2022/12/24 13:48
# @Author : Mixue Lin
# @Email : m15528382598@163.com
import requests
from lxml import etree
import time
import pandas as pd

def get_info(url,header,data):
    res = requests.get(url,headers=header)
    selector = etree.HTML(res.text)
    infos = selector.xpath('//li[@data-rid]')
    for info in infos:
        url = info.xpath('div[2]/h2/a/@href')[0]
        title = info.xpath('div[2]/h2/a/text()')[0]
        author = info.xpath('div[2]/p[1]/a[1]/text()')[0]
        style1 = info.xpath('div[2]/p[1]/a[2]/text()')[0]
        style2 = info.xpath('div[2]/p[1]/a[3]/text()')[0]
        style = style1 +"·"+ style2
        complete = info.xpath('div[2]/p[1]/span/text()')[0]
        introduce = info.xpath('div[2]/p[2]/text()')[0].strip()
        wordNum = info.xpath('div[2]/p[3]/span/span/text()')[0].strip()
        for key in data.keys():
            data[key].append(eval(key))

if __name__=="__main__":
    urls = ['https://www.qidian.com/all/page{}/'.format(str(num)) for num in range(1,6,1)]
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    cols = ["title","author","style","complete","introduce","wordNum","url"]
    data = {}
    for c in cols:
        data[c] = []
    for url in urls:
        get_info(url,header,data)
        time.sleep(1)
    data = pd.DataFrame(data)
    data.to_csv("qidianzhongwenwang.csv")
