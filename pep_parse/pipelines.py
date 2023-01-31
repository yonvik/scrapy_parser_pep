import csv
from collections import defaultdict
from datetime import datetime as dt

from pep_parse.settings import (
    BASE_DIR,
    DIR_OUTPUT,
    FIELDS_NAME,
    DT_FORMAT,
    FILE_NAME,
    TOTAL,
    TABLE_STATUS,
)


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item[TABLE_STATUS]] += 1
        return item

    def close_spider(self, spider):
        with open(
            BASE_DIR / DIR_OUTPUT / FILE_NAME.format(
                time=dt.now().strftime(DT_FORMAT)),
            mode='w',
            encoding='utf-8'
        ) as csvfile:
            csv.writer(csvfile, dialect=csv.unix_dialect).writerows([
                FIELDS_NAME,
                *(self.status_count.items()),
                [TOTAL, sum(self.status_count.values())]
            ])
