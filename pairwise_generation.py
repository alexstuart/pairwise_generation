import base64

from .base import ResponseMicroService

class AddPairwiseAttribute(ResponseMicroService):
    def __init__(self, config, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def process(self, context, data):
        if len(data.attributes['edupersontargetedid']) > 0:
           data.attributes.update({"pairwise-id": [base64.b32encode(bytes(data.attributes['edupersontargetedid'][0], 'utf-8')).decode() + '@gateway.jisc.ac.uk']})
        return super().process(context, data)
