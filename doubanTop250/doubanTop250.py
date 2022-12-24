# -*- coding: utf-8 -*-
# @Filename : doubanTop250.py
# @Functions : 爬取豆瓣前250的图书信息->https://book.douban.com/top250
# @Time : 2022/12/24 10:41
# @Author : Mixue Lin
# @Email : m15528382598@163.com
import requests
from lxml import etree
import pandas as pd

def get_info(url,header,data):
    html = requests.get(url=url,headers=header)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//tr[@class="item"]')
    for info in infos:
        name = info.xpath('td[2]/div[1]/a/@title')[0]
        url = info.xpath('td[2]/div[1]/a/@href')[0]
        book_infos = info.xpath('td[2]/p[1]/text()')[0]
        book_infos = book_infos.split('/')
        author = book_infos[0].strip()
        publisher = book_infos[-3].strip()
        date = book_infos[-2].strip()
        try:
            price = book_infos[-1].strip()
        except IndexError:
            print(book_infos)
            price = " "
        rank = info.xpath('td[2]/div[2]/span[2]/text()')[0]
        comments = info.xpath('td[2]/div[2]/span[3]/text()')[0].strip('(').strip(')').strip()
        try:
            quote = info.xpath('td[2]/p[@class="quote"]/span/text()')[0].strip()
        except IndexError:
            print(info.xpath('td[2]/p[@class="quote"]/span/text()'))
            quote = " "
        for key in data.keys():
            data[key].append(eval(key))


if __name__=="__main__":
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    urls = ['https://book.douban.com/top250?start={}'.format(str(num)) for num in range(0,501,25)]
    cols = ["name","url","author","publisher","date","price","rank","comments","quote"]
    data = {}
    for col in cols:
        data[col] = []
    for url in urls:
        get_info(url,header,data)
    data = pd.DataFrame(data)
    data.to_csv("doubanTop250.csv")
