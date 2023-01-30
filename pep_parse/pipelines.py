import csv
from collections import defaultdict
from datetime import datetime as dt

from pep_parse.settings import BASE_DIR, DIR_OUTPUT
from pep_parse.constants import (
    FIELDS_NAME,
    DT_FORMAT,
    FILE_NAME,
    TOTAL,
    TABLE_STATUS
)


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item[TABLE_STATUS]] += 1
        return item

    def close_spider(self, spider):
        time = dt.now().strftime(DT_FORMAT)
        path = BASE_DIR / DIR_OUTPUT / FILE_NAME.format(time=time)

        with open(path, mode='w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(FIELDS_NAME)
            writer.writerows(self.status_count.items())

            total = sum(self.status_count.values())
            writer.writerow([TOTAL, total])
