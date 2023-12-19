# User
(*user*)

## Overview

Operations about user

### Available Operations

* [create_user_form](#create_user_form) - Create user
* [create_user_json](#create_user_json) - Create user
* [create_user_raw](#create_user_raw) - Create user
* [create_users_with_list_input](#create_users_with_list_input) - Creates list of users with given input array
* [delete_user](#delete_user) - Delete user
* [get_user_by_name](#get_user_by_name) - Get user by user name
* [login_user](#login_user) - Logs user into the system
* [logout_user](#logout_user) - Logs out current logged in user session
* [update_user_form](#update_user_form) - Update user
* [update_user_json](#update_user_json) - Update user
* [update_user_raw](#update_user_raw) - Update user

## create_user_form

This can only be done by the logged in user.

### Example Usage

```python
import petstore
from petstore.models import shared

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = shared.User(
    email='john@email.com',
    first_name='John',
    id=10,
    last_name='James',
    password='12345',
    phone='12345',
    user_status=1,
    username='theUser',
)

res = s.user.create_user_form(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [shared.User](../../models/shared/user.md) | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateUserFormResponse](../../models/operations/createuserformresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_user_json

This can only be done by the logged in user.

### Example Usage

```python
import petstore
from petstore.models import shared

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = shared.User(
    email='john@email.com',
    first_name='John',
    id=10,
    last_name='James',
    password='12345',
    phone='12345',
    user_status=1,
    username='theUser',
)

res = s.user.create_user_json(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [shared.User](../../models/shared/user.md) | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateUserJSONResponse](../../models/operations/createuserjsonresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_user_raw

This can only be done by the logged in user.

### Example Usage

```python
import petstore
from petstore.models import shared

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = '0xB4dDB1Eeed'.encode()

res = s.user.create_user_raw(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [bytes](../../models/.md)                  | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateUserRawResponse](../../models/operations/createuserrawresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## create_users_with_list_input

Creates list of users with given input array

### Example Usage

```python
import petstore
from petstore.models import shared

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = [
    shared.User(
        email='john@email.com',
        first_name='John',
        id=10,
        last_name='James',
        password='12345',
        phone='12345',
        user_status=1,
        username='theUser',
    ),
]

res = s.user.create_users_with_list_input(req)

if res.user is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [List[shared.User]](../../models/.md)      | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.CreateUsersWithListInputResponse](../../models/operations/createuserswithlistinputresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_user

This can only be done by the logged in user.

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.DeleteUserRequest(
    username='Demetris_Torphy',
)

res = s.user.delete_user(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.DeleteUserRequest](../../models/operations/deleteuserrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.DeleteUserResponse](../../models/operations/deleteuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_user_by_name

Get user by user name

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.GetUserByNameRequest(
    username='Zachery_Schneider',
)

res = s.user.get_user_by_name(req)

if res.user is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetUserByNameRequest](../../models/operations/getuserbynamerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetUserByNameResponse](../../models/operations/getuserbynameresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## login_user

Logs user into the system

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.LoginUserRequest()

res = s.user.login_user(req)

if res.two_hundred_application_json_res is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.LoginUserRequest](../../models/operations/loginuserrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.LoginUserResponse](../../models/operations/loginuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## logout_user

Logs out current logged in user session

### Example Usage

```python
import petstore

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)


res = s.user.logout_user()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.LogoutUserResponse](../../models/operations/logoutuserresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_user_form

This can only be done by the logged in user.

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.UpdateUserFormRequest(
    user=shared.User(
        email='john@email.com',
        first_name='John',
        id=10,
        last_name='James',
        password='12345',
        phone='12345',
        user_status=1,
        username='theUser',
    ),
    username='Bo_Lynch4',
)

res = s.user.update_user_form(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateUserFormRequest](../../models/operations/updateuserformrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateUserFormResponse](../../models/operations/updateuserformresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_user_json

This can only be done by the logged in user.

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.UpdateUserJSONRequest(
    user=shared.User(
        email='john@email.com',
        first_name='John',
        id=10,
        last_name='James',
        password='12345',
        phone='12345',
        user_status=1,
        username='theUser',
    ),
    username='Alanna_Waters81',
)

res = s.user.update_user_json(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpdateUserJSONRequest](../../models/operations/updateuserjsonrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpdateUserJSONResponse](../../models/operations/updateuserjsonresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## update_user_raw

This can only be done by the logged in user.

### Example Usage

```python
import petstore
from petstore.models import operations, shared

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.UpdateUserRawRequest(
    request_body='0xf4D36eFb83'.encode(),
    username='Eleonore2',
)

res = s.user.update_user_raw(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateUserRawRequest](../../models/operations/updateuserrawrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.UpdateUserRawResponse](../../models/operations/updateuserrawresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
