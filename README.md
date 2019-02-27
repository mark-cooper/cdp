# CDP

Support plugin and scripts for CDP.

```
virtualenv venv --python=python3
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m unittest discover
python3 identifiers.py
```

## Steps

- Run reports
- Run identifiers against incoming XML
- Export and restore database
- Enable plugin for v2.5.2
- Start backend to get resources csv
- Set `CDP_PASSWORD` for environment
- Get count of resources from db [ex: 4268]
- `SELECT count(*) FROM archivesspace.resource;`
- [TODO] Run delete resources
- Confirm correct count of resources from db [ex: 2917]
- [TODO] Run delete related
- [TODO] Import incoming XML
- [TODO] Restore related
