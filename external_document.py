#!/usr/bin/env python

from cdp import DB
import csv
import datetime
import os

data = []
inserts = []
target_resources = {}

base_path = os.path.dirname(os.path.realpath(__file__))
external_document = os.path.join(base_path, 'external_document.csv')
resources = os.path.join(base_path, 'resources.csv')

matched = 0

with open(resources) as f:
    reader = csv.DictReader(f)
    for row in reader:
        target_resources[row['resource_identifier']] = row['resource_id']

with open(external_document) as f:
    reader = csv.DictReader(f)
    data = [r for r in reader]

for ed in data:
    rid = ed['resource_identifier_clean']
    if rid in target_resources:
        insert = {}
        insert['lock_version'] = 0
        insert['json_schema_version'] = 1
        insert['resource_id'] = target_resources[rid]
        insert['title'] = ed['title']
        insert['location'] = ed['location']
        insert['location_sha1'] = ed['location_sha1']
        insert['publish'] = ed['publish']
        insert['created_by'] = ed['created_by']
        insert['last_modified_by'] = ed['last_modified_by']
        insert['create_time'] = datetime.datetime.now()
        insert['system_mtime'] = datetime.datetime.now()
        insert['user_mtime'] = datetime.datetime.now()
        i = [x if x != 'NULL' else None for x in insert.values()]
        inserts.append(i)
        matched += 1

print(f'{matched} Records matched.')

db = DB(DB.DEFAULT_CONFIG)
db.insert(DB.EXTERNAL_DOCUMENT_INSERT_QUERY, inserts)
db.close()
