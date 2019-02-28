#!/usr/bin/env python

import csv
import os
from cdp import ArchivesSpace
from time import sleep

base_path = os.path.dirname(os.path.realpath(__file__))
data = []
resources = os.path.join(base_path, 'resources.csv')
service = ArchivesSpace(ArchivesSpace.DEFAULT_CONFIG)
service.ping()

with open(resources) as f:
    reader = csv.DictReader(f)
    data = [r for r in reader]

# TODO: check for record not found?
for resource in data:
    uri = resource['resource_uri']
    print(f"Deleting: {uri}")
    service.delete(uri)
    sleep(0.1)
