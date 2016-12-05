# coding=utf-8
import time
from BeautifulSoup import BeautifulSoup
import re
from GreenSpider import GreenSpider


class PpdSpider(GreenSpider):
    '''
    基于GreenSpider的爬虫,关于拍拍贷网站的一系列方法
    '''
    # 私有实例变量（外部访问会报错）
    __url_ppdai_homepage = 'http://www.ppdai.com/'
    __url_ppdai_map = 'http://map.invest.ppdai.com/'
    __url_ppdai_data = 'http://ppdai.p2peye.com/shuju/'

    def shuju_page(self):
        '''
        数据页
        :return:
        '''

        data = self.base_spider_webdriver(self.__url_ppdai_data)
        # from data import data
        soup = BeautifulSoup(data)
        print soup

    def hp_deal_number(self):
        '''
        获取首页注册用户人数，成功借款数，成交总额
        :return:dict(注册用户人数，成功借款数，成交总额)
        '''

        data = self.base_spider_webdriver(self.__url_ppdai_homepage)
        #from data import data
        soup = BeautifulSoup(data)
        regist = soup("div",  attrs={'class': 'head_inner_left'})
        # 注册用户人数
        regist_number = regist[0].next.next

        # 成功借款数
        loan = soup.findAll("div", attrs={'class': 'head_inner_right'})
        loan_number = loan[0].contents[1].next

        # 成交总额
        GMV = loan[0].contents[4].next

        deals = dict(
        regist_number=regist_number,
        loan_number=loan_number,
        g_m_v=GMV
        )
        return deals

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
            if deals['regist_number'] == deals_base['regist_number'] and deals['loan_number'] == deals_base['loan_number']\
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
                #todo:将存入数据库或excel

    def p2p_manage_money(self):
        '''
        P2P理财页面
        :return:
        '''

if __name__ == '__main__':
    ppd_spider = PpdSpider()
    #ppd_spider.hp_deal_number()
    #ppd_spider.hp_deal_monitor()
    ppd_spider.shuju_page()