import os

import lazy_object_proxy

from oarepo_model_builder.model_preprocessors import ModelPreprocessor
from oarepo_model_builder.utils.camelcase import snake_case


class InvenioDraftsDraftModelPreprocessor(ModelPreprocessor):
    TYPE = "invenio_drafts_draft"

    def transform(self, schema, settings):
        model = schema.current_model
        #alternatively record_prefix itself could be edited by adding "Draft" to it, it should work with editing the places where the unedited one is used for now (schema and mapping as far as i'm aware)
        model.setdefault("pid-field-args", ["create=True","delete=False"])
        model.setdefault("record-metadata-table-name", lazy_object_proxy.Proxy(lambda: f"{model.record_prefix.lower()}_metadata_draft"))
        model.setdefault("index-name", lazy_object_proxy.Proxy(lambda: f"{snake_case(model.record_prefix)}-draft-{os.path.basename(model.mapping_file).replace('.json', '')}"))
        model.setdefault("record-class", lazy_object_proxy.Proxy(lambda: f"{model.record_records_package}.api.{model.record_prefix}Draft"))
        model.setdefault("record-metadata-class", lazy_object_proxy.Proxy(lambda: f"{model.record_records_package}.models.{model.record_prefix}DraftMetadata"))
        model.setdefault("record-parent-class", "invenio_drafts_resources.records.api.Draft")
        model.setdefault("record-metadata-parent-class", "invenio_drafts_resources.records.DraftMetadataBase")