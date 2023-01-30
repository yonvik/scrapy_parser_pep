TABLE_NAME = 'name'
TABLE_STATUS = 'status'
TABLE_NUMBER = 'number'
NAME_SPIDER = 'pep'
FIELDS_NAME = ('Статус', 'Количество')
FILE_NAME = 'status_summary_{time}.csv'
TOTAL = 'Итого'

DOMAINS_SPIDER_PEP = 'peps.python.org'
SPIDER_URL = f'https://{DOMAINS_SPIDER_PEP}/'
PEP_PATTERN = r'PEP (?P<number>\d+) \S (?P<name>.+) \| peps\.python\.org'

DT_FORMAT = '%Y-%m-%dT%H-%M-%S'
