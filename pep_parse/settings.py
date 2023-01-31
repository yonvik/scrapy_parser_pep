from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DIR_OUTPUT = 'results'
DOMAINS_SPIDER_PEP = 'peps.python.org'
SPIDER_URL = f'https://{DOMAINS_SPIDER_PEP}/'

BOT_NAME = 'pep_parse'
TABLE_NAME = 'name'
TABLE_STATUS = 'status'
TABLE_NUMBER = 'number'
NAME_SPIDER = 'pep'
FIELDS_NAME = ('Статус', 'Количество')
FILE_NAME = 'status_summary_{time}.csv'
TOTAL = 'Итого'

SPIDER_MODULES = [f'{BOT_NAME}.spiders']
ROBOTSTXT_OBEY = True


FEEDS = {
    f"{DIR_OUTPUT}/pep_%(time)s.csv": {
        "format": "csv",
        "encoding": "utf8",
        "fields": ["number", "name", "status"],
        "item_classes": ["pep_parse.items.PepParseItem"],
        "overwrite": True,
    }
}
FEED_EXPORT_FIELDS = ["number", "name", "status"]

ITEM_PIPELINES = {
    f"{BOT_NAME}.pipelines.PepParsePipeline": 300,
}

DT_FORMAT = '%Y-%m-%dT%H-%M-%S'
