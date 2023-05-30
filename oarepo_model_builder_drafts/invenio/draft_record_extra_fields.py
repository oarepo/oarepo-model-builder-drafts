from oarepo_model_builder_drafts.invenio.invenio_drafts_record_extra_fields import InvenioDraftsRecordExtraFieldsBuilder


class DraftExtraFieldsBuilder(InvenioDraftsRecordExtraFieldsBuilder):
    TYPE = "draft_extra_fields"
    section = "draft-record"
    template = "drafts-record-extra-fields"
    record_section = "section_draft_record"
