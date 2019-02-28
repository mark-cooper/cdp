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
- Run reports
- Copy ead records to `data/ead`
- Run `identifiers.py` against incoming XML
- Export and restore database
- Enable cdp and format plugin for v2.5.2 (`config.rb`)
- Start backend to get `resources.csv` (make backup)
- Check resources csv count matches number of ead records
- Get count of resources from db [ex: 4268]
- `SELECT count(*) FROM archivesspace.resource;`
- Run `delete assessments.py`
- Run `delete_resources.py`
- Confirm count of resources from db [ex: 4268 - 2887 = 1381]
- [TODO] Run delete related
- [TODO] Import incoming XML
- [TODO] Restore related
