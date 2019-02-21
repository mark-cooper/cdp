import os
import unittest
from cdp import EadFingerprint


class TestEadFingerprint(unittest.TestCase):
    def setUp(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, 'fixtures', 'ead.xml')) as xml:  # noqa
            self.fingerprint = EadFingerprint(xml)

    def test_title(self):
        title = self.fingerprint.title()
        self.assertEqual(title, 'Aperture Labs Records')

    def test_unitid(self):
        unitid = self.fingerprint.unitid()
        self.assertEqual(unitid, '1234.abcd')

    def test_url(self):
        url = self.fingerprint.url()
        self.assertEqual(url, None)
