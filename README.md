# pairwise_generation

Microservice for SATOSA which generates pairwise-id from an incoming eduPersonTargetedID

SATOSA:
https://github.com/IdentityPython/SATOSA

SAML Subject Identifier Attributes:
https://docs.oasis-open.org/security/saml-subject-id-attr/v1.0/cs01/saml-subject-id-attr-v1.0-cs01.html

Author: Alex Stuart, alex.stuart@jisc.ac.uk

## How to use

- `pairwise_generation.py` should be at `/usr/lib/python3.4/site-packages/satosa/micro_services/pairwise_generation.py`
- `pairwise_generation.yaml` should be at `/etc/satosa/plugins/microservices/pairwise_generation.yaml`
- edit `/etc/satosa/proxy_conf.yaml` to include
```
MICRO_SERVICES:
  - /etc/satosa/plugins/microservices/pairwise_generation.yaml
```
- Internal attributes defined in `/etc/satosa/internal_attributes.yaml` should include
```
  pairwise-id:
    saml: [pairwise-id]
```
- Ensure pairwise-id is in pySAML2 attribute map, for example by updating `/usr/lib/python3.4/site-packages/saml2/attributemaps/saml_uri.py` with changes at https://github.com/IdentityPython/pysaml2/pull/607

## Copyright and License

The contents of this repository are Copyright (C) the named contributors or their
employers, as appropriate.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

> <http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
