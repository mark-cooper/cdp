#!/usr/bin/env python

import csv
import os

data = []
target_resources = {}

base_path = os.path.dirname(os.path.realpath(__file__))
accessions = os.path.join(base_path, 'accessions.csv')
resources = os.path.join(base_path, 'resources.csv')

matched = 0

with open(resources) as f:
    reader = csv.DictReader(f)
    for row in reader:
        target_resources[row['resource_identifier']] = row['resource_id']

with open(accessions) as f:
    reader = csv.DictReader(f)
    data = [r for r in reader]

for accession in data:
    rid = accession['resource_identifier_clean']
    if rid in target_resources:
        matched += 1
        aid = accession['linked_accession_id']
        pos = 0
        system_mtime = ''
        user_mtime = ''

print(matched)
