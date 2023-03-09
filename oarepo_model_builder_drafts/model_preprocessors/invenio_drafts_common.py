import os

import lazy_object_proxy

from oarepo_model_builder.model_preprocessors import ModelPreprocessor


class InvenioDraftsCommonModelPreprocessor(ModelPreprocessor):
    # shared among the model and drafts profile run
    TYPE = "invenio_drafts_common"

    def transform(self, schema, settings):
        model = schema.current_model

        model.setdefault("pid-field-provider", "DraftRecordIdProviderV2")
        model.setdefault("pid-field-imports", [{"import": "invenio_records_resources.records.systemfields.pid.PIDField"},
                                               {"import": "invenio_records_resources.records.systemfields.pid.PIDFieldContext"},
                                               {"import": "invenio_drafts_resources.records.api.DraftRecordIdProviderV2"}])

        model.setdefault("drafts-parent-state-class", lazy_object_proxy.Proxy(lambda: f"{model.record_records_package}.models.ParentState"))
        model.setdefault("drafts-parent-record-metadata-class",
                         lazy_object_proxy.Proxy(lambda: f"{model.record_records_package}.models.{model.record_prefix}ParentRecordMetadata"))
        model.setdefault("drafts-parent-record-class",
                         lazy_object_proxy.Proxy(lambda: f"{model.record_records_package}.api.{model.record_prefix}ParentRecord"))
        model.setdefault("drafts-parent-schema-name", "parent-v1.0.0.json")
        model.setdefault("drafts-parent-schema-file", lazy_object_proxy.Proxy(lambda: os.path.join(
                model.package_path, "records", "jsonschemas", model.drafts_parent_schema_name
            )))