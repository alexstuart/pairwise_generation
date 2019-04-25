import base64
import hashlib

from .base import ResponseMicroService

class AddPairwiseAttribute(ResponseMicroService):
    """
    Class to generate pairwise-id from eduPersonTargetedID
    pairwise-id = BASE32( SHA256( entityID of proxied IdP + '!' + opaque part of eduPersonTargetedID ) ) + '@gateway.jisc.ac.uk'
    """
    def __init__(self, config, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def process(self, context, data):
        if len(data.attributes['edupersontargetedid']) > 0:
           n = hashlib.sha256()
           n.update( bytes( data.auth_info.issuer + '!' + data.attributes['edupersontargetedid'][0], 'utf-8' ) )
           p = base64.b32encode(n.digest()).decode() + '@gateway.jisc.ac.uk'
           data.attributes.update({"pairwise-id": [p]})
        return super().process(context, data)
