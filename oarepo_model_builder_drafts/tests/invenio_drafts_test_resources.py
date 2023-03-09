from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder
from oarepo_model_builder.outputs.python import PythonOutput
from oarepo_model_builder.utils.hyphen_munch import HyphenMunch


class InvenioDraftsTestResourcesBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_drafts_test_resources"
    template = "drafts-test-resources"
    MODULE = "tests.test_resources"

    def finish(self, **extra_kwargs):
        module = self.MODULE
        python_path = self.module_to_path(module)

        self.process_template(
            python_path,
            self.template,
            current_package_name=module,
            **extra_kwargs,
        )
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