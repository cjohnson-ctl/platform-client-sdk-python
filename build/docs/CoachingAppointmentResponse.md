---
title: CoachingAppointmentResponse
---
## CoachingAppointmentResponse

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of coaching appointment | [optional] |
| **description** | **str** | The description of coaching appointment | [optional] |
| **date_start** | **datetime** | The date/time the coaching appointment starts. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **length_in_minutes** | **int** | The duration of coaching appointment in minutes | [optional] |
| **status** | **str** | The status of coaching appointment | [optional] |
| **facilitator** | [**UserReference**](UserReference.html) | The facilitator of coaching appointment | [optional] |
| **attendees** | [**list[UserReference]**](UserReference.html) | The list of attendees attending the coaching | [optional] |
| **created_by** | [**UserReference**](UserReference.html) | The user who created the coaching appointment | [optional] |
| **date_created** | **datetime** | The date/time the coaching appointment was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **modified_by** | [**UserReference**](UserReference.html) | The last user to modify the coaching appointment | [optional] |
| **date_modified** | **datetime** | The date/time the coaching appointment was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **conversations** | [**list[ConversationReference]**](ConversationReference.html) | The list of conversations associated with coaching appointment. | [optional] |
| **documents** | [**list[DocumentReference]**](DocumentReference.html) | The list of documents associated with coaching appointment. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}

