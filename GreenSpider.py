# coding=utf-8
import urllib2

import requests
from bs4 import BeautifulSoup
import ssl


# ssl._create_default_https_context = ssl._create_unverified_context

class GreenSpider():
    '''
    基于BeautifulSoup的爬虫
    '''
    # 私有实例变量（外部访问会报错）
    __url = 'http://www.ppdai.com/'
    # 实例变量
    public_url = ''

    def set_url(self, url):
        self.__url = url

    def base_spider_requests(self):
        '''
        使用request取html
        :return: 返回一个网址的soup对象
        '''
        r = requests.get(self.__url)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'lxml')
        return soup

    def base_spider_urllib2(self):
        '''
        使用urllib2取html
        :return: 返回一个网址的soup对象
        '''
        # 伪装浏览器头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

        req = urllib2.Request(self.__url,
                              headers=headers)
        html = urllib2.urlopen(req).read()
        # response = urllib2.urlopen(self.__url)
        # html = response.read()
        soup = BeautifulSoup(html, 'lxml')
        return soup

    def file_Spider(self):
        '''
        返回一个文件的soup对象
        :return: 某文件的soup对象
        '''
        soup = BeautifulSoup(open("<html>data</html>"))
        return soup

    def soup_struct_data(self):
        '''
        几个简单的浏览结构化数据的方法
        :return:
        '''
        soup = self.base_spider_urllib2()
        # soup.title # <title>拍拍贷官网_互联网信用借贷平台_网络贷款_投资理财</title>
        # soup.title.name # title
        # soup.title.string  # 拍拍贷官网_互联网信用借贷平台_网络贷款_投资理财
        # soup.title.parent.name  # head
        # print soup.p  # <p class="title">我要借款</p>
        # print soup.p["class"]  # ['title']
        # print soup.find_all('a')  # [<a class="ppdlogo" href="http://www.ppdai.com/"></a>, <a class="appdownload"
        # print soup.find(rel="nofollow") # <a href="http://www.p2peye.com" rel="nofollow" target="_blank">网贷天眼</a>
        print soup.find_all(rel="nofollow")  # [<a href="http://www.p2peye.com" rel="nofollow" target="_blank">\u7f51\u8d37\u5929\u773c</a>,
        # <a href="http://www.wdzj.com/" rel="nofollow" target="_blank">\u7f51\u8d37\u4e4b\u5bb6</a>]
        # href="http://www.ppdai.com/landingappdownload.html" target="_blank">APP</a>……\n</a>]

        # for link in soup.find_all('a'): 返回所有链接的网址
        #     print(link.get('href'))


    def leg_tag(self, soup):
        '''
        Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,
        所有对象可以归纳为4种: Tag , NavigableString , BeautifulSoup , Comment .
        对Tag对象进行操作
        :return:
        '''
        tag = soup.a
        # tag.name
        # print type(tag) # <class 'bs4.element.Tag'>
        # print tag # <body><noscript><meta content="0;url=http://www.baidu.com/" http-equiv="refresh"/></noscript></body>
        # print tag.name # body
        # print tag['div']
        # print tag.attrs # {}
        # return tag


if __name__ == '__main__':
    green_spider = GreenSpider()
    # print green_spider.base_spider_urllib2()
    # tag = green_spider.leg_tag(green_spider.base_spider_urllib2())
    green_spider.soup_struct_data()
