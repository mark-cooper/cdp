#!/usr/bin/env python

import csv
import os

data = []
target_resources = {}

base_path = os.path.dirname(os.path.realpath(__file__))
collection_management = os.path.join(base_path, 'collection_management.csv')  # noqa
resources = os.path.join(base_path, 'resources.csv')

matched = 0

with open(resources) as f:
    reader = csv.DictReader(f)
    for row in reader:
        target_resources[row['resource_identifier']] = row['resource_id']

with open(collection_management) as f:
    reader = csv.DictReader(f)
    data = [r for r in reader]

for cm in data:
    rid = cm['resource_identifier_clean']
    if rid in target_resources:
        matched += 1

print(matched)
