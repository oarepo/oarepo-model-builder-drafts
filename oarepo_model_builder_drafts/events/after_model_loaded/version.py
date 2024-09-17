def add_version_to_metadata(model, **kwargs):
    schema = model.schema["record"]["properties"]
    if "metadata" not in schema:
        return
    schema["metadata"].setdefault("properties", {}).setdefault("version", {"type": "keyword"})