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
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = shared.Pet(
    name='doggie',
    photo_urls=[
        '<value>',
    ],
    id=10,
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## add_pet_json

Add a new pet to the store

### Example Usage

```python
import petstore
from petstore.models import shared

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = shared.Pet(
    name='doggie',
    photo_urls=[
        '<value>',
    ],
    id=10,
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## add_pet_raw

Add a new pet to the store

### Example Usage

```python
import petstore

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = '0xcf5E85CDde'.encode()

res = s.pet.add_pet_raw(req)

if res.pet is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [bytes](../../models/.md)                  | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.AddPetRawResponse](../../models/operations/addpetrawresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_pet

Deletes a pet

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.DeletePetRequest(
    pet_id=441876,
)

res = s.pet.delete_pet(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.DeletePetRequest](../../models/operations/deletepetrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.DeletePetResponse](../../models/operations/deletepetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## find_pets_by_status

Multiple status values can be provided with comma separated strings

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.FindPetsByStatusRequest()

res = s.pet.find_pets_by_status(req)

if res.two_hundred_application_json_classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.FindPetsByStatusRequest](../../models/operations/findpetsbystatusrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.FindPetsByStatusResponse](../../models/operations/findpetsbystatusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## find_pets_by_tags

Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.FindPetsByTagsRequest()

res = s.pet.find_pets_by_tags(req)

if res.two_hundred_application_json_classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.FindPetsByTagsRequest](../../models/operations/findpetsbytagsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.FindPetsByTagsResponse](../../models/operations/findpetsbytagsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

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
    api_key="<YOUR_API_KEY_HERE>",
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_pet_with_form

Updates a pet in the store with form data

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.UpdatePetWithFormRequest(
    pet_id=303241,
)

res = s.pet.update_pet_with_form(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdatePetWithFormRequest](../../models/operations/updatepetwithformrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.UpdatePetWithFormResponse](../../models/operations/updatepetwithformresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_pet_form

Update an existing pet by Id

### Example Usage

```python
import petstore
from petstore.models import shared

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = shared.Pet(
    name='doggie',
    photo_urls=[
        '<value>',
    ],
    id=10,
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_pet_json

Update an existing pet by Id

### Example Usage

```python
import petstore
from petstore.models import shared

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = shared.Pet(
    name='doggie',
    photo_urls=[
        '<value>',
    ],
    id=10,
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_pet_raw

Update an existing pet by Id

### Example Usage

```python
import petstore

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = '0x6bCA76De67'.encode()

res = s.pet.update_pet_raw(req)

if res.pet is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [bytes](../../models/.md)                  | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.UpdatePetRawResponse](../../models/operations/updatepetrawresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## upload_file

uploads an image

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.UploadFileRequest(
    pet_id=565380,
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
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
