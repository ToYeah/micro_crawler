import scrapy
from micro_crawler.items import PropertyInfo


class MicroSpider(scrapy.Spider):
    name = "micro"

    def start_requests(self):
        urls = [
            'https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ra=013&rn=0005&ek=000517640&cb=0.0&ct=9999999&mb=0&mt=9999999&et=9999999&cn=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sngz=&po1=04&pc=10'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        building_name = ""
        for building in response.css("div.cassetteitem"):
            building_name = building.css("div.cassetteitem_content-title::text").get()
            for cassette in response.css("tr.js-cassette_link"):
                yield PropertyInfo(
                    name=building_name,
                    floor=response.css("div.cassetteitem")[0].css("tr.js-cassette_link")[0].css("td::text")[4].get(),
                    price_rent=cassette.css("span.cassetteitem_price--rent").css("span.cassetteitem_other-emphasis::text").get(),
                    price_admin=cassette.css("span.cassetteitem_price--administration::text").get(),
                    price_deposit=cassette.css("span.cassetteitem_price--deposit::text").get(),
                    price_gratuity=cassette.css("span.cassetteitem_price--gratuity::text").get(),
                    floor_plan=cassette.css("span.cassetteitem_madori::text").get(),
                    floor_area=cassette.css("span.cassetteitem_menseki::text").get()
                )
