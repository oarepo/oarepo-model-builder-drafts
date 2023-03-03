from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder
from oarepo_model_builder.outputs.python import PythonOutput
from oarepo_model_builder.utils.hyphen_munch import HyphenMunch


class InvenioDraftsParentStateBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_drafts_parent_state"
    class_config = "drafts-parent-record-metadata-class"
    template = "drafts-parent-state"

    def process_template(self, python_path, template, **extra_kwargs):
        if self.parent_modules:
            self.create_parent_modules(python_path)
        output: PythonOutput = self.builder.get_output("python", python_path)
        context = HyphenMunch(
            settings=self.settings, current_model=self.current_model, model=self.schema.model, **extra_kwargs
        )
        template = self.call_components(
            "invenio_before_python_template", template, context=context
        )
        output.merge(template, context)