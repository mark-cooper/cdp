SELECT
    r.id as current_resource_id,
    -- r.identifier as resource_identifier,
    substring_index(substring_index(r.identifier, '["', -1), '",', 1) as resource_identifier_clean,
    r.title,
    r.ead_id,
    ed.title,
    ed.location,
    ed.location_sha1,
    ed.publish,
    ed.created_by,
    ed.last_modified_by
    # create_time
    # system_mtime
    # user_mtime
FROM resource r
JOIN external_document ed ON r.id = ed.resource_id
;