import re

import marshmallow as ma

from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType
from oarepo_model_builder.datatypes.components import PIDModelComponent
from oarepo_model_builder.datatypes.components.model.pid import PIDSchema
from oarepo_model_builder.datatypes.components.model.utils import set_default
from oarepo_model_builder.utils.python_name import parent_module
from oarepo_model_builder_drafts.datatypes import DraftDataType


class DraftPIDModelComponent(PIDModelComponent):
    eligible_datatypes = [DraftDataType]



    def before_model_prepare(self, datatype, *, context, **kwargs):
        pid = set_default(datatype, "pid", {})
        pid.setdefault("field-args", ["create=True", "delete=False"])
        super().before_model_prepare(datatype, context=context, **kwargs)
