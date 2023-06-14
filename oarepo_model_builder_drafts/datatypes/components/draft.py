from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType, DataType, Import, Section
from oarepo_model_builder.datatypes.components import (
    ServiceModelComponent, RecordModelComponent, ResourceModelComponent, PIDModelComponent,
    RecordMetadataModelComponent,
)
from oarepo_model_builder.datatypes.components.model.utils import (
    append_array,
    prepend_array, set_default, place_after,
)
from oarepo_model_builder.datatypes.model import Link


class DraftComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    affects = [
        RecordModelComponent,
        ServiceModelComponent,
        ResourceModelComponent,
        PIDModelComponent,
    ]

    def process_links(self, datatype, section: Section, **kwargs):
        # add files link item
        if self.is_record_profile:
            if "links_search" in section.config:
                section.config.pop("links_search")
            for link in section.config["links_item"]:
                if link.name == "self":
                    section.config["links_item"].remove(link)
                    break
            section.config["links_item"] += [
                Link(
                    name="self",
                    link_class="ConditionalLink",
                    link_args=['cond=is_record',
                               'if_=RecordLink("{+api}{self.url_prefix}{id}")',
                               'else_=RecordLink("{+api}{self.url_prefix}{id}/draft")',],
                    imports=[Import("invenio_records_resources.services.ConditionalLink"),
                             Import("invenio_records_resources.services.RecordLink"),
                             Import("invenio_drafts_resources.services.records.config.is_record"),],
                ),
                Link(
                    name="self_html",
                    link_class="ConditionalLink",
                    link_args=['cond=is_record',
                               'if_=RecordLink("{+ui}{self.url_prefix}{id}")',
                               'else_=RecordLink("{+ui}/uploads/{id}")',], #todo this is prob not correct??, are the links in general correct?? like, url prefix contains pid value which is {id}?
                    imports=[Import("invenio_records_resources.services.ConditionalLink"),
                             Import("invenio_records_resources.services.RecordLink"),
                             Import("invenio_drafts_resources.services.records.config.is_record"),],
                ),
                Link(
                     name="latest",
                     link_class="RecordLink",
                     link_args=['"{+api}/{self.url_prefix}{id}/versions/latest"'],
                     imports=[Import("invenio_records_resources.services.RecordLink")],
                ),
                Link(
                     name="latest_html",
                     link_class="RecordLink",
                     link_args=['"{+ui}/{self.url_prefix}{id}/latest"'],
                     imports=[Import("invenio_records_resources.services.RecordLink")],
                ),
                Link(
                     name="draft",
                     link_class="RecordLink",
                     link_args=['"{+api}/{self.url_prefix}{id}/draft"'],
                     imports=[Import("invenio_records_resources.services.RecordLink")],
                     ),
                Link(
                     name="record",
                     link_class="RecordLink",
                     link_args=['"{+api}/{self.url_prefix}{id}"'],
                     imports=[Import("invenio_records_resources.services.RecordLink")],
                     ),
                Link(
                     name="publish",
                     link_class="RecordLink",
                     link_args=['"{+api}/{self.url_prefix}{id}/draft/actions/publish"'],
                     imports=[Import("invenio_records_resources.services.RecordLink")],
                     ),
                Link(
                     name="versions",
                     link_class="RecordLink",
                     link_args=['"{+api}/{self.url_prefix}{id}/versions"'],
                     imports=[Import("invenio_records_resources.services.RecordLink")],
                     ),

        ]

    def before_model_prepare(self, datatype, *, context, **kwargs):
        self.is_draft_profile = context["profile"] == "draft"
        self.is_record_profile = context["profile"] == "record"
        if self.is_draft_profile:
            #todo ask if is it ok to use definition on this level
            parent_record_datatype: DataType = context["parent_record"]
            datatype.parent_record = parent_record_datatype

            record_service = set_default(datatype, "service", {})
            record_resource = set_default(datatype, "resource", {})
            record_service_config = set_default(datatype, "service-config", {})
            record_resource_config = set_default(datatype, "resource-config", {})

            record_service.setdefault("class", parent_record_datatype.definition["service"]["class"])
            record_resource.setdefault("class", parent_record_datatype.definition["resource"]["class"])
            record_service_config.setdefault("class", parent_record_datatype.definition["service-config"]["class"])
            record_resource_config.setdefault("class", parent_record_datatype.definition["resource-config"]["class"])



        pid = set_default(datatype, "pid", {})
        pid.setdefault("provider-base-classes", ["DraftRecordIdProviderV2"])
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

            record_resource = set_default(datatype, "resource", {})
            record_resource.setdefault(
                "imports",
                [{"import": "invenio_drafts_resources.resources.RecordResource"}],
            )

            record_resource_config = set_default(datatype, "resource-config", {})
            record_resource_config.setdefault(
                "imports",
                [{"import": "invenio_drafts_resources.resources.RecordResourceConfig"}],
            )

            record_service = set_default(datatype, "service", {})
            record_service.setdefault(
                "imports",
                [
                    {
                        "import": "invenio_drafts_resources.services.RecordService",
                        "alias": "InvenioRecordService",
                    }
                ],
            )

            record_service_config = set_default(datatype, "service-config", {})
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

class DraftMetadataComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [RecordMetadataModelComponent]

    def before_model_prepare(self, datatype, *, context, **kwargs):
        # todo hierarchical profiles would hypothetically be useful here, I want to run this on all record-like profiles but no files-like profiles
        # todo i guess it's bad to reference other profiles here
        # todo it's also problematic to set it here, the profile is not unsetting itself
        if context["profile"] == "record" or context["profile"] == "draft":
            place_after(
                datatype,
                "record-metadata",
                "base-classes",
                "RecordMetadataBase",
                "ParentRecordMixin",
            )
            append_array(
                datatype,
                "record-metadata",
                "imports",
                {"import": "invenio_drafts_resources.records.ParentRecordMixin"},
            )

