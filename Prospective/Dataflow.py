import json
import uuid
from ProvenanceObject import ProvenanceObject

class Dataflow(ProvenanceObject):

    def __init__(self, tag, transformations = None):
        ProvenanceObject.__init__(self,tag)
        self._transformations = transformations
        self._json = {}

    def __repr__(self):
        return json.dumps(self._json, indent=2)

    def get_json(self):
        self._json = {'tag': self._tag}
        if(self._transformations!=None):
            self._json['transformations'] = self._transformations
        return self._json