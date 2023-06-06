import os

import marshmallow as ma

from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType
from oarepo_model_builder.datatypes.components import MappingModelComponent
from oarepo_model_builder.datatypes.components.model.mapping import ModelMappingSchema
from oarepo_model_builder.datatypes.components.model.utils import set_default
from oarepo_model_builder.utils.python_name import module_to_path, parent_module
from oarepo_model_builder_drafts.datatypes import DraftDataType


class DraftMappingModelComponent(MappingModelComponent):
    eligible_datatypes = [DraftDataType]
    dependency_remap = MappingModelComponent


    def before_model_prepare(self, datatype, *, context, **kwargs):
        prefix_snake = datatype.definition["module"]["prefix-snake"]
        alias = datatype.definition["module"]["alias"]

        records_path = module_to_path(
            parent_module(datatype.definition["record"]["module"])
        )

        mapping = set_default(datatype, "mapping-settings", {})

        short_index_name = (
            f"{prefix_snake}-draft-{datatype.definition['json-schema-settings']['version']}"
        )
        mapping.setdefault(
            "index",
            f"{datatype.definition['module']['alias']}-{short_index_name}",
        )
        mapping.setdefault(
            "file",
            os.path.join(
                records_path,
                "mappings",
                "os-v2",
                alias,
                f"{short_index_name}.json",
            ),
        )

        super().before_model_prepare(datatype, context=context, **kwargs)