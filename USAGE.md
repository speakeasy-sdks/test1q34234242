<!-- Start SDK Example Usage -->


```python
import petstore
from petstore.models import shared

s = petstore.Petstore(
    petstore_auth="",
)

req = shared.Pet(
    category=shared.Category(
        id=1,
        name='Dogs',
    ),
    id=10,
    name='doggie',
    photo_urls=[
        'string',
    ],
    tags=[
        shared.Tag(),
    ],
)

res = s.pet.add_pet_form(req)

if res.pet is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->