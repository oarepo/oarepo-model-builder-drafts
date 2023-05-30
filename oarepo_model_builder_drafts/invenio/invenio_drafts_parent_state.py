from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder
from oarepo_model_builder.outputs.python import PythonOutput


class InvenioDraftsParentStateBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_drafts_parent_state"
    section = "draft-parent-record-state"
    template = "drafts-parent-state"