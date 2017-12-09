import json
from ProvenanceObject import ProvenanceObject


class Transformation(ProvenanceObject):
    def __init__(self, tag, programs=None, sets=None):
        ProvenanceObject.__init__(self, tag)
        self._programs = programs
        self._sets = sets
        self._json = {}

    def __repr__(self):
        return json.dumps(self._json, indent=2)

    def get_json(self):
        self._json = {'tag': self._tag}
        if (self._programs != None):
            self._json['programs'] = self._programs
        if (self._sets != None):
            self._json['sets'] = self._sets
        return self._json
