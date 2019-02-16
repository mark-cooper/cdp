#!/usr/bin/env python

import os
import csv
import sys
from bs4 import BeautifulSoup

DATA_DIRECTORY = './data/'
OUTPUT_CSV = 'identifiers.csv'
metadata = []
count = 0
total = len([name for name in os.listdir(DATA_DIRECTORY)])

def get_title(xml):
    return xml.ead.eadheader.filedesc.titlestmt.titleproper.contents[0].strip()

def get_unitid(xml):
    return xml.ead.archdesc.did.unitid.contents[0].strip()

def get_url(xml):
    return xml.ead.eadheader.eadid['url']

# https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.1 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

for resource in os.listdir(DATA_DIRECTORY):
    if resource.endswith('.xml'):
        with open(os.path.join(DATA_DIRECTORY, resource)) as fp:
            progress(count, total, status=f' processing identifiers [{count}]')
            xml = BeautifulSoup(fp, 'xml')
            try:
                url = get_url(xml)
            except:
                pass
            metadata.append({
              'unitid': get_unitid(xml),
              'title': get_title(xml),
              'url': url,
            })
            count += 1

with open(OUTPUT_CSV, 'w') as of:
    keys = ['unitid', 'title', 'url']
    dict_writer = csv.DictWriter(of, keys)
    dict_writer.writeheader()
    dict_writer.writerows(metadata)
