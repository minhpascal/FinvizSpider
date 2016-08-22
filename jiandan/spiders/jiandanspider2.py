#coding:utf-8
import scrapy
from jiandan.items import JiandanItem
from scrapy.crawler import CrawlerProcess
#scrapy crawl finviz
class jiandanSpider(scrapy.Spider):
    name = "finviz2"
    allowed_domains = []

    start_urls = ["http://www.finviz.com/screener.ashx?v=151&f=idx_dji&o=-perf1w"]

    def parse(self,response):
        content_list =  response.xpath('//table[@bgcolor="#d3d3d3"]/tr[@valign="top"]')
        items = []
        for content in content_list:
            item = JiandanItem()
            item['No'] = content.xpath('td[1]/a/text()').extract()
            item['Ticker'] = content.xpath('td[2]/a/text()').extract()

            item['Sector'] = content.xpath('td[3]/a/text()').extract()
            # item['Industry'] = content.xpath('td[5]/a/text()').extract()
            # item['Country'] = content.xpath('td[6]/a/text()').extract()
            # item['MarketCap'] = content.xpath('td[7]/a/text()').extract()
            # item['PE'] = content.xpath('td[8]/a/text()').extract()
            # item['Price'] = content.xpath('td[9]/a/span/text()').extract()
            # if(len(item['Price'])==0):
            #     item['Price']=content.xpath('td[9]/a/text()').extract()
            # item['ChangeV'] = content.xpath('td[10]/a/span/text()').extract()
            # item['Volume'] = content.xpath('td[11]/a/text()').extract()
            # print '--ticker',item['ticker']
            items.append(item)
            yield item


        next_tr = response.xpath('//div[@id="screener-content"]/table/tr')#翻页
        next_a = next_tr[-2].xpath('td/a')
        new_url=''
        print next_a[-1].xpath('@class').extract()
        if next_a[-1].xpath('@class').extract()[0]=="tab-link":
            new_url = next_a[-1].xpath('@href').extract()
        print '--new_url',new_url
        if(len(new_url)>0):
            new_url = "http://www.finviz.com/"+new_url[0]
            print new_url
            yield scrapy.Request(new_url,callback=self.parse)
