SELECT
    r.id as current_resource_id,
    -- r.identifier as resource_identifier,
    substring_index(substring_index(r.identifier, '["', -1), '",', 1) as resource_identifier_clean,
    r.title,
    r.ead_id,
    cm.processing_plan,
    cm.processing_priority_id,
    cm.processing_status_id,
    cm.processors
    # created_by
    # last_modified_by
    # create_time
    # system_mtime
    # user_mtime
FROM resource r
JOIN collection_management cm ON r.id = cm.resource_id
;
