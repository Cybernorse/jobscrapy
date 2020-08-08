# scrape jobs from indeed.com 
Installing Requirements with
* python3.7 -m pip install -r requirements.txt
* you will activate the crawler with same commands you use to run scrapy with.

Usage

* open you terminal and go to this directory ```cd /job_scraper/job_scraper/```
* Activate the crawler with ```scrapy crawl jobs -o jobs.csv -a url="https://www.indeed.com|jobtitle|city"``` and that's it
* input your desired job title and city there and any regional domain related to indeed.com
* this will export a csv file full of your desired jobs but it only scrapes data from indeed.com and no other.
* you should never change anything from above command except for file name, url like ```https://pk.indeed.com``` , job title amd city.
