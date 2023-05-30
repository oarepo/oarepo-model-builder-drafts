from oarepo_model_builder.invenio.invenio_record import InvenioRecordBuilder


class InvenioDraftRecordBuilder(InvenioRecordBuilder):
    TYPE = "draft"
    section = "draft-record"
    template = "record"
    record_section = "section_draft_record"
    record_metadata_section = "section_draft_record_metadata"
    pid_section = "section_draft_pid"
    mapping_section = "section_draft_mapping_settings"
