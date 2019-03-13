# CDP

Support plugin and scripts for CDP.

```bash
virtualenv venv --python=python3
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m unittest discover
python3 identifiers.py

mkdir plugins
cd plugins
git clone https://github.com/lyrasis/aspace-importer.git
```

## Steps

- `./setup.sh` # warning this deletes csv & files in `./data/`
- Set `CDP_PASSWORD` for environment
- Copy ead records to `data/ead`
- Export and restore database
- Run reports (also counts, below)
- Run `identifiers.py` against incoming XML
- Update the ArchivesSpace config for CDP (`config/config.rb`)
- Update `build.xml` set env `-Xmx8192m`
- Start backend to get `resources.csv` (make backup)
- Check resources csv count matches number of ead records
- `SELECT count(*) FROM resource;`[ex: 4270]
- Run `delete assessments.py` (`ls data/assessments | wc -l`)
- Run `delete_resources.py`
- Stop ArchivesSpace
- Confirm count of resources from db [ex: 4270 - 2887 = 1383]
- Run `import.py` to prepare import files
- `ls /tmp/aspace/ead/*/*.xml | wc -l` # 1383
- Start ArchivesSpace using Docker (below) to import XML
- `ls /tmp/aspace/ead/*/*.xml.err | wc -l`
- `ls /tmp/aspace/json/*/*.json | wc -l`
- Restart ArchivesSpace to get updated `resources.csv`
- Stop ArchivesSpace
- Create `sql/wip.sql` (db dump)
- Run `accession.py` (`SELECT count(*) FROM spawned_rlshp;`)
- Run `collection_management.py`
- Run `user_defined.py`
- Start ArchivesSpace
- Run `assessments.py`
- Done!

Running ArchivesSpace for the import step:

```bash
docker run -it \
  --rm \
  --name aspace \
  --net=host \
  -e ASPACE_JAVA_XMX='-Xmx8192m' \
  -v $PWD/config:/archivesspace/config \
  -v $PWD/plugins:/archivesspace/plugins \
  -v /tmp/aspace:/tmp/aspace \
  archivesspace/archivesspace:2.5.2
```

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
