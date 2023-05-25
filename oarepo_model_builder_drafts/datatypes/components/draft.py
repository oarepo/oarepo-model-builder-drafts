import os

import lazy_object_proxy
from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType, DataType
from oarepo_model_builder.datatypes.components import (
    DefaultsModelComponent,
    RecordMetadataModelComponent,
    ServiceModelComponent, RecordModelComponent, PIDModelComponent, MappingModelComponent,
)
from oarepo_model_builder.datatypes.components.model.utils import (
    append_array,
    prepend_array, set_default,
)


class DraftComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    # idea - use this before the first component, so we can use lazy objects to
    # replace any properties set in the previous data structure
    # there's no need to modify the structure
    # dangers - may fail if some components are missing at evaluation
    #         - recursive definitions maybe not possible
    #
    affects = [DefaultsModelComponent]

    def before_model_prepare(self, datatype, *, context, **kwargs):
        if context["profile"] != "drafts":
            return
        parent_record_datatype: DataType = context["parent_record"]
        # model = datatype.definition
        # prefix_snake = model["defaults"]["prefix-snake"]

        # todo perhaps change to dict so only the delete is affected
        pid = set_default(datatype, "pid", {})
        pid.setdefault("field-args", ["create=True", "delete=False"])

        module_container = set_default(datatype, "module", {})


        record_metadata = set_default(datatype, "record-metadata", {})
        record_metadata.setdefault("table",
                        f"{parent_record_datatype.definition['record-metadata']['table']}_drafts")

        record_mappings = set_default(datatype, "record-mappings", {})
        record_mappings.setdefault("short-index-name", lazy_object_proxy.Proxy
        (lambda:
            f"{datatype.definition['module']['prefix-snake']}-draft-{datatype.definition['json-schema-settings']['version']}"
            )
        )


