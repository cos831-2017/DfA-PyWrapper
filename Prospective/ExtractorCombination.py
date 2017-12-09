import json
from ProvenanceObject import ProvenanceObject

class ExtractorCombination(ProvenanceObject):

    def __init__(self, outer, inner,tag = ""):
        ProvenanceObject.__init__(self,tag)
        self._outer = outer
        self._inner = inner
        self._json = {}

    def __repr__(self):
        return json.dumps(self._json, indent=2)

    def get_json(self):
        self._json = {'tag': self._tag, 'outer': self._outer, 'inner': self._inner}
        return self._json