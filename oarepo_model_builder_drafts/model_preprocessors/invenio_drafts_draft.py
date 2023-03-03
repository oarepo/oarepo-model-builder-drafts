import os

from oarepo_model_builder.model_preprocessors import ModelPreprocessor
from oarepo_model_builder.utils.camelcase import snake_case


class InvenioDraftsDraftModelPreprocessor(ModelPreprocessor):
    TYPE = "invenio_drafts_draft"

    def transform(self, schema, settings):
        drafts_model = schema.current_model
        base_model = schema.schema.model


        record_prefix = base_model.record_prefix

        drafts_model.setdefault("profile-package", base_model.profile_package)
        drafts_model.setdefault("record-records-package", base_model.record_records_package)
        drafts_model.setdefault("record-metadata-table-name", f"{base_model.record_metadata_table_name}_drafts")
        ### TODO ??? ask
        #drafts_model.setdefault("mapping-file", os.path.join(
        #        base_model.package_path,
        #        "records",
        #        "mappings",
        #        "os-v2",
        #        snake_case(model.record_prefix),
        #        model.schema_name,
        #    ),
        #)

        drafts_model.setdefault("record-class", f"{base_model.record_records_package}.api.{record_prefix}Draft")
        drafts_model.setdefault("record-metadata-class", f"{base_model.record_records_package}.models.{record_prefix}DraftMetadata")
        drafts_model.setdefault("record-parent-class", "invenio_drafts_resources.records.api.Draft")
        drafts_model.setdefault("record-metadata-parent-class", "invenio_drafts_resources.records.DraftMetadataBase")


