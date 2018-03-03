# swagger_client.DefaultApi

All URIs are relative to *http://localhost:8080/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diskspace_get**](DefaultApi.md#diskspace_get) | **GET** /diskspace | 


# **diskspace_get**
> DISKSPACE diskspace_get()



Returns disk space information of the hosting server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.diskspace_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->diskspace_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DISKSPACE**](DISKSPACE.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

