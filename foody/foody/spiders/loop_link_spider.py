import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

class SelectLink(scrapy.Spider):
    name = "link"
    allow_domains = ["foody.vn"]
    start_urls = ['https://www.foody.vn/ha-noi']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="content-container fd-clearbox ng-scope"]//a/@href'))),
        Rule(LinkExtractor(allow=("https://www.foody.vn/",)),callback='parse_item'),
    )

    def parse(self,response):
        link = response.xpath('//h1/text()').extract()
        print(link)
