from oarepo_model_builder.invenio.invenio_record import InvenioRecordBuilder


class InvenioDraftRecordBuilder(InvenioRecordBuilder):
    TYPE = "draft"
    section = "draft-record"
    template = "record"
    section_remap = {"record": "section_draft_record",
                     "record_metadata": "section_draft_record_metadata",
                     "pid": "section_draft_pid",
                     "mapping_settings": "section_draft_mapping_settings",
                     }
