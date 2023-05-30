from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType, DataType, Import, Section
from oarepo_model_builder.datatypes.components import (
    ServiceModelComponent, RecordModelComponent, ResourceModelComponent, PIDModelComponent,
    RecordMetadataModelComponent,
)
from oarepo_model_builder.datatypes.components.model.utils import (
    append_array,
    prepend_array, set_default,
)
from oarepo_model_builder.datatypes.model import Link


class InvenioDraftsBasesComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    affects = [
        RecordModelComponent,
        RecordMetadataModelComponent,
        ServiceModelComponent,
        ResourceModelComponent,
        PIDModelComponent,
    ]
    """
        links_item = {
        "self": ConditionalLink(
            cond=is_record,
            if_=RecordLink("{+api}/mocks/{id}"),
            else_=RecordLink("{+api}/mocks/{id}/draft"),
        ),
        "self_html": ConditionalLink(
            cond=is_record,
            if_=RecordLink("{+ui}/mocks/{id}"),
            else_=RecordLink("{+ui}/uploads/{id}"),
        ),
        "latest": RecordLink("{+api}/mocks/{id}/versions/latest"),
        "latest_html": RecordLink("{+ui}/mocks/{id}/latest"),
        "draft": RecordLink("{+api}/mocks/{id}/draft", when=is_record),
        "record": RecordLink("{+api}/mocks/{id}", when=is_draft),
        "publish": RecordLink("{+api}/mocks/{id}/draft/actions/publish", when=is_draft),
        "versions": RecordLink("{+api}/mocks/{id}/versions"),
    }
    """
    def process_links(self, datatype, section: Section, **kwargs):
        # add files link item
        section.config.pop("links_search")
        section.config.pop("links_item")
        # remove normal links and add
        # TODO links don't support keywords?
        section.config["links_item"] = [
            #Link(
            #    name="self",
            #    link_class="ConditionalLink",
            #    link_args=['"{self.url_prefix}{id}/files"'],
            #    imports=[Import("invenio_records_resources.services.RecordLink")],
            #),
            #Link(
            #    name="self_html"
            #),
            Link(name="latest",
                 link_class="RecordLink",
                 link_args=['"{+api}/{self.url_prefix}{id}/versions/latest"'],
                 imports=[Import("invenio_records_resources.services.RecordLink")],
            ),
            Link(name="latest_html",
                 link_class="RecordLink",
                 link_args=['"{+ui}/{self.url_prefix}{id}/latest"'],
                 imports=[Import("invenio_records_resources.services.RecordLink")],
                 ),
            Link(name="draft",
                 link_class="RecordLink",
                 link_args=['"{+api}/{self.url_prefix}{id}/draft"'],
                 imports=[Import("invenio_records_resources.services.RecordLink")],
                 ),
            Link(name="record",
                 link_class="RecordLink",
                 link_args=['"{+api}/{self.url_prefix}{id}"'],
                 imports=[Import("invenio_records_resources.services.RecordLink")],
                 ),
            Link(name="publish",
                 link_class="RecordLink",
                 link_args=['"{+api}/{self.url_prefix}{id}/draft/actions/publish"'],
                 imports=[Import("invenio_records_resources.services.RecordLink")],
                 ),
            Link(name="versions",
                 link_class="RecordLink",
                 link_args=['"{+api}/{self.url_prefix}{id}/versions"'],
                 imports=[Import("invenio_records_resources.services.RecordLink")],
                 ),

        ]

    def before_model_prepare(self, datatype, *, context, **kwargs):
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

        record = set_default(datatype, "record", {})
        record.setdefault("imports",
            [
                {
                    "import": "invenio_drafts_resources.records.api.Record",
                    "alias": "InvenioRecord",
                }
            ],
        )

        record_metadata = set_default(datatype, "record-metadata", {})
        record_metadata.setdefault("base-classes", ["db.Model", "RecordMetadataBase", "ParentRecordMixin"])
        record_metadata.setdefault(
            "imports",
            [
                {"import": "invenio_records.models.RecordMetadataBase"},
                {"import": "invenio_db.db"},
                {"import": "invenio_drafts_resources.records.ParentRecordMixin"},
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

