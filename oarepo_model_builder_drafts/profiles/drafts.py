from pathlib import Path
from typing import Union

from oarepo_model_builder.builder import ModelBuilder
from oarepo_model_builder.schema import ModelSchema
from oarepo_model_builder.profiles import Profile


class DraftsProfile(Profile):

    def build(
            self,
            model: ModelSchema,
            output_directory: Union[str, Path],
            builder: ModelBuilder,
    ):
        builder.build(model, output_directory)