import lxml
import scrapy

class diadiemanuong(scrapy.Spider):
    name = 'diadiemanuong_congthuc'
    allowed_domains = ["diadiemanuong.com"]

    counter = 0
    max_page = 100
    index = 0

    def start_requests(self):
        print("1")
        urls = []
        base_url = 'http://forum.diadiemanuong.com/home/f14/'

        self.counter = 0
        while self.counter < self.max_page:
            self.counter += 1
            urls.append(base_url + 'index' + str(self.counter)+'.html')

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_links)

    def parse_links(self, response):
        links = []
        ARTICLE_SELECTOR = '//ol[@class="threads"]'
        for row in response.xpath(ARTICLE_SELECTOR).extract():
            if row.strip():
                row = lxml.html.fromstring(row)
                # title = next(iter(row.xpath('//h3[contains(@class,"title_news")]//a/text()')), "").strip()
                # url = next(iter(row.xpath('//h3[contains(@class,"title_news")]//a/@href')), "").strip()
                link = next(iter(row.xpath('//h3/a/@href')), "").strip()
                links.append(link)
        print(links)

        for link in links:
            print(link)
            yield scrapy.Request(url=str(link), callback=self.parse_news)


    def parse_news(self, response):
        print(response)
        # title =[]
        title = response.xpath('//h1/span/a/text()').extract()
        description =  response.xpath('//div[contains(@itemprop,"reviewBody")]/blockquote/font/span/text()').extract()
        des2 =  response.xpath('//div[contains(@itemprop,"reviewBody")]/blockquote/font/span/ul/li/text()').extract()
        des3 = response.xpath('//div[contains(@itemprop,"reviewBody")]/blockquote/font/span/span/text()').extract()
        des4 = response.xpath('//div[contains(@itemprop,"reviewBody")]/blockquote/font/br/text()').extract()
        print(title)
        print(description)
        filename1 = ""
        filename = title[0]
        for a in range(0, 30):
            filename1 += filename[a]
        print(filename1)
        with open("data_congthuc/{}.txt".format(filename1), "w", encoding='utf-8') as file:
            for a in title:
                file.write(a)

            for i in description,des2:
                file.write(i + "\n")
            for i in des2:
                file.write(i + "\n")
            for i in des3:
                file.write(i+"\n")
            for i in des4:
                file.write(i+"\n")