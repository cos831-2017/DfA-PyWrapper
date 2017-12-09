import json
from ProvenanceObject import ProvenanceObject

class ExecuteDataflow(ProvenanceObject):

    def __init__(self, tag, version, dataflow):
        ProvenanceObject.__init__(self,tag)
        self._version = version
        self._dataflow = dataflow
        self._json = {}

    def __repr__(self):
        return json.dumps(self._json, indent=2)

    def get_json(self):
        self._json = {'tag': self._tag, 'version': self._version, 'dataflow': self._dataflow}
        return self._json