from enum import Enum

class MethodType(Enum):
    COMPUTATION = 'COMPUTATION'
    INSTRUMENTATION = 'INSTRUMENTATION'
    EXTRACTION = 'EXTRACTION'
    PROVENANCE = 'PROVENANCE'