# LoginUserResponse


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `content_type`                                                                        | *str*                                                                                 | :heavy_check_mark:                                                                    | HTTP response content type for this operation                                         |
| `headers`                                                                             | Dict[str, List[*str*]]                                                                | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `status_code`                                                                         | *int*                                                                                 | :heavy_check_mark:                                                                    | HTTP response status code for this operation                                          |
| `raw_response`                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_minus_sign:                                                                    | Raw HTTP response; suitable for custom response parsing                               |
| `login_user_200_application_json_string`                                              | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | successful operation                                                                  |
| `login_user_200_application_xml_string`                                               | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | successful operation                                                                  |