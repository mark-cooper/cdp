#!/usr/bin/env python

from cdp import DB
import csv
import datetime
import os

data = []
inserts = []
target_resources = {}

base_path = os.path.dirname(os.path.realpath(__file__))
user_defined = os.path.join(base_path, 'user_defined.csv')
resources = os.path.join(base_path, 'resources.csv')

matched = 0

with open(resources) as f:
    reader = csv.DictReader(f)
    for row in reader:
        target_resources[row['resource_identifier']] = row['resource_id']

with open(user_defined) as f:
    reader = csv.DictReader(f)
    data = [r for r in reader]

for ud in data:
    rid = ud['resource_identifier_clean']
    if rid in target_resources:
        insert = {}
        insert['lock_version'] = 0
        insert['json_schema_version'] = 1
        insert['resource_id'] = target_resources[rid]
        insert['integer_1'] = ud['integer_1']
        insert['string_1'] = ud['string_1']
        insert['string_2'] = ud['string_2']
        insert['string_3'] = ud['string_3']
        insert['string_4'] = ud['string_4']
        insert['text_1'] = ud['text_1']
        # insert['text_2'] = ud['text_2']
        insert['create_time'] = datetime.datetime.now()
        insert['system_mtime'] = datetime.datetime.now()
        insert['user_mtime'] = datetime.datetime.now()
        i = [x if x != 'NULL' else None for x in insert.values()]
        inserts.append(i)
        matched += 1

print(f'{matched} Records matched.')

db = DB(DB.DEFAULT_CONFIG)
db.insert(DB.USER_DEFINED_INSERT_QUERY, inserts)
db.close()
