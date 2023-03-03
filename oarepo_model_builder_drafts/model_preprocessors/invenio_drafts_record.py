from oarepo_model_builder.model_preprocessors import ModelPreprocessor

class InvenioDraftsRecordModelPreprocessor(ModelPreprocessor):
    TYPE = "invenio_drafts_records"

    def transform(self, schema, settings):
        model = schema.current_model

        model.setdefault("drafts-parent-record-parent-class",
                         "invenio_drafts_resources.records.api.ParentRecord")
        model.setdefault("record-resource-parent-class", "invenio_drafts_resources.resources.RecordResource")
        model.setdefault("record-resource-config-parent-class", "invenio_drafts_resources.resources.RecordResourceConfig")
        model.setdefault("record-service-parent-class", "invenio_drafts_resources.services.RecordService")
        model.setdefault("record-service-config-parent-class", "invenio_drafts_resources.services.RecordServiceConfig")
        model.setdefault("record-parent-class", "invenio_drafts_resources.records.api.Record")