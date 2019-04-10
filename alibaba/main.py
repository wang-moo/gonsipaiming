import time
import os
from scrapy import cmdline

start = time.time()
while True:

    os.system('scrapy crawl ranking')
    time.sleep(900)
    end = time.time()
    if end - start >= 14400:
        break

# cmdline.execute('scrapy crawl ranking'.split())
