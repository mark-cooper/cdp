SELECT
    r.id as current_resource_id,
    -- r.identifier as resource_identifier,
    substring_index(substring_index(r.identifier, '["', -1), '",', 1) as resource_identifier_clean,
    r.title,
    r.ead_id,
    ud.integer_1,
    ud.string_1,
    ud.string_2,
    ud.string_3,
    ud.string_4,
    ud.text_1,
    ud.text_2,
    ud.enum_4_id,
    ud.created_by,
    ud.last_modified_by
    # create_time
    # system_mtime
    # user_mtime
FROM resource r
JOIN user_defined ud ON r.id = ud.resource_id
;
