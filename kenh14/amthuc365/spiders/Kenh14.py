import scrapy
from scrapy.selector import Selector

from amthuc365.items import Amthuc365Item

class Kenh14(scrapy.Spider):
    name = "kenh14"
    count = 0;
    allowed_domain = ["kenh14.vn"]
    start_urls = ['http://kenh14.vn/chi-an-vai-thoi-cung-da-co-tan-5-kieu-nguoi-the-nay-ban-thuoc-kieu-nao-vay-20180611162407038.chn',
                  'http://kenh14.vn/lai-ghen-ti-voi-7-eleven-o-dai-loan-khi-so-huu-mon-kem-tra-sua-tran-chau-hay-ho-tu-hinh-thuc-den-mui-vi-20180611124751991.chn',
                  'http://kenh14.vn/co-mot-con-pho-am-thuc-tuy-ngan-nhung-hoi-tu-vo-van-mon-ngon-tu-an-vat-den-an-no-tren-khu-pho-co-20180611004705007.chn',
                  'http://kenh14.vn/nha-hang-o-anh-dam-dung-nam-doc-de-lam-mon-trang-mieng-cho-khach-20180610204502272.chn',
                  'http://kenh14.vn/o-bangkok-co-loai-kem-ma-chi-hoi-con-nha-giau-moi-co-du-tien-de-an-20180610163129663.chn',
                  'http://kenh14.vn/da-nang-hay-lam-het-an-sua-chua-voi-muoi-nguoi-ta-con-cho-quat-vao-nuoc-rau-ma-20180610110018616.chn',
                  'http://kenh14.vn/mi-lanh-trong-bat-xua-roi-nguoi-han-con-co-mon-mi-lanh-xien-que-doc-dao-the-nay-co-20180609193147319.chn',
                  'http://kenh14.vn/nhung-mon-trang-mieng-tu-dua-dang-khuay-dao-he-nay-tai-sai-gon-20180610120224741.chn',
                  ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        print("1")
        count = 0;
        urls_item = response.xpath('//div[@class="kbw-content "]').extract()
        tittle = response.xpath('//h1/text()').extract()
        content = response.xpath('//div[@class="knc-content"]/p/text()').extract()
        print(content)
        print(tittle)
        filename1=""
        filename = tittle
        for a in range(20,30):
            filename1 += filename[a]



        # it=response.xpath('//a[@href="#k14-detail-comment"]').extract()
        # filename = Selector(text=it).xpath('//span[@class="item-comment-not-async"]/@rel').extract()
        #
        print(filename1)
        with open("data/{}.txt".format(filename1), "w",encoding='utf-8') as file:
            for a in tittle:
                file.write(a)
            print("\n")
            for i in content:
                file.write(i + "\n")

        item = Amthuc365Item
        item['tittle'] = response.xpath('//h1/text()').extract()
        item['content'] = response.xpath('//div[@class="knc-content"]/p/text()').extract()
        yield item


    # def parse_item(self,response):
    #     item = Amthuc365Item
    #     item['tittle'] = response.xpath('//h1/text()').extract()
    #     item['content'] = response.xpath('//div[@class="knc-content"]/p/text()').extract()
    #     yield item