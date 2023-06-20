from oarepo_model_builder.datatypes import DataTypeComponent, ModelDataType, datatypes


class DraftMappingModelComponent(DataTypeComponent):
    def process_mapping(self, datatype, section, **kwargs):
        if self.is_draft_profile: #this will work but idk if it's correct approach
            print() # i'm trying to add the fields to mapping but tbh i have little idea what i'm exactly doing here
            #section.children["expires_at"] = datatypes.get_datatype(self,
            #                                                        {'type': 'datetime',
            #                                                         'sample': {'skip': True},
            #                                                         'marshmallow': {'read': False, 'write': False},
            #                                                         'ui': {
            #                                                            'marshmallow': {'read': False, 'write': False}}
            #                                                         },
            #                                                        "expires_at", datatype.model, datatype.schema)
            #section.children["fork_version_id"] = datatypes.get_datatype(self, v, k, datatype.model, datatype.schema)



    def before_model_prepare(self, datatype, *, context, **kwargs):
        self.is_draft_profile = context["profile"] == "draft"