from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType, DataType
from oarepo_model_builder.datatypes.components import (
    DefaultsModelComponent,
    RecordMetadataModelComponent,
    ServiceModelComponent, RecordModelComponent, ResourceModelComponent, PIDModelComponent,
)
from oarepo_model_builder.datatypes.components.model.utils import (
    append_array,
    prepend_array, set_default,
)

from oarepo_model_builder_tests.datatypes.components import ModelTestComponent

class InvenioDraftsBasesComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [ModelTestComponent]
    affects = [
        RecordModelComponent,
        ServiceModelComponent,
        ResourceModelComponent,
        PIDModelComponent,
    ]

    def before_model_prepare(self, datatype, *, context, **kwargs):
        pid = set_default(datatype, "pid", {})
        pid.setdefault("provider-base-classes", ["DraftIdProviderV2"])
        pid.setdefault(
            "imports",
            [
                {
                    "import": "invenio_records_resources.records.systemfields.pid.PIDField"
                },
                {
                    "import": "invenio_records_resources.records.systemfields.pid.PIDFieldContext"
                },
                {"import": "invenio_drafts_resources.records.api.DraftRecordIdProviderV2"},
            ],
        )


        if context["profile"] == "record":
            record = set_default(datatype, "record", {})
            record.setdefault("imports",
                [
                    {
                        "import": "invenio_drafts_resources.records.api.Record",
                        "alias": "InvenioRecord",
                    }
                ],
            )

            record_resource = set_default(datatype, "record-resource", {})
            record_resource.setdefault(
                "imports",
                [{"import": "invenio_drafts_resources.resources.RecordResource"}],
            )

            record_resource_config = set_default(datatype, "record-resource-config", {})
            record_resource_config.setdefault(
                "imports",
                [{"import": "invenio_drafts_resources.resources.RecordResourceConfig"}],
            )

            record_service = set_default(datatype, "record-service", {})
            record_service.setdefault(
                "imports",
                [
                    {
                        "import": "invenio_drafts_resources.services.RecordService",
                        "alias": "InvenioRecordService",
                    }
                ],
            )

            record_service_config = set_default(datatype, "record-service-config", {})
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



        if context["profile"] == "drafts":
            parent_record_datatype: DataType = context["parent_record"]

            record = set_default(datatype, "record", {})
            record.setdefault("class",
                              f"{parent_record_datatype.definition['record']['class']}Draft")
            record.setdefault("base-classes", ["InvenioDraft"])
            record.setdefault(
                "imports",
                [
                    {
                        "import": "invenio_drafts_resources.records.api.Draft",
                        "alias": "InvenioDraft",
                    }
                ],
            )

            record_metadata = set_default(datatype, "record-metadata", {})
            record_metadata.setdefault("class",
                                       f"{parent_record_datatype.definition['record-metadata']['class']}Draft")
            record_metadata.setdefault("base-classes", ["db.Model", "DraftMetadataBase"])
            record_metadata.setdefault(
                "imports",
                [
                    {"import": "invenio_drafts_resources.records.DraftMetadataBase"},
                    {"import": "invenio_db.db"},
                ],
            )

