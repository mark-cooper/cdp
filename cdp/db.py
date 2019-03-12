import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

class DB:
    """Database client."""

    ACCESSION_INSERT_QUERY = """
      INSERT INTO `spawned_rlshp`
      (
        `accession_id`,
        `resource_id`,
        `aspace_relationship_position`,
        `system_mtime`,
        `user_mtime`
      )
      VALUES (%s,%s,%s,%s,%s)
    """

    COLLECTION_MANAGEMENT_INSERT_QUERY = """
      INSERT INTO `collection_management`
      (
        `lock_version`,
        `json_schema_version`,
        `resource_id`,
        `processing_plan`,
        `processing_priority_id`,
        `processing_status_id`,
        `processors`,
        `create_time`,
        `system_mtime`,
        `user_mtime`
      )
      VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    # TODO: text_2
    USER_DEFINED_INSERT_QUERY = """
      INSERT INTO `user_defined`
      (
        `lock_version`,
        `json_schema_version`,
        `resource_id`,
        `integer_1`,
        `string_1`,
        `string_2`,
        `string_3`,
        `string_4`,
        `text_1`,
        `create_time`,
        `system_mtime`,
        `user_mtime`
      )
      VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    DEFAULT_CONFIG = {
        'host': 'localhost',
        'database': 'archivesspace',
        'user': 'as',
        'password': 'as123',
    }

    def __init__(self, config: dict):
        self.config = config
        self.connection = mysql.connector.connect(
            host=self.config['host'],
            database=self.config['database'],
            user=self.config['user'],
            password=self.config['password'],
            use_pure=True
        )

    def close(self):
        if self.connected():
            self.connection.close()

    def connected(self):
        return self.connection.is_connected()

    def insert(self, query: str, data: list):
        try:
            cursor = self.connection.cursor(prepared=True)
            result = cursor.executemany(query, data)
            self.connection.commit()
            print(cursor.rowcount, "Records inserted.")
        except mysql.connector.Error as error:
            print("Error: {}".format(error))
        finally:
            cursor.close()
