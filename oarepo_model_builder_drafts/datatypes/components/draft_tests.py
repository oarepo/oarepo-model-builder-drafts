from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType
from oarepo_model_builder_tests.datatypes.components import ModelTestComponent


class DraftModelTestComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [ModelTestComponent]

    def process_tests(self, datatype, section, **extra_kwargs):
        section.fixtures = {
            "record_service": "record_service",
            "sample_record": "sample_draft",
        }
        section.constants = {
            "read_url": "/draft",
            "update_url": "/draft",
            "delete_url": "/draft",
            "deleted_http_code": 404,
            "skip_search_test": True,
            "service_read_method": "read_draft",
            "service_create_method": "create",
            "service_delete_method": "delete_draft",
            "service_update_method": "update_draft",
            "deleted_record_pid_error": "PIDDoesNotExistError",
            "revision_id1": 2,
            "revision_id2": 5,
            "revision_id3": 8,
            "links": {
                "draft": "https://{site_hostname}/api{BASE_URL}{pid_value}/draft",
                "latest": "https://{site_hostname}/api{BASE_URL}{pid_value}/versions/latest",
                "latest_html": "https://{site_hostname}{BASE_URL}{pid_value}/latest",
                "publish": "https://{site_hostname}/api{BASE_URL}{pid_value}/draft/actions/publish",
                "record": "https://{site_hostname}/api{BASE_URL}{pid_value}",
                "self": "https://{site_hostname}/api{BASE_URL}{pid_value}/draft",
                "self_html": "https://{site_hostname}/uploads/{pid_value}",
                "versions": "https://{site_hostname}/api{BASE_URL}{pid_value}/versions",
            },
            "links_record": {
                "draft": "https://{site_hostname}/api{BASE_URL}{pid_value}/draft",
                "latest": "https://{site_hostname}/api{BASE_URL}{pid_value}/versions/latest",
                "latest_html": "https://{site_hostname}{BASE_URL}{pid_value}/latest",
                "publish": "https://{site_hostname}/api{BASE_URL}{pid_value}/draft/actions/publish",
                "record": "https://{site_hostname}/api{BASE_URL}{pid_value}",
                "self": "https://{site_hostname}/api{BASE_URL}{pid_value}",
                "self_html": "https://{site_hostname}{BASE_URL}{pid_value}",
                "versions": "https://{site_hostname}/api{BASE_URL}{pid_value}/versions",
            },
        }
