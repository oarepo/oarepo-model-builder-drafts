from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder


class InvenioDraftsRecordExtraFieldsBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_drafts_record_extra_fields"
    section = "record"
    template = "drafts-record-extra-fields"