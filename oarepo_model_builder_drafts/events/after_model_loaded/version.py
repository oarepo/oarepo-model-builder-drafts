def add_version_to_metadata(model, **kwargs):
    schema = model.schema["record"]["properties"]
    schema.setdefault("metadata", {}).setdefault("properties", {}).setdefault("version", {"type": "keyword"})