import marshmallow as ma

from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType
from oarepo_model_builder.datatypes.components import DefaultsModelComponent, RecordModelComponent
from oarepo_model_builder.datatypes.components.model.record_metadata import RecordMetadataClassSchema, \
    RecordMetadataModelComponent
from oarepo_model_builder.datatypes.components.model.utils import set_default
from oarepo_model_builder.utils.python_name import parent_module
from oarepo_model_builder.validation.utils import ImportSchema
from oarepo_model_builder_drafts.datatypes import DraftDataType


class DraftRecordMetadataModelComponent(RecordMetadataModelComponent):
    eligible_datatypes = [DraftDataType]
    dependency_remap = RecordMetadataModelComponent


    def before_model_prepare(self, datatype, *, context, **kwargs):
        #todo
        # skip versioning??


        draft_metadata = set_default(datatype, "record-metadata", {})
        draft_metadata.setdefault("base-classes", ["db.Model", "DraftMetadataBase", "ParentRecordMixin"])
        draft_metadata.setdefault(
            "imports",
            [
                {"import": "invenio_drafts_resources.records.DraftMetadataBase"},
                {"import": "invenio_db.db"},
                {"import": "invenio_drafts_resources.records.ParentRecordMixin"},
            ],
        )
        draft_metadata.setdefault("table", f"{context['parent_record'].definition['record-metadata']['table']}_draft")

        super().before_model_prepare(datatype, context=context, **kwargs)