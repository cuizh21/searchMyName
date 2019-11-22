# -*- coding: utf-8 -*-

import requests
from pyquery import PyQuery as pq


def get_html(url, code="utf-8"):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        # print("test")
        return r.text
    except Exception as e:
        print(e)
        return " "


def main(name):
    search_name_url = "http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=" + name
    doc = pq(get_html(search_name_url))
    print(doc)
    search_list = doc('#content_left h3.t a').items()
    i = 0
    print(i)
    for li in search_list:
        i+=1
        print(i)
        print('标题：' + li.text())
        print('链接：' + li.attr('href'))
        print("")
        
if __name__ == '__main__':
    main("崔忠辉")

