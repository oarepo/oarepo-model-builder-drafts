from oarepo_model_builder.datatypes import (
    DataType,
    DataTypeComponent,
    Import,
    ModelDataType,
    Section,
)
from oarepo_model_builder.datatypes.components import (
    PIDModelComponent,
    RecordModelComponent,
    ResourceModelComponent,
    ServiceModelComponent,
)
from oarepo_model_builder.datatypes.components.model.utils import set_default
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
                    link_args=[
                        "cond=is_record",
                        'if_=RecordLink("{+api}{self.url_prefix}{id}")',
                        'else_=RecordLink("{+api}{self.url_prefix}{id}/draft")',
                    ],
                    imports=[
                        Import("invenio_records_resources.services.ConditionalLink"),
                        Import("invenio_records_resources.services.RecordLink"),
                        Import(
                            "invenio_drafts_resources.services.records.config.is_record"
                        ),
                    ],
                ),
                Link(
                    name="self_html",
                    link_class="ConditionalLink",
                    link_args=[
                        "cond=is_record",
                        'if_=RecordLink("{+ui}{self.url_prefix}{id}")',
                        'else_=RecordLink("{+ui}/uploads/{id}")',
                    ],
                    imports=[
                        Import("invenio_records_resources.services.ConditionalLink"),
                        Import("invenio_records_resources.services.RecordLink"),
                        Import(
                            "invenio_drafts_resources.services.records.config.is_record"
                        ),
                    ],
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
            parent_record_datatype: DataType = context["parent_record"]
            datatype.parent_record = parent_record_datatype

            properties = set_default(datatype, "properties", {})
            for property_key, property_value in parent_record_datatype.definition[
                "properties"
            ].items():  # this should
                properties.setdefault(property_key, property_value)
