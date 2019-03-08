# CDP
AppConfig[:plugins] << "shelve_it" # not related
AppConfig[:plugins] << "cdp"
AppConfig[:plugins] << "aspace-importer"

AppConfig[:enable_indexer] = false
AppConfig[:solr_backup_number_to_keep] = 0

AppConfig[:importer_profiles] = [
  {
    name: 'RBML',
    batch: {
      create_enums: true,
      enabled: true,
      repository: {
        repo_code: 'RBML',
      },
      username: 'admin',
    },
    import: {
      converter: "EADConverter",
      type: "ead_xml",
      directory: "/tmp/aspace/ead/RBML",
      error_file: "/tmp/aspace/ead/RBML/importer.err",
    },
    json: {
      directory: "/tmp/aspace/json/RBML",
      error_file: "/tmp/aspace/json/RBML/importer.err",
    },
    threads: 1,
    verbose: true,
  },
  {
    name: 'AV',
    batch: {
      create_enums: true,
      enabled: true,
      repository: {
        repo_code: 'AV',
      },
      username: 'admin',
    },
    import: {
      converter: "EADConverter",
      type: "ead_xml",
      directory: "/tmp/aspace/ead/AV",
      error_file: "/tmp/aspace/ead/AV/importer.err",
    },
    json: {
      directory: "/tmp/aspace/json/AV",
      error_file: "/tmp/aspace/json/AV/importer.err",
    },
    threads: 1,
    verbose: true,
  },
  {
    name: 'EA',
    batch: {
      create_enums: true,
      enabled: true,
      repository: {
        repo_code: 'EA',
      },
      username: 'admin',
    },
    import: {
      converter: "EADConverter",
      type: "ead_xml",
      directory: "/tmp/aspace/ead/EA",
      error_file: "/tmp/aspace/ead/EA/importer.err",
    },
    json: {
      directory: "/tmp/aspace/json/EA",
      error_file: "/tmp/aspace/json/EA/importer.err",
    },
    threads: 1,
    verbose: true,
  },
  {
    name: 'UT',
    batch: {
      create_enums: true,
      enabled: true,
      repository: {
        repo_code: 'UT',
      },
      username: 'admin',
    },
    import: {
      converter: "EADConverter",
      type: "ead_xml",
      directory: "/tmp/aspace/ead/UT",
      error_file: "/tmp/aspace/ead/UT/importer.err",
    },
    json: {
      directory: "/tmp/aspace/json/UT",
      error_file: "/tmp/aspace/json/UT/importer.err",
    },
    threads: 1,
    verbose: true,
  }
]