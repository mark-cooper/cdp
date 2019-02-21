#!/usr/bin/env python

import os
import csv
from cdp import EadFingerprint
from cdp import ProgressIndicator

DATA_DIRECTORY = './data/ead/'
OUTPUT_CSV = 'identifiers.csv'
metadata = []
total = len([name for name in os.listdir(DATA_DIRECTORY)])
progress = ProgressIndicator(total)

for resource in os.listdir(DATA_DIRECTORY):
    if resource.endswith('.xml'):
        with open(os.path.join(DATA_DIRECTORY, resource)) as fp:
            progress.tick()
            metadata.append(EadFingerprint(fp).process())

with open(OUTPUT_CSV, 'w') as of:
    dict_writer = csv.DictWriter(of, EadFingerprint.ELEMENTS)
    dict_writer.writeheader()
    dict_writer.writerows(metadata)
