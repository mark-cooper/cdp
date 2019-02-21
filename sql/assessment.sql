# review assessment behavior via ui
SELECT
    r.id as current_resource_id,
    -- r.identifier as resource_identifier,
    substring_index(substring_index(r.identifier, '["', -1), '",', 1) as resource_identifier_clean,
    r.title,
    r.ead_id,
    a.id as linked_assessment_id
    # aspace_relationship_position (max)
    # system_mtime (now)
    # user_mtime (now)
    # suppressed (0)
FROM resource r
JOIN assessment_rlshp ar ON r.id = ar.resource_id
JOIN assessment a ON a.id = ar.assessment_id
;
