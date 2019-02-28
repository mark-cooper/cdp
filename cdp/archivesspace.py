import os
from asnake.client import ASnakeClient


class ArchivesSpace(object):
    """ArchivesSpace client."""

    DEFAULT_CONFIG = {
        'baseurl': 'http://localhost:4567',
        'username': 'admin',
        'password': os.environ['CDP_PASSWORD'],
    }

    def __init__(self, config: dict):
        self.config = config
        self.client = ASnakeClient(
            baseurl=self.config['baseurl'],
            username=self.config['username'],
            password=self.config['password'],
        )

    def delete(self, uri):
        self.client.delete(uri)

    def ping(self):
        self.client.authorize()
        print('Login OK!')
