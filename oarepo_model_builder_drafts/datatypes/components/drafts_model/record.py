import marshmallow as ma

from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType
from oarepo_model_builder.datatypes.components import DefaultsModelComponent, RecordModelComponent
from oarepo_model_builder.datatypes.components.model.record import RecordClassSchema
from oarepo_model_builder.datatypes.components.model.utils import set_default

class DraftRecordModelComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [DefaultsModelComponent, RecordModelComponent]

    class ModelSchema(ma.Schema):
        draft_record = ma.fields.Nested(
            RecordClassSchema,
            attribute="draft-record",
            data_key="draft-record",
            metadata={"doc": "api/Record settings"}
        )

    def before_model_prepare(self, datatype, *, context, **kwargs):
        parent = datatype.definition["record"]
        module = datatype.definition["module"]["qualified"]
        profile_module = context["profile_module"]
        record_prefix = datatype.definition["module"]["prefix"]

        draft_record = set_default(datatype, "draft-record", {})
        records_module = draft_record.setdefault("module", f"{module}.{profile_module}.api")
        draft_record.setdefault("class",
                                f"{records_module}.{record_prefix}Draft")
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
        draft_record.setdefault("generate", True)
        for attr, val in parent.items():
            draft_record.setdefault(attr, val)

        #convert_config_to_qualified_name(record)