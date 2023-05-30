import os

import marshmallow as ma

from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType
from oarepo_model_builder.datatypes.components import MappingModelComponent
from oarepo_model_builder.datatypes.components.model.mapping import ModelMappingSchema
from oarepo_model_builder.datatypes.components.model.utils import set_default
from oarepo_model_builder.utils.python_name import module_to_path, parent_module

class DraftMappingModelComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [
        MappingModelComponent,
    ]

    class ModelSchema(ma.Schema):
        draft_mapping = ma.fields.Nested(
            ModelMappingSchema,
            attribute="draft-mapping-settings",
            data_key="draft-mapping-settings",
            metadata={"doc": "Mapping definition"},
        )
        searchable = ma.fields.Bool(
            load_default=True,
            metadata={
                "doc": "Will the mapping/indexing be generated on model? (can be overriden on individual properties)"
            },
        )

    def before_model_prepare(self, datatype, **kwargs):
        parent = datatype.definition["mapping-settings"]
        prefix_snake = datatype.definition["module"]["prefix-snake"]
        alias = datatype.definition["module"]["alias"]
        records_path = module_to_path(
            parent_module(datatype.definition["record"]["module"])
        )

        mapping = set_default(datatype, "draft-mapping-settings", {})
        mapping.setdefault("generate", True)
        alias = mapping.setdefault("alias", alias)
        mapping.setdefault(
            "module",
            f'{parent_module(datatype.definition["record"]["module"])}.mappings',
        )
        short_index_name = (
            f"{prefix_snake}-draft-{datatype.definition['json-schema-settings']['version']}"
        )
        mapping.setdefault(
            "index",
            f"{alias}-{short_index_name}",
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

        for attr, val in parent.items():
            mapping.setdefault(attr, val)