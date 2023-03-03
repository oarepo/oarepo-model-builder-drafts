from oarepo_model_builder.model_preprocessors import ModelPreprocessor


class InvenioDraftsCommonModelPreprocessor(ModelPreprocessor):
    # shared among the model and drafts profile run
    TYPE = "invenio_drafts_common"

    def transform(self, schema, settings):
        base_model = schema.schema.model
        cur_model = schema.current_model


        cur_model.setdefault("drafts-parent-state-class", f"{base_model.record_records_package}.models.ParentState")
        cur_model.setdefault("drafts-parent-record-metadata-class",
                         f"{base_model.record_records_package}.models.{base_model.record_prefix}ParentRecordMetadata")
        cur_model.setdefault("drafts-parent-record-class",
                         f"{base_model.record_records_package}.api.{base_model.record_prefix}ParentRecord")