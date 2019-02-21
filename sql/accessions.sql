SELECT
    a.id as linked_accession_id,
    -- a.identifier as accession_identifier,
    a.title as accession_title,
    r.id as current_resource_id,
    -- r.identifier as resource_identifier,
    substring_index(substring_index(r.identifier, '["', -1), '",', 1) as resource_identifier_clean,
    r.title as resource_title,
    r.ead_id
    # aspace_relationship_position (max)
    # system_mtime (now)
    # user_mtime (now)
    # suppressed (0)
FROM resource r
JOIN spawned_rlshp sr ON r.id = sr.resource_id
JOIN accession a ON a.id = sr.accession_id
;