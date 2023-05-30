import marshmallow as ma

from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType
from oarepo_model_builder.datatypes.components import DefaultsModelComponent, RecordModelComponent
from oarepo_model_builder.datatypes.components.model.record_metadata import RecordMetadataClassSchema, \
    RecordMetadataModelComponent
from oarepo_model_builder.datatypes.components.model.utils import set_default
from oarepo_model_builder.utils.python_name import parent_module
from oarepo_model_builder.validation.utils import ImportSchema

class DraftRecordMetadataModelComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [DefaultsModelComponent, RecordMetadataModelComponent]

    class ModelSchema(ma.Schema):
        draft_record_metadata = ma.fields.Nested(
            RecordMetadataClassSchema,
            attribute="draft-record-metadata",
            data_key="draft-record-metadata",
            metadata={"doc": "Record metadata settings"},
        )

    def before_model_prepare(self, datatype, **kwargs):
        #todo
        # skip versioning??
        parent = datatype.definition["record-metadata"]
        records_module = parent_module(datatype.definition["record"]["module"])
        prefix = datatype.definition["module"]["prefix"]
        alias = datatype.definition["module"]["alias"]

        draft_metadata = set_default(datatype, "draft-record-metadata", {})
        metadata_module = draft_metadata.setdefault("module", f"{records_module}.models")
        draft_metadata.setdefault("class", f"{metadata_module}.{prefix}DraftMetadata")
        draft_metadata.setdefault("base-classes", ["db.Model", "DraftMetadataBase", "ParentRecordMixin"])
        draft_metadata.setdefault(
            "imports",
            [
                {"import": "invenio_drafts_resources.records.DraftMetadataBase"},
                {"import": "invenio_db.db"},
                {"import": "invenio_drafts_resources.records.ParentRecordMixin"},
            ],
        )
        draft_metadata.setdefault("table", f"{parent['table']}_draft")

        for attr, val in parent.items():
            draft_metadata.setdefault(attr, val)