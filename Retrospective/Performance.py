import json
from ProvenanceObject import ProvenanceObject


class Performance(ProvenanceObject):
    def __init__(self, tag, method_type, start_time, task_id=None, description=None, invocation=None
                 , task_sub_id=None, end_time=None):
        ProvenanceObject.__init__(self, tag)
        self._description = description
        self._method_type = method_type
        self._invocation = invocation
        self._task_id = task_id
        self._task_sub_id = task_sub_id
        self._start_time = start_time
        self._end_time = end_time
        self._json = {}

    def __repr__(self):
        return json.dumps(self._json, indent=2)

    def get_json(self):
        self._json = {'description': self._description, 'method': self._method_type,
                      'startTime': self._start_time, 'endTime': self._end_time}
        return self._json
