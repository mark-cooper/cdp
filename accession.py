#!/usr/bin/env python

from cdp import DB
import csv
import datetime
import os

data = []
inserts = []
positions = {}
target_resources = {}

base_path = os.path.dirname(os.path.realpath(__file__))
accessions = os.path.join(base_path, 'accession.csv')
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
        i = [x if x != 'NULL' else None for x in insert.values()]
        inserts.append(i)
        matched += 1

print(f'{matched} Records matched.')

db = DB(DB.DEFAULT_CONFIG)
db.insert(DB.ACCESSION_INSERT_QUERY, inserts)
db.close()
