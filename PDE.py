import requests
from Prospective.Dataflow import Dataflow
from Prospective.Program import Program
from Prospective.Set import Set
from Prospective.Extractor import Extractor
from Prospective.Transformation import Transformation
from Prospective.SetType import SetType
from Prospective.Attribute import Attribute
from Prospective.AttributeType import AttributeType
from Prospective.ExtractorCartridge import ExtractorCartridge
from Prospective.ExtractorExtension import ExtractorExtension
from Retrospective.Task import Task
from Retrospective.File import File
from Retrospective.Performance import Performance
from Retrospective.DataCollection import DataCollection
from Retrospective.Element import Element
from Retrospective.IDataset import IDataset
from Retrospective.StatusType import StatusType
from Retrospective.MethodType import MethodType


class PDE(object):
    def __init__(self, configuration=None):
        self._configuration = configuration

    # region ProspectiveProvenance
    @staticmethod
    def dataflow(tag):
        return Dataflow(tag)

    @staticmethod
    def program(name, path):
        return Program(name, path)

    @staticmethod
    def set(tag, type, attributes=None, extractors=None, extractor_combinations=None):
        return Set(tag, type, attributes, extractors, extractor_combinations)

    @staticmethod
    def extractor(tag, cartridge=None, extension=None):
        return Extractor(tag, cartridge, extension)

    @staticmethod
    def transformation(tag, programs=None, sets=None):
        return Transformation(tag, programs, sets)

    @staticmethod
    def attribute(tag, type, extractor=None):
        return Attribute(tag, type, extractor)

    @staticmethod
    def set_type():
        return SetType

    @staticmethod
    def attribute_type():
        return AttributeType

    @staticmethod
    def extractor_cartridge():
        return ExtractorCartridge

    @staticmethod
    def extractor_extension():
        return ExtractorExtension

    # endregion

    # region RetrospectiveProvenance
    @staticmethod
    def task(tag, dataflow_tag, transformation_tag, resource, workspace, status, id, performances=[],
             output=None, error=None, sub_id=None, invocation=None, dependency=None, files=[], idatasets=[]):
        return Task(tag, dataflow_tag, transformation_tag, resource, workspace, status, id, performances, output, error, sub_id,
                    invocation, dependency, files, idatasets)

    @staticmethod
    def file(name, path):
        return File(name, path)

    @staticmethod
    def performance(tag, method_type, start_time, task_id=None, description=None, invocation=None
                    , task_sub_id=None, end_time=None):
        return Performance(tag, description, method_type, invocation, task_id, task_sub_id, start_time, end_time)

    @staticmethod
    def element(tag, values):
        return Element(tag, values)

    @staticmethod
    def idataset(tag, set, elements):
        return IDataset(tag, set, elements)

    @staticmethod
    def data_collection(idataset, tag=None):
        return DataCollection(idataset, tag)

    @staticmethod
    def status_type():
        return StatusType

    @staticmethod
    def method_type():
        return MethodType

    # endregion

    # region RestAPI
    @staticmethod
    def ingest_dataflow_json(base_url, dataflow_json):
        url = base_url + '/pde/dataflow/json'
        r = requests.post(url, json=dataflow_json)
        print(r.status_code)
        print(r.content)

    @staticmethod
    def ingest_task_json(base_url, task_json):
        url = base_url + '/pde/task/json'
        r = requests.post(url, json=task_json)
        print(r.status_code)
        print(r.content)

        # endregion
