# petstore

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/speakeasy-sdks/test1q34234242.git/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/test1q34234242/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/test1q34234242.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

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
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [pet](docs/sdks/pet/README.md)

* [add_pet_form](docs/sdks/pet/README.md#add_pet_form) - Add a new pet to the store
* [add_pet_json](docs/sdks/pet/README.md#add_pet_json) - Add a new pet to the store
* [add_pet_raw](docs/sdks/pet/README.md#add_pet_raw) - Add a new pet to the store
* [delete_pet](docs/sdks/pet/README.md#delete_pet) - Deletes a pet
* [find_pets_by_status](docs/sdks/pet/README.md#find_pets_by_status) - Finds Pets by status
* [find_pets_by_tags](docs/sdks/pet/README.md#find_pets_by_tags) - Finds Pets by tags
* [get_pet_by_id](docs/sdks/pet/README.md#get_pet_by_id) - Find pet by ID
* [update_pet_with_form](docs/sdks/pet/README.md#update_pet_with_form) - Updates a pet in the store with form data
* [update_pet_form](docs/sdks/pet/README.md#update_pet_form) - Update an existing pet
* [update_pet_json](docs/sdks/pet/README.md#update_pet_json) - Update an existing pet
* [update_pet_raw](docs/sdks/pet/README.md#update_pet_raw) - Update an existing pet
* [upload_file](docs/sdks/pet/README.md#upload_file) - uploads an image

### [store](docs/sdks/store/README.md)

* [delete_order](docs/sdks/store/README.md#delete_order) - Delete purchase order by ID
* [get_inventory](docs/sdks/store/README.md#get_inventory) - Returns pet inventories by status
* [get_order_by_id](docs/sdks/store/README.md#get_order_by_id) - Find purchase order by ID
* [place_order_form](docs/sdks/store/README.md#place_order_form) - Place an order for a pet
* [place_order_json](docs/sdks/store/README.md#place_order_json) - Place an order for a pet
* [place_order_raw](docs/sdks/store/README.md#place_order_raw) - Place an order for a pet

### [user](docs/sdks/user/README.md)

* [create_user_form](docs/sdks/user/README.md#create_user_form) - Create user
* [create_user_json](docs/sdks/user/README.md#create_user_json) - Create user
* [create_user_raw](docs/sdks/user/README.md#create_user_raw) - Create user
* [create_users_with_list_input](docs/sdks/user/README.md#create_users_with_list_input) - Creates list of users with given input array
* [delete_user](docs/sdks/user/README.md#delete_user) - Delete user
* [get_user_by_name](docs/sdks/user/README.md#get_user_by_name) - Get user by user name
* [login_user](docs/sdks/user/README.md#login_user) - Logs user into the system
* [logout_user](docs/sdks/user/README.md#logout_user) - Logs out current logged in user session
* [update_user_form](docs/sdks/user/README.md#update_user_form) - Update user
* [update_user_json](docs/sdks/user/README.md#update_user_json) - Update user
* [update_user_raw](docs/sdks/user/README.md#update_user_raw) - Update user
<!-- End Available Resources and Operations [operations] -->



<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

### Example

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

res = None
try:
    res = s.pet.add_pet_form(req)
except errors.SDKError as e:
    print(e)  # handle exception
    raise(e)

if res.pet is not None:
    # handle response
    pass
```
<!-- End Error Handling [errors] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https:///v3` | None |

#### Example

```python
import petstore
from petstore.models import shared

s = petstore.Petstore(
    server_idx=0,
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


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import petstore
from petstore.models import shared

s = petstore.Petstore(
    server_url="https:///v3",
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
<!-- End Server Selection [server] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import petstore
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = petstore.Petstore(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->



<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name            | Type            | Scheme          |
| --------------- | --------------- | --------------- |
| `petstore_auth` | oauth2          | OAuth2 token    |

To authenticate with the API the `petstore_auth` parameter must be set when initializing the SDK client instance. For example:
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

### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
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
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
