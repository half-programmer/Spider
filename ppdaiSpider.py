# coding=utf-8
from BeautifulSoup import BeautifulSoup
import re
from GreenSpider import GreenSpider


class PpdSpider(GreenSpider):
    '''
    基于GreenSpider的爬虫,关于拍拍贷网站的一系列方法
    '''

    def hp_deal_number(self):
        '''
        获取首页交易总额及注册人数
        :return:
        '''
        from data import data
        #data = self.base_spider_webdriver()
        soup = BeautifulSoup(data)
        regist = soup("div",  attrs={'class': 'head_inner_left'})
        # 注册用户人数
        regist_number = regist[0].next.next
        print regist_number

        # 成功借款数
        loan = soup.findAll("div", attrs={'class': 'head_inner_right'})
        loan_number = loan[0].contents[1].next
        print loan_number

        # 成交总额
        GMV = loan[0].contents[4].next
        print GMV


if __name__ == '__main__':
    ppd_spider = PpdSpider()
    ppd_spider.hp_deal_number()