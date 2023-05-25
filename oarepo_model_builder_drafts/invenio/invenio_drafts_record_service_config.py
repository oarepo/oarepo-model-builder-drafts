from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder


class InvenioDraftsRecordServiceConfigBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_drafts_record_service_config"
    section = "record-service-config"
    template = "drafts-record-service-config"

