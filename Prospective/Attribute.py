import json
from ProvenanceObject import ProvenanceObject

class Attribute(ProvenanceObject):

    def __init__(self, tag, type, extractor = None):
        ProvenanceObject.__init__(self,tag)
        self._type = type
        self._extractor = extractor
        self._json = {}

    def __repr__(self):
        return json.dumps(self._json, indent=2)

    def get_json(self):
        self._json = {'name': self._tag, 'type': self._type}
        if(self._extractor!=None):
            self._json['extractor'] = self._extractor
        return self._json