UPDATE agent_corporate_entity SET publish = true, system_mtime = NOW() WHERE create_time >= date_sub(curdate(), interval 1 day);
UPDATE agent_family SET publish = true, system_mtime = NOW() WHERE create_time >= date_sub(curdate(), interval 1 day);
UPDATE agent_person SET publish = true, system_mtime = NOW() WHERE create_time >= date_sub(curdate(), interval 1 day);
UPDATE subject SET system_mtime = NOW() WHERE create_time >= date_sub(curdate(), interval 1 day);
