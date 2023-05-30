from .draft_parent import DraftParentComponent
from .drafts_bases import InvenioDraftsBasesComponent
from .drafts_model import DraftRecordModelComponent, DraftRecordMetadataModelComponent, DraftPIDModelComponent, \
    DraftMappingModelComponent

DRAFT_COMPONENTS = [
    DraftParentComponent,
    InvenioDraftsBasesComponent,
    DraftRecordModelComponent,
    DraftRecordMetadataModelComponent,
    DraftPIDModelComponent,
    DraftMappingModelComponent,
]