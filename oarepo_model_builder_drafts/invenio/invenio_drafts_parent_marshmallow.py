from pathlib import Path

from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder
from oarepo_model_builder.utils.python_name import module_to_path


class InvenioDraftsParentMarshmallowBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_drafts_parent_marshmallow"
    section = "marshmallow"
    template = "drafts-parent-marshmallow"


