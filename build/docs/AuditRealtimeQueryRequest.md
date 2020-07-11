---
title: AuditRealtimeQueryRequest
---
## AuditRealtimeQueryRequest

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **interval** | **str** | Date and time range of data to query. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | |
| **service_name** | **str** | Name of the service to query audits for. | |
| **filters** | [**list[AuditQueryFilter]**](AuditQueryFilter.html) | Additional filters for the query. | [optional] |
| **sort** | [**list[AuditQuerySort]**](AuditQuerySort.html) | Sort parameter for the query. | [optional] |
| **page_number** | **int** | Page number | [optional] |
| **page_size** | **int** | Page size | [optional] |
{: class="table table-striped"}

