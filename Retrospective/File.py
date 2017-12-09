import json
from ProvenanceObject import ProvenanceObject

class File(ProvenanceObject):
    def __init__(self, tag, path):
        ProvenanceObject.__init__(self, tag)
        self._path = path
        self._json = {}

    def __repr__(self):
        return json.dumps(self._json, indent=2)

    def get_json(self):
        self._json = {'name': self._tag, 'path': self._path}
        return self._json