import json
from ProvenanceObject import ProvenanceObject

class Extractor(ProvenanceObject):

    def __init__(self, tag, cartridge = None , extension= None):
        ProvenanceObject.__init__(self,tag)
        self._cartridge = cartridge
        self._extension = extension
        self._json = {}

    def __repr__(self):
        return json.dumps(self._json, indent=2)

    def get_json(self):
        self._json = {'tag': self._tag}
        if(self._cartridge!=None):
            self._json['cartridge'] = self._cartridge
        if (self._extension != None):
            self._json['extension'] = self._extension
        return self._json