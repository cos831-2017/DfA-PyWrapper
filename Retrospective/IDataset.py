import json
from ProvenanceObject import ProvenanceObject

class IDataset(ProvenanceObject):
    def __init__(self, tag, set, elements):
        ProvenanceObject.__init__(self, tag)
        self._set = set
        self._elements = elements
        self._json = {}

    def __repr__(self):
        return json.dumps(self._json, indent=2)

    def get_json(self):
        self._json = {'tag': self._tag, 'set': self._set, 'elements': self._elements}
        return self._json