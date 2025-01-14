---
title: TimeOffRequest
---
## TimeOffRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The id of the time off request | |
| **user** | [**UserReference**](UserReference.html) | The user that the time off request belongs to | |
| **is_full_day_request** | **bool** | Whether this is a full day request (false means partial day) | [optional] |
| **marked_as_read** | **bool** | Whether this request has been marked as read by the agent | [optional] |
| **activity_code_id** | **str** | The ID of the activity code associated with this time off request. Activity code must be of the TimeOff category | [optional] |
| **status** | **str** | The status of this time off request | [optional] |
| **partial_day_start_date_times** | **list[datetime]** | A set of start date-times in ISO-8601 format for partial day requests.  Will be not empty if isFullDayRequest == false | [optional] |
| **full_day_management_unit_dates** | **list[str]** | A set of dates in yyyy-MM-dd format.  Should be interpreted in the management unit&#39;s configured time zone.  Will be not empty if isFullDayRequest == true | [optional] |
| **daily_duration_minutes** | **int** | The daily duration of this time off request in minutes | [optional] |
| **notes** | **str** | Notes about the time off request | [optional] |
| **submitted_by** | [**UserReference**](UserReference.html) | The user who submitted this time off request | [optional] |
| **submitted_date** | **datetime** | The timestamp when this request was submitted. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **reviewed_by** | [**UserReference**](UserReference.html) | The user who reviewed this time off request | [optional] |
| **reviewed_date** | **datetime** | The timestamp when this request was reviewed. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **metadata** | [**WfmVersionedEntityMetadata**](WfmVersionedEntityMetadata.html) | The version metadata of the time off request | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


