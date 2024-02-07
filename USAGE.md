<!-- Start SDK Example Usage [usage] -->
```python
import petstore
from petstore.models import shared

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = shared.Pet(
    name='doggie',
    photo_urls=[
        'string',
    ],
    category=shared.Category(
        id=1,
        name='Dogs',
    ),
    id=10,
    tags=[
        shared.Tag(),
    ],
)

res = s.pet.add_pet_form(req)

if res.pet is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->