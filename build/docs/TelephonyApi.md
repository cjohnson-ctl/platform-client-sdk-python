---
title: TelephonyApi
---

## PureCloudPlatformClientV2.TelephonyApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_telephony_siptraces**](TelephonyApi.html#get_telephony_siptraces) | Fetch SIP metadata|
|[**get_telephony_siptraces_download_download_id**](TelephonyApi.html#get_telephony_siptraces_download_download_id) | Get signed S3 URL for a pcap download|
|[**post_telephony_siptraces_download**](TelephonyApi.html#post_telephony_siptraces_download) | Request a download of a pcap file to S3|
{: class="table table-striped"}

<a name="get_telephony_siptraces"></a>

## [**SipSearchResult**](SipSearchResult.html) get_telephony_siptraces(date_start, date_end, call_id=call_id, to_user=to_user, from_user=from_user, conversation_id=conversation_id)



Fetch SIP metadata

Fetch SIP metadata that matches a given parameter. If exactMatch is passed as a parameter only sip records that have exactly that value will be returned. For example, some records contain conversationId but not all relevant records for that call may contain the conversationId so only a partial view of the call will be reflected

Wraps GET /api/v2/telephony/siptraces 

Requires ALL permissions: 

* telephony:pcap:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyApi()
date_start = '2013-10-20T19:20:30+01:00' # datetime | Start date of the search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
date_end = '2013-10-20T19:20:30+01:00' # datetime | End date of the search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z
call_id = 'call_id_example' # str | unique identification of the placed call (optional)
to_user = 'to_user_example' # str | User to who the call was placed (optional)
from_user = 'from_user_example' # str | user who placed the call (optional)
conversation_id = 'conversation_id_example' # str | Unique identification of the conversation (optional)

try:
    # Fetch SIP metadata
    api_response = api_instance.get_telephony_siptraces(date_start, date_end, call_id=call_id, to_user=to_user, from_user=from_user, conversation_id=conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->get_telephony_siptraces: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **date_start** | **datetime**| Start date of the search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z |  |
| **date_end** | **datetime**| End date of the search. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z |  |
| **call_id** | **str**| unique identification of the placed call | [optional]  |
| **to_user** | **str**| User to who the call was placed | [optional]  |
| **from_user** | **str**| user who placed the call | [optional]  |
| **conversation_id** | **str**| Unique identification of the conversation | [optional]  |
{: class="table table-striped"}

### Return type

[**SipSearchResult**](SipSearchResult.html)

<a name="get_telephony_siptraces_download_download_id"></a>

## [**SignedUrlResponse**](SignedUrlResponse.html) get_telephony_siptraces_download_download_id(download_id)



Get signed S3 URL for a pcap download



Wraps GET /api/v2/telephony/siptraces/download/{downloadId} 

Requires ALL permissions: 

* telephony:pcap:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyApi()
download_id = 'download_id_example' # str | unique id for the downloaded file in S3

try:
    # Get signed S3 URL for a pcap download
    api_response = api_instance.get_telephony_siptraces_download_download_id(download_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->get_telephony_siptraces_download_download_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **download_id** | **str**| unique id for the downloaded file in S3 |  |
{: class="table table-striped"}

### Return type

[**SignedUrlResponse**](SignedUrlResponse.html)

<a name="post_telephony_siptraces_download"></a>

## [**SipDownloadResponse**](SipDownloadResponse.html) post_telephony_siptraces_download(sip_search_public_request)



Request a download of a pcap file to S3



Wraps POST /api/v2/telephony/siptraces/download 

Requires ALL permissions: 

* telephony:pcap:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.TelephonyApi()
sip_search_public_request = PureCloudPlatformClientV2.SIPSearchPublicRequest() # SIPSearchPublicRequest | 

try:
    # Request a download of a pcap file to S3
    api_response = api_instance.post_telephony_siptraces_download(sip_search_public_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelephonyApi->post_telephony_siptraces_download: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **sip_search_public_request** | [**SIPSearchPublicRequest**](SIPSearchPublicRequest.html)|  |  |
{: class="table table-striped"}

### Return type

[**SipDownloadResponse**](SipDownloadResponse.html)

