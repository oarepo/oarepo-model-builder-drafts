from oarepo_model_builder.builders.json_base import JSONBaseBuilder
from oarepo_model_builder.builders.jsonschema import JSONSchemaBuilder
from oarepo_model_builder.stack import ModelBuilderStack


class JSONSchemaDraftsParentBuilder(JSONSchemaBuilder):
    TYPE = "jsonschema_drafts_parent"
    output_file_type = "jsonschema"
    output_file_name = "drafts-parent-schema-file"
    parent_module_root_name = "jsonschemas"

    def begin(self, schema, settings):
        super().begin(schema, settings)
        target_json = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "$id": f"{schema.current_model.schema_server}{schema.current_model.drafts_parent_schema_name}",
            "type": "object",
            "properties": {
                "id": {
                    "type": "string"
                }
            }
        }
        self.stack = ModelBuilderStack()
        self.stack.push(None, target_json)
