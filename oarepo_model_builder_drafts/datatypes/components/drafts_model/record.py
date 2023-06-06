from oarepo_model_builder.datatypes import DataTypeComponent
from oarepo_model_builder.datatypes.components import RecordModelComponent
from oarepo_model_builder.datatypes.components.model.utils import set_default
from oarepo_model_builder_drafts.datatypes import DraftDataType
from oarepo_model_builder_drafts.datatypes.components import InvenioDraftsBasesComponent


class DraftRecordModelComponent(DataTypeComponent):
    eligible_datatypes = [DraftDataType]
    affects = [InvenioDraftsBasesComponent]


    def before_model_prepare(self, datatype, *, context, **kwargs):
        draft_record = set_default(datatype, "record", {})
        draft_record.setdefault("base-classes", ["InvenioDraft"])
        draft_record.setdefault(
            "imports",
            [
                {
                    "import": "invenio_drafts_resources.records.api.Draft",
                    "alias": "InvenioDraft",
                }
            ],
        )

