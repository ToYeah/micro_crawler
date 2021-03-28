import scrapy
from micro_crawler.items import PropertyInfo


class MicroSpider(scrapy.Spider):
    name = "micro"

    def start_requests(self):
        url = 'https://suumo.jp'
        query = '/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ra=013&rn=0005&ek=000517640&cb=0.0&ct=9999999&mb=0&mt=9999999&md=01&md=06&md=07&et=9999999&cn=1&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sngz=&po1=25&pc=50'
        if query is None:
            url+=self.query
        else:
            url+=query
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        next_url = ""
        for building in response.css("div.cassetteitem"):
            building_name = building.css("div.cassetteitem_content-title::text").get()
            for cassette in building.css("tbody"):
                yield PropertyInfo(
                    name=building_name,
                    floor=cassette.css("td::text")[4].get().replace('\r\n\t\t\t\t\t\t\t\t\t\t\t', ''),
                    price_rent=cassette.css("span.cassetteitem_price--rent span.cassetteitem_other-emphasis::text").get(),
                    price_admin=cassette.css("span.cassetteitem_price--administration::text").get(),
                    price_deposit=cassette.css("span.cassetteitem_price--deposit::text").get(),
                    price_gratuity=cassette.css("span.cassetteitem_price--gratuity::text").get(),
                    floor_plan=cassette.css("span.cassetteitem_madori::text").get(),
                    floor_area=cassette.css("span.cassetteitem_menseki::text").get()
                )
        next_url = response.css("p.pagination-parts a::attr(href)").get()
        if next is not None:
            yield response.follow(next_url, callback=self.parse)
