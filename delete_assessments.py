#!/usr/bin/env python

import csv
import json
import os
from cdp import ArchivesSpace
from time import sleep

data = []
target_resources = []

DATA_DIRECTORY = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'assessments')  # noqa
base_path = os.path.dirname(os.path.realpath(__file__))
resources = os.path.join(base_path, 'resources.csv')
assessments = os.path.join(base_path, 'assessment.csv')

service = ArchivesSpace(ArchivesSpace.DEFAULT_CONFIG)
service.ping()

# get list of resources (by identifier) with assessments to delete
with open(resources) as f:
    reader = csv.DictReader(f)
    target_resources = [r['resource_identifier'] for r in reader]

# read assessments data from db query
with open(assessments) as f:
    reader = csv.DictReader(f)
    data = [r for r in reader]

for assessment in data:
    repo_id = assessment['repo_id']
    rid = assessment['resource_identifier_clean']
    aid = assessment['linked_assessment_id']
    if rid in target_resources:
        uri = f'/repositories/{repo_id}/assessments/{aid}'
        print(f"Fetching: {uri}")
        result = service.get(uri)
        with open(os.path.join(DATA_DIRECTORY, f'{rid}.json'), 'w') as f:
            f.write(json.dumps(result))
        print(f'Deleting: {uri}')
        service.delete(uri)
        sleep(0.1)
