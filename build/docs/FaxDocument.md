---
title: FaxDocument
---
## FaxDocument

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **date_created** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **date_modified** | **datetime** | Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **content_uri** | **str** |  | [optional] |
| **workspace** | [**DomainEntityRef**](DomainEntityRef.html) |  | [optional] |
| **created_by** | [**DomainEntityRef**](DomainEntityRef.html) |  | [optional] |
| **content_type** | **str** |  | [optional] |
| **content_length** | **int** |  | [optional] |
| **filename** | **str** |  | [optional] |
| **read** | **bool** |  | [optional] |
| **page_count** | **int** |  | [optional] |
| **caller_address** | **str** |  | [optional] |
| **receiver_address** | **str** |  | [optional] |
| **thumbnails** | [**list[DocumentThumbnail]**](DocumentThumbnail.html) |  | [optional] |
| **sharing_uri** | **str** |  | [optional] |
| **download_sharing_uri** | **str** |  | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}


