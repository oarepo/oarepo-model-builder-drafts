from oarepo_model_builder.model_preprocessors import ModelPreprocessor

class InvenioDraftsBaseClassesModelPreprocessor(ModelPreprocessor):
    TYPE = "invenio_drafts_base_classes"

    def transform(self, schema, settings):
        self.set_default_and_append_if_not_present(
            schema.current_model,
            "record-metadata-bases",
            [],
            "invenio_drafts_resources.records.ParentRecordMixin"
        )

