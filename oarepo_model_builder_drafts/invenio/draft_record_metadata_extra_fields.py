from oarepo_model_builder_drafts.invenio.invenio_drafts_record_metadata_extra_fields import \
    InvenioDraftsRecordMetadataExtraFieldsBuilder


class DraftMetadataExtraFieldsBuilder(InvenioDraftsRecordMetadataExtraFieldsBuilder):
    TYPE = "draft_metadata_extra_fields"
    section = "draft-record-metadata"
    template = "drafts-record-metadata-extra-fields"
    record_metadata_section = "section_draft_record_metadata"
