import os
import requests
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

    def convert_to_json(self, xml):
        path = 'plugins/jsonmodel_from_format/resource/ead'
        url = f'{self.config["baseurl"]}/{path}'
        token = self.client.session.headers['X-ArchivesSpace-Session']
        headers = {
            'Content-Type': 'text/xml',
            'X-ArchivesSpace-Session': token,
        }
        return requests.post(url, data=xml, headers=headers, timeout=None).json()  # noqa

    def delete(self, uri):
        return self.client.delete(uri)

    def get(self, uri):
        return self.client.get(uri).json()

    # def import(self, json):

    def ping(self):
        self.client.authorize()
        print('Login OK!')

    def post(self, uri, payload):
        return self.client.post(uri, json=payload)
