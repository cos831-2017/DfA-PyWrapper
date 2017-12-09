import json
from ProvenanceObject import ProvenanceObject

class DataCollection(ProvenanceObject):

    def __init__(self, idataset, tag=None):
        ProvenanceObject.__init__(self,tag)
        self._type = type
        self._idataset = idataset
        self._json = {}

    def __repr__(self):
        return json.dumps(self._json, indent=2)

    def get_json(self):
        self._json = {'tag': self._tag, 'type': self._type, 'idataset': self._idataset}
        return self._json