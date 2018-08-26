import lxml
import scrapy

class bepgiadinh(scrapy.Spider):
    name = 'thanhnien'
    allowed_domains = ["thanhnien.vn"]

    counter = 0
    max_page = 100
    index = 0

    def start_requests(self):
        print("1")
        urls = []
        base_url = 'https://thanhnien.vn/doi-song/am-thuc/'

        self.counter = 0
        while self.counter < self.max_page:
            self.counter += 1
            urls.append(base_url + 'trang-' + str(self.counter)+".html")

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_links)

    def parse_links(self, response):
        links = []
        ARTICLE_SELECTOR = '//div[@class="relative"]'
        for row in response.xpath(ARTICLE_SELECTOR).extract():
            if row.strip():
                row = lxml.html.fromstring(row)
                # title = next(iter(row.xpath('//h3[contains(@class,"title_news")]//a/text()')), "").strip()
                # url = next(iter(row.xpath('//h3[contains(@class,"title_news")]//a/@href')), "").strip()
                link = "https://thanhnien.vn"+next(iter(row.xpath('//article[@class="story"]/a/@href')), "").strip()
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
        des2 =  response.xpath('//div[@class="sapo"]/div/text()').extract()
        des3 = response.xpath('//div[@id="abody"]/div/text()').extract()
        print(title)
        # print(description)
        filename1 = ""
        filename = title[0]
        for a in range(0, 30):
            filename1 += filename[a]
        print(filename1)
        with open("data_thanhnien/{}.txt".format(filename1), "w", encoding='utf-8') as file:
            for a in title:
                file.write(a)

            for i in des2 + des3:
                file.write(i + "\n")