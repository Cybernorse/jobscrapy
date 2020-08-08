import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
import csv 
from itertools import zip_longest
from job_scraper.items import JobScraperItem
from urllib.request import urlparse

class indeed_jobs(CrawlSpider):
    name='jobs'
    def __init__(self, url=None,*args, **kwargs):
        super(indeed_jobs, self).__init__(*args, **kwargs)
        self.args=url.split('|')
        allowed_domains=[urlparse(self.args[0]).netloc]
        self.start_urls = [self.args[0]]

    def parse(self, response):
        
        formdata = {'q': self.args[1],
                'l': self.args[2], 
                }
        custom_settings={
            'LOG_LEVEL':None,
        }
        yield FormRequest.from_response(response,formdata=formdata, clickdata={'type': 'submit'},callback=self.parse1)

    def parse1(self, response):

        job_links=response.css('h2.title a::attr(href)').getall()
        for x in job_links:
            if x:
                yield response.follow(x,self.parse2)

        next_page = response.css('ul.pagination-list li a::attr(href)').getall()
        for i in next_page:
            if i is not None:
                yield response.follow(i, self.parse1)

    def parse2(self,response):
        titles=response.xpath('//div[@class="jobsearch-JobInfoHeader-title-container"]/ h3[@class="icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title"]/text()').extract()
        company=response.xpath('//div[@class="jobsearch-InlineCompanyRating icl-u-xs-mt--xs  jobsearch-DesktopStickyContainer-companyrating"]/div[@class="icl-u-lg-mr--sm icl-u-xs-mr--xs"]/text()').extract()
        status=response.xpath('//div[@class="jobsearch-JobMetadataFooter"]/text()').getall()
        Job_details=response.xpath('//div[@class="jobsearch-jobDescriptionText"]//p//text()').getall()+response.xpath('//div[@class="jobsearch-jobDescriptionText"] /ul//text() ').getall()
        if not Job_details :
            Job_details=response.xpath('//div[@class="jobsearch-jobDescriptionText"]//div//text()').getall()
        if not company:
            company=response.xpath('//div[@class="icl-u-lg-mr--sm icl-u-xs-mr--xs"]//a /text()').getall()
        yield{
            'Job Title':titles,
            'Company':company,
            'Post Status':status,
            'Job URL':[response.url],
            'Job Details':Job_details,
        }
'''
extracted_data=zip(items['titles'],items['status'],items['job_urls'],items['companies'],items['days_ago'],items['salaries'],items['short_description'])
with open('jobs.csv', 'a',newline='') as myfile:
wr = csv.writer(myfile)
wr.writerow(("Job titles","Status","Job_urls","Companies","Days_ago","Salaries","Short_description"))
for data in extracted_data:
    r.writerows(data)
'''