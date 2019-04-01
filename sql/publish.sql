UPDATE agent_corporate_entity SET publish = true, system_mtime = NOW() WHERE create_time >= CURDATE();
UPDATE agent_family SET publish = true, system_mtime = NOW() WHERE create_time >= CURDATE();
UPDATE agent_person SET publish = true, system_mtime = NOW() WHERE create_time >= CURDATE();
UPDATE subject SET publish = true, system_mtime = NOW() WHERE create_time >= CURDATE();
