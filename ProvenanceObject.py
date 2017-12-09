import json

class ProvenanceObject(object):

    def __init__(self, tag):
        self._tag = tag
        self._json = {}

    def __repr__(self):
        return json.dumps(self._json, indent=2)

    def get_json(self):
        self._json = {'tag': self._tag}
        return self._json