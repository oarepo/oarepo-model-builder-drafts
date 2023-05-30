from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder
from oarepo_model_builder.outputs.python import PythonOutput


class InvenioDraftsTestResourcesBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_drafts_test_resources"
    template = "drafts-test-resources"
    MODULE = "tests.test_resources"

    def _get_output_module(self):
        return f'{self.current_model.definition["tests"]["module"]}.test_resource'
