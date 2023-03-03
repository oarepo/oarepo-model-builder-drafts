from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder


class InvenioDraftsParentRecordBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_drafts_parent_record"
    class_config = "drafts-parent-record-class"
    template = "drafts-parent-record"