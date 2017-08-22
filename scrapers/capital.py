import json

from .base import Scraper
from .config import scrap_sites , base_urls


class CapitalMedia(Scraper):
    def __init__(self):
        super(CapitalMedia, self).__init__()
        self.url = scrap_sites["capital"]
        self.base = Scraper()

    def scrap_page(self):
        result_html = self.base.get_html_content(self.url)
        data = []
        items =result_html.find_all("div", class_="entry-cover-image ")
        for item in items:
            img_url = item.find("img").get("src")
            link = item.find("a").get("href")
            data.append({
            'link':link,
            'img':img_url
                })
        print (json.dumps(data, indent=2))     
        self.base.s3.put_object(
            Bucket='taxclock.codeforkenya.org',
            ACL='public-read',
            Key='data/standard-news.json',
            Body=json.dumps(data))
        






        

