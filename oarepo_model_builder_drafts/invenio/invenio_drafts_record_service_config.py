from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder


class InvenioDraftsRecordServiceConfigBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_drafts_record_service_config"
    section = "service-config"
    template = "drafts-record-service-config"

    def finish(self, **extra_kwargs):
        super().finish(parent_record=self.current_model.parent_record, **extra_kwargs)
