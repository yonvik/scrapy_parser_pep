import re

import scrapy

from pep_parse.items import PepParseItem
from pep_parse.constants import (
    TABLE_NAME,
    TABLE_NUMBER,
    TABLE_STATUS,
    NAME_SPIDER,
    DOMAINS_SPIDER_PEP,
    SPIDER_URL,
    PEP_PATTERN
)


class PepSpider(scrapy.Spider):
    name = NAME_SPIDER
    allowed_domains = [DOMAINS_SPIDER_PEP, ]
    start_urls = [SPIDER_URL]

    def parse(self, response):
        yield from response.follow_all(
            css='section[id=numerical-index] tbody td:nth-of-type(2) a',
            callback=self.parse_pep
        )

    def parse_pep(self, response):
        title = re.match(
            PEP_PATTERN,
            response.xpath("//title/text()").get()
        )
        yield PepParseItem(
            {
                TABLE_NAME: title.group(TABLE_NAME),
                TABLE_NUMBER: title.group(TABLE_NUMBER),
                TABLE_STATUS: response.css(
                    'dt:contains("Status") + dd abbr::text'
                ).get()
            }
        )
