from oarepo_model_builder.datatypes import DataTypeComponent
from oarepo_model_builder.datatypes.components import RecordModelComponent
from oarepo_model_builder.datatypes.components.model.utils import set_default
from oarepo_model_builder.utils.python_name import base_name, split_base_name, split_package_base_name
from oarepo_model_builder_drafts.datatypes import DraftDataType


class DraftRecordModelComponent(RecordModelComponent):
    eligible_datatypes = [DraftDataType]
    dependency_remap = RecordModelComponent


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
        is_record_preset = draft_record.get("class", None)
        super().before_model_prepare(datatype, context=context, **kwargs)
        if not is_record_preset and draft_record["class"][-6:] == "Record":
            draft_record["class"] = draft_record["class"][:-6]


