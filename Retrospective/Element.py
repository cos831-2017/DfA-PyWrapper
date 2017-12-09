import json
from ProvenanceObject import ProvenanceObject

class Element(ProvenanceObject):

    def __init__(self, tag, values):
        ProvenanceObject.__init__(self,tag)
        self._values = values
        self._json = {}

    def __repr__(self):
        return json.dumps(self._json, indent=2)

    def get_json(self):
        self._json = {'tag': self._tag, 'values': self._values}
        return self._json