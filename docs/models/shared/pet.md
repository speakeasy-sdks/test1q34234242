# Pet


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `category`                                              | [Optional[Category]](../../models/shared/category.md)   | :heavy_minus_sign:                                      | N/A                                                     |                                                         |
| `id`                                                    | *Optional[int]*                                         | :heavy_minus_sign:                                      | N/A                                                     | 10                                                      |
| `name`                                                  | *str*                                                   | :heavy_check_mark:                                      | N/A                                                     | doggie                                                  |
| `photo_urls`                                            | List[*str*]                                             | :heavy_check_mark:                                      | N/A                                                     |                                                         |
| `status`                                                | [Optional[PetStatus]](../../models/shared/petstatus.md) | :heavy_minus_sign:                                      | pet status in the store                                 |                                                         |
| `tags`                                                  | List[[Tag](../../models/shared/tag.md)]                 | :heavy_minus_sign:                                      | N/A                                                     |                                                         |