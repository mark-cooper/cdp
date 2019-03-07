# CDP

Support plugin and scripts for CDP.

```
virtualenv venv --python=python3
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m unittest discover
python3 identifiers.py

mkdir -p data/assessments
mkdir -p data/ead
mkdir -p data/resources
```

## Steps

- Set `CDP_PASSWORD` for environment
- Copy ead records to `data/ead`
- Export and restore database
- Run reports (also counts, below)
- Run `identifiers.py` against incoming XML
- Update the ArchivesSpace config for CDP (`config.rb`)
- Start backend to get `resources.csv` (make backup)
- Check resources csv count matches number of ead records
- Get count of resources from db [ex: 4268]
- Run `delete assessments.py`
- Run `delete_resources.py`
- Confirm count of resources from db [ex: 4268 - 2887 = 1381]
- [TODO] Prepare import directories
- [TODO] Import incoming XML
- [TODO] Restore related

Counts:

```sql
SELECT count(*) FROM resource; # b4: 4268, af: 2887
SELECT count(*) FROM assessment; # b4: 77, af: 46
SELECT count(*) FROM collection_management; # b4: 4301, af: 4240
SELECT count(*) FROM spawned_rlshp; # b4: 4544, af: 2195
SELECT count(*) FROM user_defined; # b4: 8412, af: 7043
```

CLI import testing:

```bash
echo "export TOKEN=$(curl -Fpassword=$CDP_PASSWORD http://localhost:4567/users/admin/login | jq '.session')" > .session
source .session

curl \
  -H "Content-Type: text/xml" \
  -H "X-ArchivesSpace-Session: $TOKEN" \
  -X POST \
  -d @data/ead/2157842_MERGED-CLEAN_ead.xml \
  "http://localhost:4567/plugins/jsonmodel_from_format/resource/ead" > ead.json

curl \
  -H "Content-Type: application/json" \
  -H "X-ArchivesSpace-Session: $TOKEN" \
  -X POST \
  -d @ead.json \
  "http://localhost:4567/repositories/2/batch_imports"
```
