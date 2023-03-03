from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder


class InvenioDraftsRecordMetadataExtraFieldsBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_drafts_record_metadata_extra_fields"
    class_config = "record-metadata-class"
    template = "drafts-record-metadata-extra-fields"
