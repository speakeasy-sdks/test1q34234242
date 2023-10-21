# Pet
(*pet*)

## Overview

Everything about your Pets

Find out more
<http://swagger.io>
### Available Operations

* [add_pet_form](#add_pet_form) - Add a new pet to the store
* [add_pet_json](#add_pet_json) - Add a new pet to the store
* [add_pet_raw](#add_pet_raw) - Add a new pet to the store
* [delete_pet](#delete_pet) - Deletes a pet
* [find_pets_by_status](#find_pets_by_status) - Finds Pets by status
* [find_pets_by_tags](#find_pets_by_tags) - Finds Pets by tags
* [get_pet_by_id](#get_pet_by_id) - Find pet by ID
* [update_pet_with_form](#update_pet_with_form) - Updates a pet in the store with form data
* [update_pet_form](#update_pet_form) - Update an existing pet
* [update_pet_json](#update_pet_json) - Update an existing pet
* [update_pet_raw](#update_pet_raw) - Update an existing pet
* [upload_file](#upload_file) - uploads an image

## add_pet_form

Add a new pet to the store

### Example Usage

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

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [shared.Pet](../../models/shared/pet.md)   | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.AddPetFormResponse](../../models/operations/addpetformresponse.md)**


## add_pet_json

Add a new pet to the store

### Example Usage

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

res = s.pet.add_pet_json(req)

if res.pet is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [shared.Pet](../../models/shared/pet.md)   | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.AddPetJSONResponse](../../models/operations/addpetjsonresponse.md)**


## add_pet_raw

Add a new pet to the store

### Example Usage

```python
import petstore
from petstore.models import shared

s = petstore.Petstore(
    petstore_auth="",
)

req = 'W`6wC8ntZ\'.encode()

res = s.pet.add_pet_raw(req)

if res.pet is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [bytes](../../models//.md)                 | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.AddPetRawResponse](../../models/operations/addpetrawresponse.md)**


## delete_pet

Deletes a pet

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore(
    petstore_auth="",
)

req = operations.DeletePetRequest(
    pet_id=441876,
)

res = s.pet.delete_pet(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.DeletePetRequest](../../models/operations/deletepetrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.DeletePetResponse](../../models/operations/deletepetresponse.md)**


## find_pets_by_status

Multiple status values can be provided with comma separated strings

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore(
    petstore_auth="",
)

req = operations.FindPetsByStatusRequest()

res = s.pet.find_pets_by_status(req)

if res.pets is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.FindPetsByStatusRequest](../../models/operations/findpetsbystatusrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.FindPetsByStatusResponse](../../models/operations/findpetsbystatusresponse.md)**


## find_pets_by_tags

Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore(
    petstore_auth="",
)

req = operations.FindPetsByTagsRequest(
    tags=[
        'string',
    ],
)

res = s.pet.find_pets_by_tags(req)

if res.pets is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.FindPetsByTagsRequest](../../models/operations/findpetsbytagsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.FindPetsByTagsResponse](../../models/operations/findpetsbytagsresponse.md)**


## get_pet_by_id

Returns a single pet

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore()

req = operations.GetPetByIDRequest(
    pet_id=504151,
)

res = s.pet.get_pet_by_id(req, operations.GetPetByIDSecurity(
    api_key="",
))

if res.pet is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetPetByIDRequest](../../models/operations/getpetbyidrequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.GetPetByIDSecurity](../../models/operations/getpetbyidsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.GetPetByIDResponse](../../models/operations/getpetbyidresponse.md)**


## update_pet_with_form

Updates a pet in the store with form data

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore(
    petstore_auth="",
)

req = operations.UpdatePetWithFormRequest(
    pet_id=303241,
)

res = s.pet.update_pet_with_form(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdatePetWithFormRequest](../../models/operations/updatepetwithformrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.UpdatePetWithFormResponse](../../models/operations/updatepetwithformresponse.md)**


## update_pet_form

Update an existing pet by Id

### Example Usage

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

res = s.pet.update_pet_form(req)

if res.pet is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [shared.Pet](../../models/shared/pet.md)   | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.UpdatePetFormResponse](../../models/operations/updatepetformresponse.md)**


## update_pet_json

Update an existing pet by Id

### Example Usage

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

res = s.pet.update_pet_json(req)

if res.pet is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [shared.Pet](../../models/shared/pet.md)   | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.UpdatePetJSONResponse](../../models/operations/updatepetjsonresponse.md)**


## update_pet_raw

Update an existing pet by Id

### Example Usage

```python
import petstore
from petstore.models import shared

s = petstore.Petstore(
    petstore_auth="",
)

req = ':Pnf><u_<@'.encode()

res = s.pet.update_pet_raw(req)

if res.pet is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [bytes](../../models//.md)                 | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.UpdatePetRawResponse](../../models/operations/updatepetrawresponse.md)**


## upload_file

uploads an image

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore(
    petstore_auth="",
)

req = operations.UploadFileRequest(
    request_body='U?WWKB{5@q'.encode(),
    pet_id=621158,
)

res = s.pet.upload_file(req)

if res.api_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.UploadFileRequest](../../models/operations/uploadfilerequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.UploadFileResponse](../../models/operations/uploadfileresponse.md)**

