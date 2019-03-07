#!/usr/bin/env python
import csv
import os
import shutil

REPOSITORY_MAP = {
  'Rare Book and Manuscript Library': 'RBML',
  'Avery Architectural and Fine Arts Library': 'AV',
  'The Burke Library at Union Theological Seminary': 'UT',
  'C. V. Starr East Asian Library': 'EA',
}

data = []

DATA_DIRECTORY = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'ead')  # noqa
IMPORT_DIRECTORY = os.path.join('/tmp', 'aspace', 'ead')
base_path = os.path.dirname(os.path.realpath(__file__))
identifiers = os.path.join(base_path, 'identifiers.csv')

with open(identifiers) as f:
    reader = csv.DictReader(f)
    data = [r for r in reader]

for identifier in data:
    repo_code = REPOSITORY_MAP[identifier['repo_name']]
    dest_path = os.path.join(IMPORT_DIRECTORY, repo_code)
    os.makedirs(dest_path, exist_ok=True)
    fn = identifier['filename']
    source = os.path.join(DATA_DIRECTORY, fn)
    dest = os.path.join(dest_path, fn)
    # copy data dir file to dest
    print(f'Copying [{source}] to [{dest}]')
    shutil.copy(source, dest)
