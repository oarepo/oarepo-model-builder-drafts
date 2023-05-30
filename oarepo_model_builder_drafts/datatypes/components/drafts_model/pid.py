import re

import marshmallow as ma

from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType
from oarepo_model_builder.datatypes.components import PIDModelComponent
from oarepo_model_builder.datatypes.components.model.pid import PIDSchema
from oarepo_model_builder.datatypes.components.model.utils import set_default
from oarepo_model_builder.utils.python_name import parent_module


class DraftPIDModelComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [PIDModelComponent]

    class ModelSchema(ma.Schema):
        draft_pid = ma.fields.Nested(PIDSchema,
                                     attribute="draft-pid",
                                     data_key="draft-pid",
                                     metadata={"doc": "PID settings"})

    def before_model_prepare(self, datatype, *, context, **kwargs):
        parent = datatype.definition["pid"]

        pid = set_default(datatype, "draft-pid", {})
        pid.setdefault("field-args", ["create=True", "delete=False"])

        for attr, val in parent.items():
            pid.setdefault(attr, val)