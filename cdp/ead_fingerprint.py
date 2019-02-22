from bs4 import BeautifulSoup


class EadFingerprint(object):
    """Process EAD fingerprint from XML."""
    ELEMENTS = ['repo_name', 'title', 'unitid', 'url']

    def __init__(self, xml):
        self.data = {}
        self.xml = BeautifulSoup(xml, 'xml')

    def process(self):
        self.repo_name()
        self.title()
        self.unitid()
        try:
            self.url()
        except:
            pass
        return self.data

    def repo_name(self):
        self.data['repo_name'] = self.xml.ead.eadheader.filedesc.publicationstmt.publisher.contents[0].strip()  # noqa
        return self.data['repo_name']

    def title(self):
        self.data['title'] = self.xml.ead.eadheader.filedesc.titlestmt.titleproper.contents[0].strip()  # noqa
        return self.data['title']

    def unitid(self):
        self.data['unitid'] = self.xml.ead.archdesc.did.unitid.contents[0].strip()  # noqa
        return self.data['unitid']

    def url(self):
        try:
            self.data['url'] = self.xml.ead.eadheader.eadid['url']
        except:
            self.data['url'] = None
        return self.data['url']
