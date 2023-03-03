from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder


class InvenioDraftsParentMetadataBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_drafts_parent_metadata"
    class_config = "drafts-parent-record-metadata-class"
    template = "drafts-parent-metadata"
