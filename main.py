from PDE import PDE

# Prospective Provenance.
dataflow = PDE.dataflow("ok")
transformation = PDE.transformation("dt1")
program = PDE.program("tag", "path")

set = PDE.set("set", PDE.set_type().INPUT.value)
attribute = PDE.attribute("att1", PDE.attribute_type().FILE.value)
extractor = PDE.extractor("ext1", PDE.extractor_cartridge().EXTRACTION.value, PDE.extractor_extension().CSV.value)

attribute._extractor = extractor._tag
set._attributes = [attribute.get_json()]
set._extractors = [extractor.get_json()]

# Set data transformation fiedls.
transformation._programs = [program.get_json()]
transformation._sets = [set.get_json()]

# Set data transformation to dataflow.
dataflow._transformations = [transformation.get_json()]

# Realiza post na api restful do dfa para inserir o dataflow.
PDE.ingest_dataflow_json(dataflow.get_json())

# Retrospective Provenance.
task = PDE.task("t1",dataflow._tag, transformation._tag, "resource", "workspace",PDE.status_type().READY.value, "2")

# Realiza post na api restful do dfa para inserir a task.
PDE.ingest_task_json(task.get_json())