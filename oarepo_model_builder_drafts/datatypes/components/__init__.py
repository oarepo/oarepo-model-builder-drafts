#from .draft_parent import DraftParentComponent
#from .drafts_bases import InvenioDraftsBasesComponent
from .draft_parent import DraftParentComponent
from .drafts_bases import InvenioDraftsBasesComponent
from .drafts_model import DraftDefaultsModelComponent, DraftMappingModelComponent, DraftRecordModelComponent, \
    DraftRecordMetadataModelComponent, DraftPIDModelComponent, DraftJSONSchemaModelComponent

DRAFT_COMPONENTS = [
    DraftParentComponent,
    InvenioDraftsBasesComponent,
    DraftRecordModelComponent,
    DraftRecordMetadataModelComponent,
    DraftPIDModelComponent,
    DraftMappingModelComponent,
    DraftDefaultsModelComponent,
    DraftJSONSchemaModelComponent,
]