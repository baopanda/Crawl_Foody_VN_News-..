import scrapy
from scrapy_splash import SplashRequest
from foody.items import FoodyItem
from scrapy.selector import Selector

script_start = """
    function main(splash)
        assert(splash:go(splash.args.url))
        assert(splash:wait(0.5))
        local exits = splash:jsfunc([[
            function () {
                var x = document.getElementsByClassName('fd-btn-more');
                if(x.length>0) {
                    return true;
                }
                return false;
            }
        ]])

        local get_dimensions = splash:jsfunc([[
            function () {
                var rect = document.getElementsByClassName('fd-btn-more')[0].getClientRects()[0];
                return {"x": rect.left, "y": rect.top}
            }
        ]])

        local ex = exits()
        local a = 0
        while ex==true and a<40 do
            local dimensions = get_dimensions()
            splash:mouse_click(dimensions.x, dimensions.y)
            splash:set_viewport_full()
            splash:wait(0.5)
            ex = exits()
            a = a +1
        end

        splash:set_viewport_full()
        splash:wait(0.5)

        return splash:html()

    end
    """

script_per_page = """
    function main(splash)
        assert(splash:go(splash.args.url))
        assert(splash:wait(0.5))
        local exits = splash:jsfunc([[
            function () {
                var x = document.getElementsByClassName('fd-btn-more');
                if(x.length>0) {
                    return true;
                }
                return false;
            }
        ]])

        local get_dimensions = splash:jsfunc([[
            function () {
                var rect = document.getElementsByClassName('fd-btn-more')[0].getClientRects()[0];
                return {"x": rect.left, "y": rect.top}
            }
        ]])

        local ex = exits()
        local a = 0
        while ex==true and a<10 do
            local dimensions = get_dimensions()
            splash:mouse_click(dimensions.x, dimensions.y)
            splash:set_viewport_full()
            splash:wait(0.5)
            ex = exits()
            a = a +1
        end

        splash:set_viewport_full()
        splash:wait(1)

        return splash:html()
    end
    """


class FoodySpider(scrapy.Spider):
    name = "foody"
    count = 0
    allowed_domains = ["foody.vn"]
    start_urls = 'https://www.foody.vn/ha-noi/tra-sua-gong-cha-giang-vo'

    def start_requests(self):

        yield SplashRequest(self.start_urls, self.parse)
            # yield Request(url,self.parse)

    def parse(self, response):
        # body = response.body
        # with open("hanoi5.html","wb") as file:
        #     file.write(body)


        print("===============================================================")

        self.count +=1
        path = self.start_urls + "/binh-luan"
        print(path)
        yield SplashRequest(path, self.parse_item, endpoint='execute',
                        args={'lua_source': script_per_page})
        print("++++++++++++{}+++++++++++".format(self.count))
        print("++++++++++++{}+++++++++++".format(len(self.start_urls)))
        print("===============================================================")

    def parse_item(self, response):
        # body = response.body
        page = response.url.split("/")[-2]
        # sel = Selector(response)
        # hxs = HtmlXPathSelector(response)
        list_it= response.xpath('//li[contains(@class,"review-item")]').extract()
        list_item = []
        for it in list_it:
            # item = FoodyItem()
            # content = response.xpath('//div[contains(@class,"review-des")]/div[contains(@class,"rd-des")]/span/text()').extract_first()
            content = Selector(text=it).xpath('//div[contains(@class,"review-des")]/div[contains(@class,"rd-des")]/span/text()').extract_first()
            if content!=None :
                content = content.replace("\n"," ")

            # point =response.xpath('//div[contains(@class,"review-des")]//div[contains(@class,"review-points")]/span/text()').extract_first()
            point = Selector(text=it).xpath('//div[contains(@class,"review-des")]//div[contains(@class,"review-points")]/span/text()').extract_first()
            # print("############################################################")
            # # print(it)
            # print(content)
            # print("############################################################")
            # print(point)

            # list_item.append(point + content)


            if point != None and content != None:
                # list_item.append(point+ "\t" + content)
                list_item.append(point+ "\t" + content)
                # yield self.parse_detail_item(it)

            yield scrapy.Request(it,self.parse_detail_item)


            # yield self.parse_detail_item(it)
            # yield SplashRequest(it, self.parse_item, endpoint='execute',
            #                     args={'lua_source': script_per_page})

        for a in list_item:
            print("###############################")
            print(a)

        with open("data2/{}.txt".format(page), "w",encoding='utf-8') as file:
            for i in list_item:
                file.write(i + "\n")


        # yield scrapy.Request(self.start_urls,self.parse)
        # with open("{}.html".format(page), "wb") as file:
        #     file.write(body)



        # yield self(self.parse())

    def parse_detail_item(self,it):
        print(self.count)
        print("############################################################")
        print(it)
        print("############################################################")
        item = FoodyItem()
        item['content'] = it.xpath('//div[@class="review-des]/div[@class="rd-des"]/span/text()').extract_first()
        item['point'] = it.xpath('//div[@class="review-user"]/div[@class="review-points"]/span/text()').extract_first()
        print("====================================================================")
        print(item['content'])
        print(item['point'])
        print("====================================================================")
        yield (item)








