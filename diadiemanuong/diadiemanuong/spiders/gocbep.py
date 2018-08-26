import lxml
import scrapy

class bepgiadinh(scrapy.Spider):
    name = 'gocbep'
    allowed_domains = ["bepgiadinh.com"]

    counter = 0
    max_page = 100
    index = 0

    def start_requests(self):
        print("1")
        urls = []
        base_url = 'https://www.bepgiadinh.com/goc-bep/'

        self.counter = 0
        while self.counter < self.max_page:
            self.counter += 1
            urls.append(base_url + 'page/' + str(self.counter))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_links)

    def parse_links(self, response):
        links = []
        ARTICLE_SELECTOR = '//ul[@class="list-verti"]'
        for row in response.xpath(ARTICLE_SELECTOR).extract():
            if row.strip():
                row = lxml.html.fromstring(row)
                # title = next(iter(row.xpath('//h3[contains(@class,"title_news")]//a/text()')), "").strip()
                # url = next(iter(row.xpath('//h3[contains(@class,"title_news")]//a/@href')), "").strip()
                link = next(iter(row.xpath('//div[@class="wrap-image-article"]/a/@href')), "").strip()
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
        des2 =  response.xpath('//div[@class="object_detail editor-blog"]/p/text()').extract()
        des3 = response.xpath('//div[@class="object_detail editor-blog"]/ul/li/text()').extract()
        des4 = response.xpath('//div[@class="object_detail editor-blog"]/h2/text()').extract()
        print(title)
        # print(description)
        filename1 = ""
        filename = title[0]
        for a in range(0, 30):
            filename1 += filename[a]
        print(filename1)
        with open("data_gocbep/{}.txt".format(filename1), "w", encoding='utf-8') as file:
            for a in title:
                file.write(a)

            # for i1 in description:
            #     file.write(i1 + "\n")
            for i2 in des2:
                file.write(i2 + "\n")
            for i3 in des3:
                file.write(i3+"\n")
            for i4 in des4:
                file.write(i4+"\n")
            # for i5 in des5:
            #     file.write(i5 + "\n")
            # for i6 in des6:
            #     file.write(i6 + "\n")