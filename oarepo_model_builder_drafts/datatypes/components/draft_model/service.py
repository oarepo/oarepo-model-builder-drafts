from oarepo_model_builder.datatypes import DataType, ModelDataType
from oarepo_model_builder.datatypes.components import ServiceModelComponent
from oarepo_model_builder.datatypes.components.model.utils import set_default


class DraftServiceModelComponent(ServiceModelComponent):
    eligible_datatypes = [ModelDataType]
    dependency_remap = ServiceModelComponent

    def before_model_prepare(self, datatype, *, context, **kwargs):
        if context["profile"] not in {"record", "draft"}:
            return
        record_service = set_default(datatype, "service", {})
        record_service_config = set_default(datatype, "service-config", {})

        if context["profile"] == "draft":
            parent_record_datatype: DataType = context["parent_record"]
            record_service.setdefault(
                "class", parent_record_datatype.definition["service"]["class"]
            )
            record_service_config.setdefault(
                "class", parent_record_datatype.definition["service-config"]["class"]
            )

        if context["profile"] == "record":
            record_service.setdefault(
                "imports",
                [
                    {
                        "import": "invenio_drafts_resources.services.RecordService",
                        "alias": "InvenioRecordService",
                    }
                ],
            )
            record_service_config.setdefault(
                "imports",
                [
                    {
                        "import": "invenio_drafts_resources.services.RecordServiceConfig",
                        "alias": "InvenioRecordServiceConfig",
                    },
                    {
                        "import": "oarepo_runtime.config.service.PermissionsPresetsConfigMixin"
                    },
                ],
            )

        super().before_model_prepare(datatype, context=context, **kwargs)
