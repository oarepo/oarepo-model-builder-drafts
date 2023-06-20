from .draft_parent import DraftParentComponent
from .draft import DraftComponent, DraftMetadataComponent
from .draft_model import DraftDefaultsModelComponent, DraftRecordModelComponent, \
    DraftRecordMetadataModelComponent, DraftPIDModelComponent, DraftJSONSchemaModelComponent, DraftMappingModelComponent
from .draft_tests import DraftModelTestComponent

DRAFT_COMPONENTS = [
    DraftParentComponent,
    DraftComponent,
    DraftMetadataComponent,
    DraftRecordModelComponent,
    DraftRecordMetadataModelComponent,
    DraftPIDModelComponent,
    DraftDefaultsModelComponent,
    DraftJSONSchemaModelComponent,
    DraftModelTestComponent,
    DraftMappingModelComponent,
]