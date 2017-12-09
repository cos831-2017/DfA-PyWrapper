import json
from ProvenanceObject import ProvenanceObject


class Set(ProvenanceObject):
    def __init__(self, tag, type, attributes=None, extractors=None, extractor_combinations=None):
        ProvenanceObject.__init__(self, tag)
        self._type = type
        self._attributes = attributes
        self._extractors = extractors
        self._extractor_combinations = extractor_combinations
        self._json = {}

    def __repr__(self):
        return json.dumps(self._json, indent=2)

    def get_json(self):
        self._json = {'tag': self._tag, 'type': self._type}
        if (self._attributes != None):
            self._json['attributes'] = self._attributes
        if (self._extractors != None):
            self._json['extractors'] = self._extractors
        if (self._extractor_combinations != None):
            self._json['extractor.combination'] = self._extractor_combinations
        return self._json
