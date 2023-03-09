import marshmallow as ma
from marshmallow import fields
from oarepo_model_builder.validation.model_validation import model_validator


class DraftAddonClasses(ma.Schema):
    drafts_parent_record_class = fields.String(data_key="drafts-parent-record-class", required=False)
    drafts_parent_record_parent_class = fields.String(data_key="drafts-parent-record-parent-class", required=False)
    drafts_parent_record_metadata_class = fields.String(data_key="drafts-parent-record-metadata-class", required=False)
    drafts_parent_state_class = fields.String(data_key="drafts-parent-state-class", required=False)
    drafts_parent_schema_name = fields.String(data_key="drafts-parent-schema-name", required=False)
    drafts_parent_schema_file = fields.String(data_key="drafts-parent-schema-file", required=False)


class DraftsModelSchema(ma.Schema):
    drafts = fields.Nested(lambda: model_validator.validator_class("model")())


validators = {"model": DraftAddonClasses, "root": DraftsModelSchema}
