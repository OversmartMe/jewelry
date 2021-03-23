import scrapy



class jewelrySpider(scrapy.Spider):
    name = 'jewelry'
    allowed_domains = ['houseofindya.com']
    start_urls = ['https://www.houseofindya.com/zyra/necklace-sets/cat']

    custom_settings = {'FEED_URI': "jewelry_%(time)s.csv",
                       'FEED_FORMAT': 'csv'}


    def parse(self, response):


        print("procesing:" + response.url)

        # Extract data using css selectors

        product_name = response.css("label::text").getall()
        price_range = response.css(".fal.fa-rupee-sign::text").getall()



        row_data = zip(product_name, price_range)

        # Making extracted data row wise
        for item in row_data:
            # create a dictionary to store the scraped info
            scraped_info = {
                # key:value
                'page': response.url,
                'product_name': item[0],
                # item[0] means product in the list and so on, index tells what value to assign
                'price_range': item[1]

            }

            # yield or give the scraped info to scrapy
            yield scraped_info


