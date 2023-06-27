from oarepo_model_builder.datatypes.components import DefaultsModelComponent
from oarepo_model_builder.datatypes.components.model.utils import set_default

from oarepo_model_builder_drafts.datatypes import DraftDataType


class DraftDefaultsModelComponent(DefaultsModelComponent):
    eligible_datatypes = [DraftDataType]
    dependency_remap = DefaultsModelComponent

    def before_model_prepare(self, datatype, *, context, **kwargs):
        parent = context["parent_record"]
        set_default(datatype, "model-name", parent.definition["model-name"])
        module_container = set_default(datatype, "module", {})
        module_container.setdefault(
            "prefix", f"{parent.definition['module']['prefix']}Draft"
        )

        super().before_model_prepare(datatype, context=context, **kwargs)
