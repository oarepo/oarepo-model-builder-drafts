from pathlib import Path
from typing import Union, List

from oarepo_model_builder.builder import ModelBuilder
from oarepo_model_builder.profiles.record import RecordProfile
from oarepo_model_builder.schema import ModelSchema
from oarepo_model_builder.utils.dict import dict_get

class DraftsProfile(RecordProfile):
    default_model_path = ["record", "drafts"]

    def build(
        self,
        model: ModelSchema,
        profile: str,
        model_path: List[str],
        output_directory: Union[str, Path],
        builder: ModelBuilder,
        **kwargs,
    ):
        parent_record = model.get_schema_section("record", model_path[:-1])

        draft_profile = dict_get(model.schema, model_path)
        draft_profile["type"] = "draft_record"

        # pass the parent record as an extra context item. This will be handled by file-aware
        # components in their "prepare" method
        super().build(
            model=model,
            profile=profile,
            model_path=model_path,
            output_directory=output_directory,
            builder=builder,
            context={
                "profile": "drafts",
                "profile_module": "records",
                "parent_record": parent_record,
            },
        )
