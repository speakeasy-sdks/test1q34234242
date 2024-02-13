# Store
(*store*)

## Overview

Access to Petstore orders

Find out more about our store
<http://swagger.io>
### Available Operations

* [delete_order](#delete_order) - Delete purchase order by ID
* [get_inventory](#get_inventory) - Returns pet inventories by status
* [get_order_by_id](#get_order_by_id) - Find purchase order by ID
* [place_order_form](#place_order_form) - Place an order for a pet
* [place_order_json](#place_order_json) - Place an order for a pet
* [place_order_raw](#place_order_raw) - Place an order for a pet

## delete_order

For valid response try integer IDs with value < 1000. Anything above 1000 or nonintegers will generate API errors

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.DeleteOrderRequest(
    order_id=127902,
)

res = s.store.delete_order(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.DeleteOrderRequest](../../models/operations/deleteorderrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.DeleteOrderResponse](../../models/operations/deleteorderresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_inventory

Returns a map of status codes to quantities

### Example Usage

```python
import petstore

s = petstore.Petstore()


res = s.store.get_inventory("<YOUR_API_KEY_HERE>")

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `security`                                                                         | [operations.GetInventorySecurity](../../models/operations/getinventorysecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.GetInventoryResponse](../../models/operations/getinventoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_order_by_id

For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

### Example Usage

```python
import petstore
from petstore.models import operations

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = operations.GetOrderByIDRequest(
    order_id=614993,
)

res = s.store.get_order_by_id(req)

if res.order is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetOrderByIDRequest](../../models/operations/getorderbyidrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetOrderByIDResponse](../../models/operations/getorderbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## place_order_form

Place a new order in the store

### Example Usage

```python
import petstore
from petstore.models import shared

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = shared.Order(
    id=10,
    pet_id=198772,
    quantity=7,
    status=shared.Status.APPROVED,
)

res = s.store.place_order_form(req)

if res.order is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                    | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `request`                                    | [shared.Order](../../models/shared/order.md) | :heavy_check_mark:                           | The request object to use for the request.   |


### Response

**[operations.PlaceOrderFormResponse](../../models/operations/placeorderformresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## place_order_json

Place a new order in the store

### Example Usage

```python
import petstore
from petstore.models import shared

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = shared.Order(
    id=10,
    pet_id=198772,
    quantity=7,
    status=shared.Status.APPROVED,
)

res = s.store.place_order_json(req)

if res.order is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                    | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `request`                                    | [shared.Order](../../models/shared/order.md) | :heavy_check_mark:                           | The request object to use for the request.   |


### Response

**[operations.PlaceOrderJSONResponse](../../models/operations/placeorderjsonresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## place_order_raw

Place a new order in the store

### Example Usage

```python
import petstore

s = petstore.Petstore(
    petstore_auth="Bearer <YOUR_ACCESS_TOKEN_HERE>",
)

req = '0xcB9dC14dEe'.encode()

res = s.store.place_order_raw(req)

if res.order is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [bytes](../../models/.md)                  | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.PlaceOrderRawResponse](../../models/operations/placeorderrawresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
