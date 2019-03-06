#!/usr/bin/env python

import json
import os
from bs4 import BeautifulSoup
from cdp import ArchivesSpace
from pathlib import Path
from time import sleep

DATA_DIRECTORY = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'ead')  # noqa
OUTPUT_DIRECTORY = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'resources')  # noqa

service = ArchivesSpace(ArchivesSpace.DEFAULT_CONFIG)
service.ping()

for resource in os.listdir(DATA_DIRECTORY):
    fn = Path(os.path.basename(resource)).stem
    result = None
    if resource.endswith('.xml'):
        print(f'Converting: {fn}')
        with open(os.path.join(DATA_DIRECTORY, resource), encoding='utf-8') as f:  # noqa
            xml = BeautifulSoup(f, 'xml')  # check parse
            try:
                result = service.convert_to_json(xml.encode_contents())
            except:
                pass
    if result:
        with open(os.path.join(OUTPUT_DIRECTORY, f'{fn}.json'), 'w') as output:
            json.dump(result, output)
    sleep(0.1)
