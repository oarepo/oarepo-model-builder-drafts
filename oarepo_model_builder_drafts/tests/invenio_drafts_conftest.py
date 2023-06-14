from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder
from oarepo_model_builder.outputs.python import PythonOutput


class InvenioDraftsConftestBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_drafts_conftest"
    template = "drafts-conftest"
    MODULE = "tests.conftest"

    def _get_output_module(self):
        return f'{self.current_model.definition["tests"]["module"]}.conftest'

    def finish(self, **extra_kwargs):
        tests = getattr(self.current_model, "section_tests")
        super().finish(fixtures=tests.fixtures, test_constants=tests.constants, **extra_kwargs)