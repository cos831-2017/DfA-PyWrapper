from enum import Enum

class DataflowType(Enum):
    DATAFLOW = 'DATAFLOW'
    TRANSFORMATION = 'TRANSFORMATION'
    PROGRAM = 'PROGRAM'
    SET = 'SET'
    ATTRIBUTE = 'ATTRIBUTE'
    EXTRACTOR = 'EXTRACTOR'
    TASK = 'TASK'
    FILE = 'FILE'
    FILES = 'FILES'
    PERFORMANCE = 'PERFORMANCE'
    ELEMENT = 'ELEMENT'