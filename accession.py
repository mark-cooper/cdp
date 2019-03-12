#!/usr/bin/env python

import csv
import datetime
import os

data = []
inserts = []
positions = {}
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
        insert = {}
        if rid in positions:
            positions[rid] += 1
        else:
            positions[rid] = 0
        insert['accession_id'] = accession['linked_accession_id']
        insert['resource_id'] = target_resources[rid]
        insert['aspace_relationship_position'] = positions[rid]
        insert['system_mtime'] = datetime.datetime.now()
        insert['user_mtime'] = datetime.datetime.now()
        inserts.append(insert)
        matched += 1

print(matched)
print(inserts)
