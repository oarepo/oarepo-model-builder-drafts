from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder


class InvenioDraftsRecordServiceConfigBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_drafts_record_service_config"
    class_config = "record-service-config-class"
    template = "drafts-record-service-config"

