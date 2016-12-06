# coding=utf-8
import time
from BeautifulSoup import BeautifulSoup
import re
from GreenSpider import GreenSpider
import xlwt

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class TianyanSpider(GreenSpider):
    '''
    基于GreenSpider的爬虫,关于天眼网站的一系列方法
    '''
    __page = 11
    # 私有实例变量（外部访问会报错）
    # 数码科技有限公司
    def company_list(self):
        '''
        获取首页注册用户人数，成功借款数，成交总额
        :return:dict(注册用户人数，成功借款数，成交总额)
        '''
        __url_tianyan_sheying = 'http://nanjing.tianyancha.com/search/p' + str(self.__page) + '?key=%E6%91%84%E5%BD%B1'
        # 创建一个workbook
        book = xlwt.Workbook(encoding='utf-8', style_compression=0)
        # 创建一个sheet，命名为dede
        sheet = book.add_sheet('dede', cell_overwrite_ok=True)
        j = 0
        i = 0
        for pages in range(1, 10):
            url_tianyan_shuma = 'http://nanjing.tianyancha.com/search/p' + str(self.__page) + '?key=%E6%95%B0%E7%A0%81'
            data = self.base_spider_webdriver(url_tianyan_shuma)
            soup = BeautifulSoup(data)
            loan = soup.findAll("div", attrs={'class': 'title'})
            company_names = soup.findAll("span", attrs={'ng-bind-html': 'node.name | trustHtml'})

            for each in company_names:
                if j % 3 == 0:
                     print
                sheet.write(j, 1, each.text.decode('utf-8'))
                print each.text
                j += 1
            for each in loan:
                if i%3 == 0:
                    sheet.write(i/3, 2, each.text.decode('utf-8'))
                    print
                if i % 3 == 1:
                    sheet.write((i-1)/3, 3, each.text.decode('utf-8'))
                if i % 3 == 2:
                    sheet.write((i-2)/3, 4, each.text.decode('utf-8'))
                print each.text
                i += 1
            self.__page += 1
        book.save('E:/777.xls')



        # print loan[01].text
        # regist = soup("div",  attrs={'class': 'head_inner_left'})
        # # 注册用户人数
        # regist_number = regist[0].next.next
        #
        # # 成功借款数
        # loan = soup.findAll("div", attrs={'class': 'head_inner_right'})
        # loan_number = loan[0].contents[1].next
        #
        # # 成交总额
        # GMV = loan[0].contents[4].next
        #
        # deals = dict(
        # regist_number=regist_number,
        # loan_number=loan_number,
        # g_m_v=GMV
        # )
        # return deals

    def hp_deal_monitor(self):
        '''
        循环获取注册用户人数，成功借款数，成交总额
        :return:
        '''
        # 用来存储上一次的deal，发生变化则记录新的
        deals_base = self.hp_deal_number()

        while 1:
            # 获取注册用户人数，成功借款数，成交总额
            deals = self.hp_deal_number()
            if deals['regist_number'] == deals_base['regist_number'] and deals['loan_number'] == deals_base[
                'loan_number'] \
                    and deals['g_m_v'] == deals_base['g_m_v']:
                # time.sleep(1)
                print deals['regist_number']
                print deals['loan_number']
                print deals['g_m_v']
                pass
            else:
                # 睡眠0.1秒
                # time.sleep(1)
                print deals['regist_number']
                print deals['loan_number']
                print deals['g_m_v']


                # todo:将存入数据库或excel

    def p2p_manage_money(self):
        '''
        P2P理财页面
        :return:
        '''


if __name__ == '__main__':
    tianyan_spider = TianyanSpider()
    tianyan_spider.company_list()

    # ppd_spider.hp_deal_number()
