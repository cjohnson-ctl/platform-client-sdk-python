---
title: CoachingApi
---

## PureCloudPlatformClientV2.CoachingApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_coaching_appointment**](CoachingApi.html#delete_coaching_appointment) | Delete an existing appointment|
|[**delete_coaching_appointment_annotation**](CoachingApi.html#delete_coaching_appointment_annotation) | Delete an existing annotation|
|[**get_coaching_appointment**](CoachingApi.html#get_coaching_appointment) | Retrieve an appointment|
|[**get_coaching_appointment_annotation**](CoachingApi.html#get_coaching_appointment_annotation) | Retrieve an annotation.|
|[**get_coaching_appointment_annotations**](CoachingApi.html#get_coaching_appointment_annotations) | Get a list of annotations.|
|[**get_coaching_appointment_statuses**](CoachingApi.html#get_coaching_appointment_statuses) | Get the list of status changes for a coaching appointment.|
|[**get_coaching_appointments**](CoachingApi.html#get_coaching_appointments) | Get appointments for users and optional date range|
|[**get_coaching_appointments_me**](CoachingApi.html#get_coaching_appointments_me) | Get my appointments for a given date range|
|[**get_coaching_notification**](CoachingApi.html#get_coaching_notification) | Get an existing notification|
|[**get_coaching_notifications**](CoachingApi.html#get_coaching_notifications) | Retrieve the list of your notifications.|
|[**patch_coaching_appointment**](CoachingApi.html#patch_coaching_appointment) | Update an existing appointment|
|[**patch_coaching_appointment_annotation**](CoachingApi.html#patch_coaching_appointment_annotation) | Update an existing annotation.|
|[**patch_coaching_appointment_status**](CoachingApi.html#patch_coaching_appointment_status) | Update the status of a coaching appointment|
|[**patch_coaching_notification**](CoachingApi.html#patch_coaching_notification) | Update an existing notification.|
|[**post_coaching_appointment_annotations**](CoachingApi.html#post_coaching_appointment_annotations) | Create a new annotation.|
|[**post_coaching_appointments**](CoachingApi.html#post_coaching_appointments) | Create a new appointment|
{: class="table table-striped"}

<a name="delete_coaching_appointment"></a>

##  delete_coaching_appointment(appointment_id)



Delete an existing appointment

Permission not required if you are the creator of the appointment

Wraps DELETE /api/v2/coaching/appointments/{appointmentId} 

Requires ANY permissions: 

* COACHING:APPOINTMENT:DELETE

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
appointment_id = 'appointment_id_example' # str | The ID of the coaching appointment.

try:
    # Delete an existing appointment
    api_instance.delete_coaching_appointment(appointment_id)
except ApiException as e:
    print "Exception when calling CoachingApi->delete_coaching_appointment: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **appointment_id** | **str**| The ID of the coaching appointment. |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="delete_coaching_appointment_annotation"></a>

##  delete_coaching_appointment_annotation(appointment_id, annotation_id)



Delete an existing annotation

You must have the appropriate permission for the type of annotation you are updating. Permission not required if you are the creator or facilitator of the appointment

Wraps DELETE /api/v2/coaching/appointments/{appointmentId}/annotations/{annotationId} 

Requires ANY permissions: 

* COACHING:ANNOTATION:DELETE
* COACHING:PRIVATEANNOTATION:DELETE

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
appointment_id = 'appointment_id_example' # str | The ID of the coaching appointment.
annotation_id = 'annotation_id_example' # str | The ID of the annotation.

try:
    # Delete an existing annotation
    api_instance.delete_coaching_appointment_annotation(appointment_id, annotation_id)
except ApiException as e:
    print "Exception when calling CoachingApi->delete_coaching_appointment_annotation: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **appointment_id** | **str**| The ID of the coaching appointment. |  |
| **annotation_id** | **str**| The ID of the annotation. |  |
{: class="table table-striped"}

### Return type

void (empty response body)

<a name="get_coaching_appointment"></a>

## [**CoachingAppointmentResponse**](CoachingAppointmentResponse.html) get_coaching_appointment(appointment_id)



Retrieve an appointment

Permission not required if you are the attendee, creator or facilitator of the appointment

Wraps GET /api/v2/coaching/appointments/{appointmentId} 

Requires ANY permissions: 

* COACHING:APPOINTMENT:VIEW

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
appointment_id = 'appointment_id_example' # str | The ID of the coaching appointment.

try:
    # Retrieve an appointment
    api_response = api_instance.get_coaching_appointment(appointment_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CoachingApi->get_coaching_appointment: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **appointment_id** | **str**| The ID of the coaching appointment. |  |
{: class="table table-striped"}

### Return type

[**CoachingAppointmentResponse**](CoachingAppointmentResponse.html)

<a name="get_coaching_appointment_annotation"></a>

## [**CoachingAnnotation**](CoachingAnnotation.html) get_coaching_appointment_annotation(appointment_id, annotation_id)



Retrieve an annotation.

You must have the appropriate permission for the type of annotation you are creating. Permission not required if you are related to the appointment (only the creator or facilitator can view private annotations).

Wraps GET /api/v2/coaching/appointments/{appointmentId}/annotations/{annotationId} 

Requires ANY permissions: 

* COACHING:ANNOTATION:VIEW
* COACHING:PRIVATEANNOTATION:VIEW

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
appointment_id = 'appointment_id_example' # str | The ID of the coaching appointment.
annotation_id = 'annotation_id_example' # str | The ID of the annotation.

try:
    # Retrieve an annotation.
    api_response = api_instance.get_coaching_appointment_annotation(appointment_id, annotation_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CoachingApi->get_coaching_appointment_annotation: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **appointment_id** | **str**| The ID of the coaching appointment. |  |
| **annotation_id** | **str**| The ID of the annotation. |  |
{: class="table table-striped"}

### Return type

[**CoachingAnnotation**](CoachingAnnotation.html)

<a name="get_coaching_appointment_annotations"></a>

## [**CoachingAnnotationList**](CoachingAnnotationList.html) get_coaching_appointment_annotations(appointment_id, page_number=page_number, page_size=page_size)



Get a list of annotations.

You must have the appropriate permission for the type of annotation you are creating. Permission not required if you are related to the appointment (only the creator or facilitator can view private annotations).

Wraps GET /api/v2/coaching/appointments/{appointmentId}/annotations 

Requires ANY permissions: 

* COACHING:ANNOTATION:VIEW
* COACHING:PRIVATEANNOTATION:VIEW

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
appointment_id = 'appointment_id_example' # str | The ID of the coaching appointment.
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get a list of annotations.
    api_response = api_instance.get_coaching_appointment_annotations(appointment_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CoachingApi->get_coaching_appointment_annotations: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **appointment_id** | **str**| The ID of the coaching appointment. |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**CoachingAnnotationList**](CoachingAnnotationList.html)

<a name="get_coaching_appointment_statuses"></a>

## [**CoachingAppointmentStatusDtoList**](CoachingAppointmentStatusDtoList.html) get_coaching_appointment_statuses(appointment_id, page_number=page_number, page_size=page_size)



Get the list of status changes for a coaching appointment.

Permission not required if you are an attendee, creator or facilitator of the appointment

Wraps GET /api/v2/coaching/appointments/{appointmentId}/statuses 

Requires ANY permissions: 

* COACHING:APPOINTMENTSTATUS:VIEW

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
appointment_id = 'appointment_id_example' # str | The ID of the coaching appointment.
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Get the list of status changes for a coaching appointment.
    api_response = api_instance.get_coaching_appointment_statuses(appointment_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CoachingApi->get_coaching_appointment_statuses: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **appointment_id** | **str**| The ID of the coaching appointment. |  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**CoachingAppointmentStatusDtoList**](CoachingAppointmentStatusDtoList.html)

<a name="get_coaching_appointments"></a>

## [**CoachingAppointmentResponseList**](CoachingAppointmentResponseList.html) get_coaching_appointments(user_ids, interval=interval, page_number=page_number, page_size=page_size, statuses=statuses, facilitator_ids=facilitator_ids, sort_order=sort_order)



Get appointments for users and optional date range



Wraps GET /api/v2/coaching/appointments 

Requires ANY permissions: 

* COACHING:APPOINTMENT:VIEW

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
user_ids = ['user_ids_example'] # list[str] | The user IDs for which to retrieve appointments
interval = 'interval_example' # str | Interval string; format is ISO-8601. Separate start and end times with forward slash '/' (optional)
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
statuses = ['statuses_example'] # list[str] | Appointment Statuses to filter by (optional)
facilitator_ids = ['facilitator_ids_example'] # list[str] | The facilitator IDs for which to retrieve appointments (optional)
sort_order = 'sort_order_example' # str | Sort (by due date) either Asc or Desc (optional)

try:
    # Get appointments for users and optional date range
    api_response = api_instance.get_coaching_appointments(user_ids, interval=interval, page_number=page_number, page_size=page_size, statuses=statuses, facilitator_ids=facilitator_ids, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CoachingApi->get_coaching_appointments: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_ids** | [**list[str]**](str.html)| The user IDs for which to retrieve appointments |  |
| **interval** | **str**| Interval string; format is ISO-8601. Separate start and end times with forward slash &#39;/&#39; | [optional]  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **statuses** | [**list[str]**](str.html)| Appointment Statuses to filter by | [optional] <br />**Values**: Scheduled, InProgress, Completed |
| **facilitator_ids** | [**list[str]**](str.html)| The facilitator IDs for which to retrieve appointments | [optional]  |
| **sort_order** | **str**| Sort (by due date) either Asc or Desc | [optional] <br />**Values**: Desc, Asc |
{: class="table table-striped"}

### Return type

[**CoachingAppointmentResponseList**](CoachingAppointmentResponseList.html)

<a name="get_coaching_appointments_me"></a>

## [**CoachingAppointmentResponseList**](CoachingAppointmentResponseList.html) get_coaching_appointments_me(interval=interval, page_number=page_number, page_size=page_size, statuses=statuses, facilitator_ids=facilitator_ids, sort_order=sort_order)



Get my appointments for a given date range



Wraps GET /api/v2/coaching/appointments/me 

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
api_instance = PureCloudPlatformClientV2.CoachingApi()
interval = 'interval_example' # str | Interval string; format is ISO-8601. Separate start and end times with forward slash '/' (optional)
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)
statuses = ['statuses_example'] # list[str] | Appointment Statuses to filter by (optional)
facilitator_ids = ['facilitator_ids_example'] # list[str] | The facilitator IDs for which to retrieve appointments (optional)
sort_order = 'sort_order_example' # str | Sort (by due date) either Asc or Desc (optional)

try:
    # Get my appointments for a given date range
    api_response = api_instance.get_coaching_appointments_me(interval=interval, page_number=page_number, page_size=page_size, statuses=statuses, facilitator_ids=facilitator_ids, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CoachingApi->get_coaching_appointments_me: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **interval** | **str**| Interval string; format is ISO-8601. Separate start and end times with forward slash &#39;/&#39; | [optional]  |
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
| **statuses** | [**list[str]**](str.html)| Appointment Statuses to filter by | [optional] <br />**Values**: Scheduled, InProgress, Completed |
| **facilitator_ids** | [**list[str]**](str.html)| The facilitator IDs for which to retrieve appointments | [optional]  |
| **sort_order** | **str**| Sort (by due date) either Asc or Desc | [optional] <br />**Values**: Desc, Asc |
{: class="table table-striped"}

### Return type

[**CoachingAppointmentResponseList**](CoachingAppointmentResponseList.html)

<a name="get_coaching_notification"></a>

## [**CoachingNotification**](CoachingNotification.html) get_coaching_notification(notification_id)



Get an existing notification

Permission not required if you are the owner of the notification.

Wraps GET /api/v2/coaching/notifications/{notificationId} 

Requires ANY permissions: 

* COACHING:NOTIFICATION:VIEW

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
notification_id = 'notification_id_example' # str | The ID of the notification.

try:
    # Get an existing notification
    api_response = api_instance.get_coaching_notification(notification_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CoachingApi->get_coaching_notification: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **notification_id** | **str**| The ID of the notification. |  |
{: class="table table-striped"}

### Return type

[**CoachingNotification**](CoachingNotification.html)

<a name="get_coaching_notifications"></a>

## [**CoachingNotificationList**](CoachingNotificationList.html) get_coaching_notifications(page_number=page_number, page_size=page_size)



Retrieve the list of your notifications.



Wraps GET /api/v2/coaching/notifications 

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
api_instance = PureCloudPlatformClientV2.CoachingApi()
page_number = 1 # int | Page number (optional) (default to 1)
page_size = 25 # int | Page size (optional) (default to 25)

try:
    # Retrieve the list of your notifications.
    api_response = api_instance.get_coaching_notifications(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CoachingApi->get_coaching_notifications: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_number** | **int**| Page number | [optional] [default to 1] |
| **page_size** | **int**| Page size | [optional] [default to 25] |
{: class="table table-striped"}

### Return type

[**CoachingNotificationList**](CoachingNotificationList.html)

<a name="patch_coaching_appointment"></a>

## [**CoachingAppointmentResponse**](CoachingAppointmentResponse.html) patch_coaching_appointment(appointment_id, body)



Update an existing appointment

Permission not required if you are the creator or facilitator of the appointment

Wraps PATCH /api/v2/coaching/appointments/{appointmentId} 

Requires ANY permissions: 

* COACHING:APPOINTMENT:EDIT

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
appointment_id = 'appointment_id_example' # str | The ID of the coaching appointment.
body = PureCloudPlatformClientV2.UpdateCoachingAppointmentRequest() # UpdateCoachingAppointmentRequest | The new version of the appointment

try:
    # Update an existing appointment
    api_response = api_instance.patch_coaching_appointment(appointment_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CoachingApi->patch_coaching_appointment: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **appointment_id** | **str**| The ID of the coaching appointment. |  |
| **body** | [**UpdateCoachingAppointmentRequest**](UpdateCoachingAppointmentRequest.html)| The new version of the appointment |  |
{: class="table table-striped"}

### Return type

[**CoachingAppointmentResponse**](CoachingAppointmentResponse.html)

<a name="patch_coaching_appointment_annotation"></a>

## [**CoachingAnnotation**](CoachingAnnotation.html) patch_coaching_appointment_annotation(appointment_id, annotation_id, body)



Update an existing annotation.

You must have the appropriate permission for the type of annotation you are updating. Permission not required if you are the creator or facilitator of the appointment

Wraps PATCH /api/v2/coaching/appointments/{appointmentId}/annotations/{annotationId} 

Requires ANY permissions: 

* COACHING:ANNOTATION:EDIT
* COACHING:PRIVATEANNOTATION:EDIT

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
appointment_id = 'appointment_id_example' # str | The ID of the coaching appointment.
annotation_id = 'annotation_id_example' # str | The ID of the annotation.
body = PureCloudPlatformClientV2.CoachingAnnotation() # CoachingAnnotation | The new version of the annotation

try:
    # Update an existing annotation.
    api_response = api_instance.patch_coaching_appointment_annotation(appointment_id, annotation_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CoachingApi->patch_coaching_appointment_annotation: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **appointment_id** | **str**| The ID of the coaching appointment. |  |
| **annotation_id** | **str**| The ID of the annotation. |  |
| **body** | [**CoachingAnnotation**](CoachingAnnotation.html)| The new version of the annotation |  |
{: class="table table-striped"}

### Return type

[**CoachingAnnotation**](CoachingAnnotation.html)

<a name="patch_coaching_appointment_status"></a>

## [**CoachingAppointmentStatusDto**](CoachingAppointmentStatusDto.html) patch_coaching_appointment_status(appointment_id, body)



Update the status of a coaching appointment

Permission not required if you are an attendee, creator or facilitator of the appointment

Wraps PATCH /api/v2/coaching/appointments/{appointmentId}/status 

Requires ANY permissions: 

* COACHING:APPOINTMENTSTATUS:EDIT

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
appointment_id = 'appointment_id_example' # str | The ID of the coaching appointment.
body = PureCloudPlatformClientV2.CoachingAppointmentStatusDto() # CoachingAppointmentStatusDto | Updated status of the coaching appointment

try:
    # Update the status of a coaching appointment
    api_response = api_instance.patch_coaching_appointment_status(appointment_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CoachingApi->patch_coaching_appointment_status: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **appointment_id** | **str**| The ID of the coaching appointment. |  |
| **body** | [**CoachingAppointmentStatusDto**](CoachingAppointmentStatusDto.html)| Updated status of the coaching appointment |  |
{: class="table table-striped"}

### Return type

[**CoachingAppointmentStatusDto**](CoachingAppointmentStatusDto.html)

<a name="patch_coaching_notification"></a>

## [**CoachingNotification**](CoachingNotification.html) patch_coaching_notification(notification_id, body)



Update an existing notification.

Can only update your own notifications.

Wraps PATCH /api/v2/coaching/notifications/{notificationId} 

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
api_instance = PureCloudPlatformClientV2.CoachingApi()
notification_id = 'notification_id_example' # str | The ID of the notification.
body = PureCloudPlatformClientV2.CoachingNotification() # CoachingNotification | Change the read state of a notification

try:
    # Update an existing notification.
    api_response = api_instance.patch_coaching_notification(notification_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CoachingApi->patch_coaching_notification: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **notification_id** | **str**| The ID of the notification. |  |
| **body** | [**CoachingNotification**](CoachingNotification.html)| Change the read state of a notification |  |
{: class="table table-striped"}

### Return type

[**CoachingNotification**](CoachingNotification.html)

<a name="post_coaching_appointment_annotations"></a>

## [**CoachingAnnotation**](CoachingAnnotation.html) post_coaching_appointment_annotations(appointment_id, body)



Create a new annotation.

You must have the appropriate permission for the type of annotation you are creating. Permission not required if you are related to the appointment (only the creator or facilitator can create private annotations).

Wraps POST /api/v2/coaching/appointments/{appointmentId}/annotations 

Requires ANY permissions: 

* COACHING:ANNOTATION:ADD
* COACHING:PRIVATEANNOTATION:ADD

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
appointment_id = 'appointment_id_example' # str | The ID of the coaching appointment.
body = PureCloudPlatformClientV2.CoachingAnnotationCreateRequest() # CoachingAnnotationCreateRequest | The annotation to add

try:
    # Create a new annotation.
    api_response = api_instance.post_coaching_appointment_annotations(appointment_id, body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CoachingApi->post_coaching_appointment_annotations: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **appointment_id** | **str**| The ID of the coaching appointment. |  |
| **body** | [**CoachingAnnotationCreateRequest**](CoachingAnnotationCreateRequest.html)| The annotation to add |  |
{: class="table table-striped"}

### Return type

[**CoachingAnnotation**](CoachingAnnotation.html)

<a name="post_coaching_appointments"></a>

## [**CoachingAppointmentResponse**](CoachingAppointmentResponse.html) post_coaching_appointments(body)



Create a new appointment



Wraps POST /api/v2/coaching/appointments 

Requires ANY permissions: 

* COACHING:APPOINTMENT:ADD

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.CoachingApi()
body = PureCloudPlatformClientV2.CreateCoachingAppointmentRequest() # CreateCoachingAppointmentRequest | The appointment to add

try:
    # Create a new appointment
    api_response = api_instance.post_coaching_appointments(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CoachingApi->post_coaching_appointments: %s\n" % e
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateCoachingAppointmentRequest**](CreateCoachingAppointmentRequest.html)| The appointment to add |  |
{: class="table table-striped"}

### Return type

[**CoachingAppointmentResponse**](CoachingAppointmentResponse.html)
