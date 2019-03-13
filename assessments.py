#!/usr/bin/env python

import csv
import json
import os

data = []
target_resources = {}

DATA_DIRECTORY = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'assessments')  # noqa
base_path = os.path.dirname(os.path.realpath(__file__))
resources = os.path.join(base_path, 'resources.csv')

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
                # TODO: delete fields from json
                # TODO: replace old resource id with rid ['records']['ref]
                print(rid)
