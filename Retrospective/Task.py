import json
from ProvenanceObject import ProvenanceObject


class Task(ProvenanceObject):
    def __init__(self, tag, dataflow_tag, transformation_tag, resource, workspace, status, id, performances=[],
                 output="", error="", sub_id="", invocation="", dependency="", files=[], idatasets = []):
        ProvenanceObject.__init__(self, tag)
        self._id = id
        self._sub_id = sub_id
        self._dataflow_tag = dataflow_tag
        self._transformation_tag = transformation_tag
        self._resource = resource
        self._workspace = workspace
        self._performances = performances
        self._invocation = invocation
        self._status = status
        self._output = output
        self._error = error
        self._dependency = dependency
        self._files = files
        self._idatasets = idatasets
        self._json = {}

    def __repr__(self):
        return json.dumps(self._json, indent=2)

    def get_json(self):
        self._json = {'tag': self._tag, 'id': self._id, 'sub_id': self._sub_id, 'resource': self._resource,
                      'workspace': self._workspace, 'invocation': self._invocation, 'status': self._status,
                      'output': self._output, 'error': self._error, "dataflow": self._dataflow_tag,
                      "transformation": self._transformation_tag, "performances": self._performances,
                      "dependency": self._dependency, "files" : self._files, "sets" : self._idatasets}

        return self._json
