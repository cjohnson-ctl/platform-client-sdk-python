---
title: FacebookIntegration
---
## FacebookIntegration

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | A unique Integration Id. | |
| **name** | **str** | The name of the Facebook Integration | |
| **app_id** | **str** | The App Id from Facebook messenger | |
| **page_id** | **str** | The Page Id from Facebook messenger | [optional] |
| **status** | **str** | The status of the Facebook Integration | [optional] |
| **recipient** | [**DomainEntityRef**](DomainEntityRef.html) | The recipient reference associated to the Facebook Integration. This recipient is used to associate a flow to an integration | [optional] |
| **date_created** | **datetime** | Date this Integration was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | **datetime** | Date this Integration was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **created_by** | [**DomainEntityRef**](DomainEntityRef.html) | User reference that created this Integration | [optional] |
| **modified_by** | [**DomainEntityRef**](DomainEntityRef.html) | User reference that last modified this Integration | [optional] |
| **version** | **int** | Version number required for updates. | |
| **create_status** | **str** | Status of asynchronous create operation | [optional] |
| **create_error** | [**ErrorBody**](ErrorBody.html) | Error information returned, if createStatus is set to Error | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


