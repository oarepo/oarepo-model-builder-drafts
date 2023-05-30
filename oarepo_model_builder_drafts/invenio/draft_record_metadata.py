from oarepo_model_builder.invenio.invenio_record_metadata import InvenioRecordMetadataBuilder


class InvenioDraftMetadataBuilder(InvenioRecordMetadataBuilder):
    TYPE = "draft_metadata"
    section = "draft-record-metadata"
    template = "record-metadata"
    record_section = "section_draft_record"
    record_metadata_section = "section_draft_record_metadata"
