#!/usr/bin/env python

# https://github.com/archivesspace/archivesspace/blob/master/backend/app/controllers/assessment.rb#L15-L23
# https://github.com/archivesspace/archivesspace/blob/master/backend/spec/controller_assessment_spec.rb

import csv
import json
import os
import re
from cdp import ArchivesSpace
from time import sleep

data = []
target_resources = {}

DATA_DIRECTORY = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'assessments')  # noqa
base_path = os.path.dirname(os.path.realpath(__file__))
resources = os.path.join(base_path, 'resources.csv')

service = ArchivesSpace(ArchivesSpace.DEFAULT_CONFIG)
service.ping()

FIELDS_TO_DELETE = [
    'collections',
    'create_time',
    'repository',
    'system_mtime',
    'uri',
    'user_mtime',
]

matched = 0

with open(resources) as f:
    reader = csv.DictReader(f)
    for row in reader:
        target_resources[row['resource_identifier']] = row['resource_id']

for assessment in os.listdir(DATA_DIRECTORY):
    if assessment.endswith('.json'):
        with open(os.path.join(DATA_DIRECTORY, assessment)) as json_file:
            identifier = os.path.splitext(os.path.basename(json_file.name))[0]
            if identifier in target_resources:
                data = json.load(json_file)
                rid = target_resources[identifier]
                repo_uri = data['repository']['ref']
                path = f'{repo_uri}/assessments'

                # delete fields not used for import
                for field in FIELDS_TO_DELETE:
                    del data[field]

                # replace old resource id with rid ['records'][0]['ref]
                for record in data['records']:
                    if not 'resources' in record['ref']:
                        continue
                    updated_record_id = re.sub(r'(\d+)$', rid, record['ref'])
                    record['ref'] = updated_record_id

                print(f'Creating assessment for: {rid}')
                service.post(path, data)
                sleep(0.1)
