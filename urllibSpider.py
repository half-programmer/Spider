# coding=utf-8
import urllib
import urllib2

class Spider():

    def baseSpider(self):
        response = urllib2.urlopen('http://www.baidu.com/')
        html = response.read()
        print html

    def resSpider(self):
        req = urllib2.Request('http://www.baidu.com')
        response = urllib2.urlopen(req)
        the_page = response.read()
        print the_page


    def postSpider(self):
        '''
        使用Post
        :return:
        '''
        url = 'http://www.shacus.top'

        values = {'name' : 'WHY',
          'location' : 'SDU',
          'language' : 'Python' }

        data = urllib.urlencode(values) # 编码工作
        req = urllib2.Request(url, data)  # 发送请求同时传data表单
        response = urllib2.urlopen(req)  #接受反馈的信息
        the_page = response.read()  #读取反馈的内容

    def getSpider(self):
        '''
        使用get发送表单
        :return:
        '''
        data = {}

        data['name'] = 'WHY'
        data['location'] = 'SDU'
        data['language'] = 'Python'

        url_values = urllib.urlencode(data)
        print url_values

        #name=Somebody+Here&language=Python&location=Northampton
        url = 'http://www.example.com/example.cgi'
        full_url = url + '?' + url_values

        data = urllib2.open(full_url)