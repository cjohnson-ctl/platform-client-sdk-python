---
title: KnowledgeTraining
---
## KnowledgeTraining

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** |  | [optional] |
| **date_triggered** | **datetime** | Trigger date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **date_completed** | **datetime** | Training completed date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **status** | **str** | Training status | [optional] |
| **language_code** | **str** | Actual language of the Training | [optional] |
| **knowledge_base** | [**KnowledgeBase**](KnowledgeBase.html) | Knowledge base which Training does belong to | [optional] |
| **error_message** | **str** | Any error message during the Training or Promote action. | [optional] |
| **knowledge_documents_state** | **str** | State of the Trained Documents, which can be one of these Draft, Active, Discarded, Archived. | [optional] |
| **date_promoted** | **datetime** | Trained Documents Promoted date-time. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
{: class="table table-striped"}

