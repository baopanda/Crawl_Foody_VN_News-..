import lxml
import scrapy

class diadiemanuong(scrapy.Spider):
    name = 'diadiemanuong'
    allowed_domains = ["diadiemanuong.com"]

    counter = 0
    max_page = 200
    index = 0

    def start_requests(self):
        print("1")
        urls = []
        base_url = 'http://diadiemanuong.com/co-gi-hot/am-thuc'

        self.counter = 0
        while self.counter < self.max_page:
            self.counter += 1
            urls.append(base_url + '?p=' + str(self.counter))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_links)

    def parse_links(self, response):
        links = []
        ARTICLE_SELECTOR = '//div[contains(@class,"large-8 columns")]'
        for row in response.xpath(ARTICLE_SELECTOR).extract():
            if row.strip():
                row = lxml.html.fromstring(row)
                # title = next(iter(row.xpath('//h3[contains(@class,"title_news")]//a/text()')), "").strip()
                # url = next(iter(row.xpath('//h3[contains(@class,"title_news")]//a/@href')), "").strip()
                link = "http://diadiemanuong.com"+next(iter(row.xpath('//div[@class="result-items"]/a[@class="block-item"]/@href')), "").strip()
                links.append(link)
        print(links)

        for link in links:
            print(link)
            yield scrapy.Request(url=str(link), callback=self.parse_news)


    def parse_news(self, response):
        print(response)
        # title =[]
        title = response.xpath('//h3/text()').extract()
        description = response.xpath('//*[@id="body_editor"]/p/text()').extract()
        print(title)
        print(description)
        filename1 = ""
        filename = title[0]
        for a in range(5, 30):
            filename1 += filename[a]
        print(filename1)
        with open("data_nhahang_quanan/{}.txt".format(filename1), "w", encoding='utf-8') as file:
            for a in title:
                file.write(a)

            for i in description:
                file.write(i + "\n")