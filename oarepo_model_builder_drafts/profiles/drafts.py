import copy
from pathlib import Path
from typing import Union

from oarepo_model_builder.builder import ModelBuilder
from oarepo_model_builder.conflict_resolvers import AutomaticResolver
from oarepo_model_builder.entrypoints import create_builder_from_entrypoints
from oarepo_model_builder.schema import ModelSchema
from oarepo_model_builder.profiles import Profile

from oarepo_model_builder.utils.hyphen_munch import HyphenMunch
import munch


class DraftsProfile(Profile):

    def build(
            self,
            model: ModelSchema,
            base_model: ModelSchema,
            output_directory: Union[str, Path],
            builder: ModelBuilder,
    ):
        del model.current_model["known-classes"]
        model.schema.drafts = base_model.schema.model
        model.model_field = "drafts"
        builder.build(model, output_directory)