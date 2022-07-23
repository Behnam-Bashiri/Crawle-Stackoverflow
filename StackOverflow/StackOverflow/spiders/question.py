from operator import le
from turtle import title
import scrapy


class QuestionSpider(scrapy.Spider):
    name = 'question'

    def start_requests(self):
        url_list = [

        ]
        for i in range(2,153):
            url_list.append('https://stackoverflow.com/questions/tagged/python?page=%d' % i)

        urls = []
        urls.append('https://stackoverflow.com/questions')   
        for url in url_list:
            urls.append(url)
            yield scrapy.Request(url=url, callback=self.parse)
        

    def parse(self, response):
        title_question = response.xpath("//h3[@class='s-post-summary--content-title']/a/text()").extract()
        body_question = response.xpath("//div[@class='s-post-summary--content-excerpt']/text()").extract()
        author_question = response.xpath("//div[@class='s-user-card--link d-flex gs4']/a/text()").extract()
        link_question = response.xpath("//h3[@class='s-post-summary--content-title']/a/@href").extract()

        with open('question.txt', 'a') as f:
            for i in range(len(title_question)):
                f.write("******"+title_question[i]+"******"+'\n'\
                    +body_question[i]+'\n'\
                        +"@"+author_question[i]+'\n'\
                            +"link : "+link_question[i]+'\n'\
                                +"----------------------------------------------------------------"+'\n')
            f.close()