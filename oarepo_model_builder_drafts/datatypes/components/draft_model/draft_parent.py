import os

import marshmallow as ma
from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType
from oarepo_model_builder.datatypes.components import (
    RecordMetadataModelComponent,
    RecordModelComponent,
)
from oarepo_model_builder.datatypes.components.model.utils import set_default
from oarepo_model_builder.utils.python_name import module_to_path, parent_module
from oarepo_model_builder.validation.utils import ImportSchema


class DraftParentRecordSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    class_ = ma.fields.Str(
        attribute="class",
        data_key="class",
        metadata={"doc": "Qualified name of the class"},
    )
    base_classes = ma.fields.List(
        ma.fields.Str(),
        attribute="base-classes",
        data_key="base-classes",
        metadata={"doc": "Model base classes"},
    )
    extra_code = ma.fields.Str(
        attribute="extra-code",
        data_key="extra-code",
        metadata={"doc": "Extra code to copy to record file"},
    )
    module = ma.fields.String(metadata={"doc": "Class module"})
    imports = ma.fields.List(
        ma.fields.Nested(ImportSchema), metadata={"doc": "List of python imports"}
    )
    skip = ma.fields.Boolean()
    generate = ma.fields.Boolean()


class DraftParentRecordStateSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    class_ = ma.fields.Str(
        attribute="class",
        data_key="class",
        metadata={"doc": "Qualified name of the class"},
    )
    base_classes = ma.fields.List(
        ma.fields.Str(),
        attribute="base-classes",
        data_key="base-classes",
        metadata={"doc": "Model base classes"},
    )

    imports = ma.fields.List(
        ma.fields.Nested(ImportSchema), metadata={"doc": "List of python imports"}
    )
    module = ma.fields.String(
        metadata={"doc": "Module where the facets will be placed"}
    )
    table = ma.fields.String()
    generate = ma.fields.Boolean()
    skip = ma.fields.Boolean()


class DraftParentRecordMetadataSchema:
    class Meta:
        unknown = ma.RAISE

    class_ = ma.fields.Str(
        attribute="class",
        data_key="class",
        metadata={"doc": "Qualified name of the class"},
    )
    base_classes = ma.fields.List(
        ma.fields.Str(),
        attribute="base-classes",
        data_key="base-classes",
        metadata={"doc": "Model base classes"},
    )

    imports = ma.fields.List(
        ma.fields.Nested(ImportSchema), metadata={"doc": "List of python imports"}
    )
    module = ma.fields.String(
        metadata={"doc": "Module where the facets will be placed"}
    )
    generate = ma.fields.Boolean()
    skip = ma.fields.Boolean()


class DraftParentRecordJsonSchema:
    name = ma.fields.Str(metadata={"doc": "Schema name"})
    module = ma.fields.Str(metadata={"doc": "Schema module"})
    file_ = ma.fields.Str(
        data_key="file", attribute="file", metadata={"doc": "Path to schema file"}
    )
    generate = ma.fields.Boolean()
    skip = ma.fields.Boolean()


class DraftParentComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [RecordModelComponent, RecordMetadataModelComponent]

    class ModelSchema(ma.Schema):
        draft_parent_record = ma.fields.Nested(
            DraftParentRecordSchema,
            attribute="draft-parent-record",
            data_key="draft-parent-record",
            # metadata={"doc": "Service config settings"},
        )
        draft_parent_record_state = ma.fields.Nested(
            DraftParentRecordStateSchema,
            attribute="draft-parent-record-state",
            data_key="draft-parent-record-state",
            # metadata={"doc": "Service config settings"},
        )
        draft_parent_record_metadata = ma.fields.Nested(
            DraftParentRecordMetadataSchema,
            attribute="draft-parent-record-metadata",
            data_key="draft-parent-record-metadata",
            # metadata={"doc": "Service config settings"},
        )
        draft_parent_record_json_schema = ma.fields.Nested(
            DraftParentRecordJsonSchema,
            attribute="draft-parent-record-schema",
            data_key="draft-parent-record-schema",
            # metadata={"doc": "Service config settings"},
        )

    def before_model_prepare(self, datatype, *, context, **kwargs):
        record_module = datatype.definition["record"]["module"]
        metadata_module = datatype.definition["record-metadata"]["module"]
        record_prefix = datatype.definition["module"]["prefix"]
        records_path = module_to_path(
            parent_module(datatype.definition["record"]["module"])
        )

        draft_parent_record = set_default(datatype, "draft-parent-record", {})
        draft_parent_record.setdefault("class", f"{record_module}.DraftParentRecord")
        draft_parent_record.setdefault("base-classes", ["ParentRecord"])
        draft_parent_record.setdefault(
            "imports", [{"import": "invenio_drafts_resources.records.api.ParentRecord"}]
        )
        draft_parent_record.setdefault("module", record_module)
        draft_parent_record.setdefault("generate", True)

        draft_parent_record_state = set_default(
            datatype, "draft-parent-record-state", {}
        )
        draft_parent_record_state.setdefault("class", f"{metadata_module}.ParentState")
        draft_parent_record_state.setdefault(
            "base-classes", ["db.Model", "ParentRecordStateMixin"]
        )
        draft_parent_record_state.setdefault(
            "imports",
            [
                {"import": "invenio_drafts_resources.records.ParentRecordStateMixin"},
                {"import": "invenio_db.db"},
            ],
        )
        draft_parent_record_state.setdefault("module", metadata_module)
        draft_parent_record_state.setdefault("generate", True)
        draft_parent_record_state.setdefault("table", "parent_state_metadata")

        draft_parent_record_metadata = set_default(
            datatype, "draft-parent-record-metadata", {}
        )
        draft_parent_record_metadata.setdefault(
            "class", f"{metadata_module}.DraftParentMetadata"
        )
        draft_parent_record_metadata.setdefault(
            "base-classes", ["db.Model", "RecordMetadataBase"]
        )
        draft_parent_record_metadata.setdefault(
            "imports",
            [
                {"import": "invenio_records.models.RecordMetadataBase"},
                {"import": "invenio_db.db"},
            ],
        )
        draft_parent_record_metadata.setdefault("module", metadata_module)
        draft_parent_record_metadata.setdefault("generate", True)

        json_schema = set_default(datatype, "draft-parent-record-schema", {})
        schema_name = json_schema.setdefault(
            "name",
            f"parent-v1.0.0.json",
        )

        json_schema.setdefault(
            "file", os.path.join(records_path, "jsonschemas", schema_name)
        )
        json_schema.setdefault("generate", True)