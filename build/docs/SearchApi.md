---
title: SearchApi
---

## PureCloudPlatformClientV2.SearchApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**get_documentation_gkn_search**](SearchApi.html#get_documentation_gkn_search) | Search gkn documentation using the q64 value returned from a previous search|
|[**get_documentation_search**](SearchApi.html#get_documentation_search) | Search documentation using the q64 value returned from a previous search|
|[**get_groups_search**](SearchApi.html#get_groups_search) | Search groups using the q64 value returned from a previous search|
|[**get_locations_search**](SearchApi.html#get_locations_search) | Search locations using the q64 value returned from a previous search|
|[**get_search**](SearchApi.html#get_search) | Search using the q64 value returned from a previous search.|
|[**get_search_suggest**](SearchApi.html#get_search_suggest) | Suggest resources using the q64 value returned from a previous suggest query.|
|[**get_users_search**](SearchApi.html#get_users_search) | Search users using the q64 value returned from a previous search|
|[**get_voicemail_search**](SearchApi.html#get_voicemail_search) | Search voicemails using the q64 value returned from a previous search|
|[**post_analytics_conversations_transcripts_query**](SearchApi.html#post_analytics_conversations_transcripts_query) | Search resources.|
|[**post_documentation_gkn_search**](SearchApi.html#post_documentation_gkn_search) | Search gkn documentation|
|[**post_documentation_search**](SearchApi.html#post_documentation_search) | Search documentation|
|[**post_groups_search**](SearchApi.html#post_groups_search) | Search groups|
|[**post_knowledge_knowledgebase_search**](SearchApi.html#post_knowledge_knowledgebase_search) | Search Documents|
|[**post_locations_search**](SearchApi.html#post_locations_search) | Search locations|
|[**post_search**](SearchApi.html#post_search) | Search resources.|
|[**post_search_suggest**](SearchApi.html#post_search_suggest) | Suggest resources.|
|[**post_speechandtextanalytics_transcripts_search**](SearchApi.html#post_speechandtextanalytics_transcripts_search) | Search resources.|
|[**post_users_search**](SearchApi.html#post_users_search) | Search users|
|[**post_voicemail_search**](SearchApi.html#post_voicemail_search) | Search voicemails|
{: class="table table-striped"}

<a name="get_documentation_gkn_search"></a>

## [**GKNDocumentationSearchResponse**](GKNDocumentationSearchResponse.html) get_documentation_gkn_search(q64)



Search gkn documentation using the q64 value returned from a previous search



Wraps GET /api/v2/documentation/gkn/search 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
q64 = 'q64_example' # str | q64

try:
    # Search gkn documentation using the q64 value returned from a previous search
    api_response = api_instance.get_documentation_gkn_search(q64)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_documentation_gkn_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
{: class="table table-striped"}

### Return type

[**GKNDocumentationSearchResponse**](GKNDocumentationSearchResponse.html)

<a name="get_documentation_search"></a>

## [**DocumentationSearchResponse**](DocumentationSearchResponse.html) get_documentation_search(q64)



Search documentation using the q64 value returned from a previous search



Wraps GET /api/v2/documentation/search 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
q64 = 'q64_example' # str | q64

try:
    # Search documentation using the q64 value returned from a previous search
    api_response = api_instance.get_documentation_search(q64)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_documentation_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
{: class="table table-striped"}

### Return type

[**DocumentationSearchResponse**](DocumentationSearchResponse.html)

<a name="get_groups_search"></a>

## [**GroupsSearchResponse**](GroupsSearchResponse.html) get_groups_search(q64, expand=expand)



Search groups using the q64 value returned from a previous search



Wraps GET /api/v2/groups/search 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | expand (optional)

try:
    # Search groups using the q64 value returned from a previous search
    api_response = api_instance.get_groups_search(q64, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_groups_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
| **expand** | [**list[str]**](str.html)| expand | [optional]  |
{: class="table table-striped"}

### Return type

[**GroupsSearchResponse**](GroupsSearchResponse.html)

<a name="get_locations_search"></a>

## [**LocationsSearchResponse**](LocationsSearchResponse.html) get_locations_search(q64, expand=expand)



Search locations using the q64 value returned from a previous search



Wraps GET /api/v2/locations/search 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | Provides more details about a specified resource (optional)

try:
    # Search locations using the q64 value returned from a previous search
    api_response = api_instance.get_locations_search(q64, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_locations_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
| **expand** | [**list[str]**](str.html)| Provides more details about a specified resource | [optional] <br />**Values**: images, addressVerificationDetails |
{: class="table table-striped"}

### Return type

[**LocationsSearchResponse**](LocationsSearchResponse.html)

<a name="get_search"></a>

## [**JsonNodeSearchResponse**](JsonNodeSearchResponse.html) get_search(q64, expand=expand, profile=profile)



Search using the q64 value returned from a previous search.



Wraps GET /api/v2/search 

Requires ANY permissions: 

* directory:user:divisionview

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)
profile = true # bool | profile (optional) (default to true)

try:
    # Search using the q64 value returned from a previous search.
    api_response = api_instance.get_search(q64, expand=expand, profile=profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography, callerUser.routingStatus, callerUser.primaryPresence, callerUser.conversationSummary, callerUser.outOfOffice, callerUser.geolocation, images, addressVerificationDetails |
| **profile** | **bool**| profile | [optional] [default to true] |
{: class="table table-striped"}

### Return type

[**JsonNodeSearchResponse**](JsonNodeSearchResponse.html)

<a name="get_search_suggest"></a>

## [**JsonNodeSearchResponse**](JsonNodeSearchResponse.html) get_search_suggest(q64, expand=expand, profile=profile)



Suggest resources using the q64 value returned from a previous suggest query.



Wraps GET /api/v2/search/suggest 

Requires ANY permissions: 

* directory:user:divisionview

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | Which fields, if any, to expand (optional)
profile = true # bool | profile (optional) (default to true)

try:
    # Suggest resources using the q64 value returned from a previous suggest query.
    api_response = api_instance.get_search_suggest(q64, expand=expand, profile=profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_search_suggest: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
| **expand** | [**list[str]**](str.html)| Which fields, if any, to expand | [optional] <br />**Values**: routingStatus, presence, conversationSummary, outOfOffice, geolocation, station, authorization, lasttokenissued, authorization.unusedRoles, team, profileSkills, certifications, locations, groups, skills, languages, languagePreference, employerInfo, biography, callerUser.routingStatus, callerUser.primaryPresence, callerUser.conversationSummary, callerUser.outOfOffice, callerUser.geolocation, images, addressVerificationDetails |
| **profile** | **bool**| profile | [optional] [default to true] |
{: class="table table-striped"}

### Return type

[**JsonNodeSearchResponse**](JsonNodeSearchResponse.html)

<a name="get_users_search"></a>

## [**UsersSearchResponse**](UsersSearchResponse.html) get_users_search(q64, expand=expand, integration_presence_source=integration_presence_source)



Search users using the q64 value returned from a previous search



Wraps GET /api/v2/users/search 

Requires ANY permissions: 

* directory:user:divisionview

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | expand (optional)
integration_presence_source = 'integration_presence_source_example' # str | integrationPresenceSource (optional)

try:
    # Search users using the q64 value returned from a previous search
    api_response = api_instance.get_users_search(q64, expand=expand, integration_presence_source=integration_presence_source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_users_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
| **expand** | [**list[str]**](str.html)| expand | [optional]  |
| **integration_presence_source** | **str**| integrationPresenceSource | [optional] <br />**Values**: MicrosoftTeams, ZoomPhone, RingCentral |
{: class="table table-striped"}

### Return type

[**UsersSearchResponse**](UsersSearchResponse.html)

<a name="get_voicemail_search"></a>

## [**VoicemailsSearchResponse**](VoicemailsSearchResponse.html) get_voicemail_search(q64, expand=expand)



Search voicemails using the q64 value returned from a previous search



Wraps GET /api/v2/voicemail/search 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
q64 = 'q64_example' # str | q64
expand = ['expand_example'] # list[str] | expand (optional)

try:
    # Search voicemails using the q64 value returned from a previous search
    api_response = api_instance.get_voicemail_search(q64, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_voicemail_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **q64** | **str**| q64 |  |
| **expand** | [**list[str]**](str.html)| expand | [optional]  |
{: class="table table-striped"}

### Return type

[**VoicemailsSearchResponse**](VoicemailsSearchResponse.html)

<a name="post_analytics_conversations_transcripts_query"></a>

## [**AnalyticsConversationWithoutAttributesMultiGetResponse**](AnalyticsConversationWithoutAttributesMultiGetResponse.html) post_analytics_conversations_transcripts_query(body)



Search resources.



Wraps POST /api/v2/analytics/conversations/transcripts/query 

Requires ANY permissions: 

* analytics:conversationDetail:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.TranscriptConversationDetailSearchRequest() # TranscriptConversationDetailSearchRequest | Search request options

try:
    # Search resources.
    api_response = api_instance.post_analytics_conversations_transcripts_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_analytics_conversations_transcripts_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TranscriptConversationDetailSearchRequest**](TranscriptConversationDetailSearchRequest.html)| Search request options |  |
{: class="table table-striped"}

### Return type

[**AnalyticsConversationWithoutAttributesMultiGetResponse**](AnalyticsConversationWithoutAttributesMultiGetResponse.html)

<a name="post_documentation_gkn_search"></a>

## [**GKNDocumentationSearchResponse**](GKNDocumentationSearchResponse.html) post_documentation_gkn_search(body)



Search gkn documentation



Wraps POST /api/v2/documentation/gkn/search 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.GKNDocumentationSearchRequest() # GKNDocumentationSearchRequest | Search request options

try:
    # Search gkn documentation
    api_response = api_instance.post_documentation_gkn_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_documentation_gkn_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**GKNDocumentationSearchRequest**](GKNDocumentationSearchRequest.html)| Search request options |  |
{: class="table table-striped"}

### Return type

[**GKNDocumentationSearchResponse**](GKNDocumentationSearchResponse.html)

<a name="post_documentation_search"></a>

## [**DocumentationSearchResponse**](DocumentationSearchResponse.html) post_documentation_search(body)



Search documentation



Wraps POST /api/v2/documentation/search 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.DocumentationSearchRequest() # DocumentationSearchRequest | Search request options

try:
    # Search documentation
    api_response = api_instance.post_documentation_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_documentation_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**DocumentationSearchRequest**](DocumentationSearchRequest.html)| Search request options |  |
{: class="table table-striped"}

### Return type

[**DocumentationSearchResponse**](DocumentationSearchResponse.html)

<a name="post_groups_search"></a>

## [**GroupsSearchResponse**](GroupsSearchResponse.html) post_groups_search(body)



Search groups



Wraps POST /api/v2/groups/search 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.GroupSearchRequest() # GroupSearchRequest | Search request options

try:
    # Search groups
    api_response = api_instance.post_groups_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_groups_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**GroupSearchRequest**](GroupSearchRequest.html)| Search request options |  |
{: class="table table-striped"}

### Return type

[**GroupsSearchResponse**](GroupsSearchResponse.html)

<a name="post_knowledge_knowledgebase_search"></a>

## [**KnowledgeSearchResponse**](KnowledgeSearchResponse.html) post_knowledge_knowledgebase_search(knowledge_base_id, body=body)



Search Documents



Wraps POST /api/v2/knowledge/knowledgebases/{knowledgeBaseId}/search 

Requires ALL permissions: 

* knowledge:knowledgebase:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
knowledge_base_id = 'knowledge_base_id_example' # str | Knowledge base ID
body = PureCloudPlatformClientV2.KnowledgeSearchRequest() # KnowledgeSearchRequest |  (optional)

try:
    # Search Documents
    api_response = api_instance.post_knowledge_knowledgebase_search(knowledge_base_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_knowledge_knowledgebase_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **knowledge_base_id** | **str**| Knowledge base ID |  |
| **body** | [**KnowledgeSearchRequest**](KnowledgeSearchRequest.html)|  | [optional]  |
{: class="table table-striped"}

### Return type

[**KnowledgeSearchResponse**](KnowledgeSearchResponse.html)

<a name="post_locations_search"></a>

## [**LocationsSearchResponse**](LocationsSearchResponse.html) post_locations_search(body)



Search locations



Wraps POST /api/v2/locations/search 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.LocationSearchRequest() # LocationSearchRequest | Search request options

try:
    # Search locations
    api_response = api_instance.post_locations_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_locations_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**LocationSearchRequest**](LocationSearchRequest.html)| Search request options |  |
{: class="table table-striped"}

### Return type

[**LocationsSearchResponse**](LocationsSearchResponse.html)

<a name="post_search"></a>

## [**JsonNodeSearchResponse**](JsonNodeSearchResponse.html) post_search(body, profile=profile)



Search resources.



Wraps POST /api/v2/search 

Requires ANY permissions: 

* directory:user:divisionview

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.SearchRequest() # SearchRequest | Search request options
profile = true # bool | profile (optional) (default to true)

try:
    # Search resources.
    api_response = api_instance.post_search(body, profile=profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SearchRequest**](SearchRequest.html)| Search request options |  |
| **profile** | **bool**| profile | [optional] [default to true] |
{: class="table table-striped"}

### Return type

[**JsonNodeSearchResponse**](JsonNodeSearchResponse.html)

<a name="post_search_suggest"></a>

## [**JsonNodeSearchResponse**](JsonNodeSearchResponse.html) post_search_suggest(body, profile=profile)



Suggest resources.



Wraps POST /api/v2/search/suggest 

Requires ANY permissions: 

* directory:user:divisionview

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.SuggestSearchRequest() # SuggestSearchRequest | Search request options
profile = true # bool | profile (optional) (default to true)

try:
    # Suggest resources.
    api_response = api_instance.post_search_suggest(body, profile=profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_search_suggest: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**SuggestSearchRequest**](SuggestSearchRequest.html)| Search request options |  |
| **profile** | **bool**| profile | [optional] [default to true] |
{: class="table table-striped"}

### Return type

[**JsonNodeSearchResponse**](JsonNodeSearchResponse.html)

<a name="post_speechandtextanalytics_transcripts_search"></a>

## [**JsonSearchResponse**](JsonSearchResponse.html) post_speechandtextanalytics_transcripts_search(body)



Search resources.



Wraps POST /api/v2/speechandtextanalytics/transcripts/search 

Requires ANY permissions: 

* analytics:conversationDetail:view
* recording:recording:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.TranscriptSearchRequest() # TranscriptSearchRequest | Search request options

try:
    # Search resources.
    api_response = api_instance.post_speechandtextanalytics_transcripts_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_speechandtextanalytics_transcripts_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TranscriptSearchRequest**](TranscriptSearchRequest.html)| Search request options |  |
{: class="table table-striped"}

### Return type

[**JsonSearchResponse**](JsonSearchResponse.html)

<a name="post_users_search"></a>

## [**UsersSearchResponse**](UsersSearchResponse.html) post_users_search(body)



Search users



Wraps POST /api/v2/users/search 

Requires ANY permissions: 

* directory:user:divisionview

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.UserSearchRequest() # UserSearchRequest | Search request options

try:
    # Search users
    api_response = api_instance.post_users_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_users_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UserSearchRequest**](UserSearchRequest.html)| Search request options |  |
{: class="table table-striped"}

### Return type

[**UsersSearchResponse**](UsersSearchResponse.html)

<a name="post_voicemail_search"></a>

## [**VoicemailsSearchResponse**](VoicemailsSearchResponse.html) post_voicemail_search(body)



Search voicemails



Wraps POST /api/v2/voicemail/search 

Requires NO permissions: 


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.SearchApi()
body = PureCloudPlatformClientV2.VoicemailSearchRequest() # VoicemailSearchRequest | Search request options

try:
    # Search voicemails
    api_response = api_instance.post_voicemail_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_voicemail_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**VoicemailSearchRequest**](VoicemailSearchRequest.html)| Search request options |  |
{: class="table table-striped"}

### Return type

[**VoicemailsSearchResponse**](VoicemailsSearchResponse.html)

