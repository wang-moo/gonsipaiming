# -*- coding: utf-8 -*-
import re
import time

import scrapy
import logging

from alibaba.items import AlibabaItem


class RankingSpider(scrapy.Spider):
    """
    网站：www.alibaba.com
    爬取 搜索词 led 8w 的搜索结果列表
    在搜索结果中去找到，https://yusing.en.alibaba.com(Ningbo Yusing Lighting) ，这个店铺的排名
    系统每15分钟去看一次排名
    系统连续运行4h
    以上出结果排名波动图
    https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=led+8w&page=
    """
    name = 'ranking'
    # allowed_domains = []

    # url = 'www.alibaba.com'

    page = 1
    key_word = 'led+8w'
    url = 'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={}&page={}'
    url1 = url.format(key_word, page)
    start_urls = [url1]

    standing_list = []

    def parse(self, response):
        item = AlibabaItem()
        try:
            # content = response.xpath(
            #     "//div[@class='l-col-main']/div[@class='l-main-wrap']/div[@class='l-theme-card-box']/div/div")
            num = re.search('"total":(\d*)', response.text).group(1)
            # # result = self.get_result(content, item)
            # for i in content:
            #     href = i.xpath(
            #         "./div[@class='m-gallery-product-item-v2']//div[@class='stitle']/a/@href").extract_first()
            #     if href == '//yusing.en.alibaba.com/company_profile.html#top-nav-bar':
            #         # if href == '//meishansun.en.alibaba.com/company_profile.html#top-nav-bar':
            #         ranking_list_num = i.xpath('./@data-vcount').extract()[0]
            #         name = \
            #         i.xpath("./div[@class='m-gallery-product-item-v2']//div[@class='stitle']/a/text()").extract()[0]
            #
            #         item['ranking_list_num'] = ranking_list_num
            #         item['name'] = name
            #         item['url'] = 'https:' + href
            #         item['page'] = self.page
            #         item['time'] = time.time()
            #         yield item
            #         self.crawler.engine.close_spider(self, '已找到目标停止爬虫')
            #     else:
            #         pass
            # # yield result
            for n in range(int(num) - 1):
                item['page'] = self.page
                yield scrapy.Request(url=self.url.format(self.key_word, self.page), callback=self.circulation,
                                     meta={'item': item})
                self.page += 1
        except Exception as e:
            logging.info(e)
            logging.info('被封了')

    def circulation(self, response):
        item = response.meta['item']

        content = response.xpath(
            "//div[@class='l-col-main']/div[@class='l-main-wrap']/div[@class='l-theme-card-box']/div/div")
        # result = self.get_result(content, item)
        for i in content:
            href = i.xpath("./div[@class='m-gallery-product-item-v2']//div[@class='stitle']/a/@href").extract_first()
            if href == '//yusing.en.alibaba.com/company_profile.html#top-nav-bar':
                # if href == '//meishansun.en.alibaba.com/company_profile.html#top-nav-bar':
                ranking_list_num = i.xpath('./@data-vcount').extract()[0]
                name = i.xpath("./div[@class='m-gallery-product-item-v2']//div[@class='stitle']/a/text()").extract()[0]

                item['ranking_list_num'] = ranking_list_num
                item['name'] = name
                item['url'] = 'https:' + href
                item['time'] = time.time()
                yield item
                self.crawler.engine.close_spider(self, '已找到目标停止爬虫')
            else:
                pass

    # def get_result(self, content, item):
    #     for i in content:
    #         ranking_list_num = i.xpath('./@data-vcount').extract()[0]
    #         href = i.xpath("./div[@class='m-gallery-product-item-v2']//div[@class='stitle']/a/@href").extract_first()
    #         name = i.xpath("./div[@class='m-gallery-product-item-v2']//div[@class='stitle']/a/text()").extract()[0]
    #         if href == '//yusing.en.alibaba.com/company_profile.html#top-nav-bar':
    #             item['ranking_list_num'] = ranking_list_num
    #             item['name'] = name
    #             item['url'] = 'https:' + href
    #             print(name)
    #             print(222)
    #             yield item
    #             self.crawler.engine.close_spider(self, '已找到目标停止爬虫')
    #         else:
    #             pass
