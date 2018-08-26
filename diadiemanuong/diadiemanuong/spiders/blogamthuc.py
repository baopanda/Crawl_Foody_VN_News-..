import lxml
import scrapy


class amthuc365(scrapy.Spider):
    name = 'blogamthuc'
    allowed_domains = ["blogamthuc.com"]

    counter = 0
    max_page = 1201
    index = 0

    def start_requests(self):
        print("1")
        urls = []
        base_url = 'http://www.blogamthuc.com/'

        self.counter = 0
        while self.counter < self.max_page:
            self.counter += 1
            urls.append(base_url + 'page/' + str(self.counter))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_links)

    def parse_links(self, response):
        links = []
        ARTICLE_SELECTOR = '//div[@id="content"]'
        for row in response.xpath(ARTICLE_SELECTOR).extract():
            if row.strip():
                row = lxml.html.fromstring(row)
                # title = next(iter(row.xpath('//h3[contains(@class,"title_news")]//a/text()')), "").strip()
                # url = next(iter(row.xpath('//h3[contains(@class,"title_news")]//a/@href')), "").strip()
                link = next(iter(row.xpath('//h2/a/@href')), "").strip()
                links.append(link)
        print(links)

        for link in links:
            print(link)
            yield scrapy.Request(url=str(link), callback=self.parse_news)


    def parse_news(self, response):
        print(response)
        # title =[]
        title = response.xpath('//h1/text()').extract()
        # description =  response.xpath('//div[contains(@itemprop,"reviewBody")]/blockquote/font/span/text()').extract()
        # description =  response.xpath('//div[contains(@itemprop,"ingredients")]/p/text()').extract()

        des2 = response.xpath('//div[@class="entry clearfix"]/p/text()').extract()


        print(title)
        # print(description)
        filename1 = ""
        filename = title[0]
        for a in range(0, 20):
            filename1 += filename[a]
        print(filename1)
        with open("data_blogamthuc/{}.txt".format(filename1), "w", encoding='utf-8') as file:
            for a in title:
                file.write(a+"\n")

            # for i1 in description:
            #     file.write(i1 + "\n")
            for i in des2:
                file.write(i + "\n")
        # item = DiadiemanuongItem()
        # item[des2] = des2
        # item[des3] = des3
        # item[des4] = des4
        # item[des5] = des5
        # item[des6] = des6
        # item[des7] = des7
        # item[des8] = des8
        # yield item



