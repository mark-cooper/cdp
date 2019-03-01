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
```

## Steps

- Set `CDP_PASSWORD` for environment
- Copy ead records to `data/ead`
- Export and restore database
- Run reports (also counts, below)
- Run `identifiers.py` against incoming XML
- Enable cdp and format plugin for v2.5.2 (`config.rb`)
- Start backend to get `resources.csv` (make backup)
- Check resources csv count matches number of ead records
- Get count of resources from db [ex: 4268]
- Run `delete assessments.py`
- Run `delete_resources.py`
- Confirm count of resources from db [ex: 4268 - 2887 = 1381]
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
