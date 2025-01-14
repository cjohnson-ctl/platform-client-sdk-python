---
title: LearningModule
---
## LearningModule

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** | The globally unique identifier for the object. | [optional] |
| **name** | **str** | The name of learning module | |
| **created_by** | [**UserReference**](UserReference.html) | The user who created learning module | [optional] |
| **date_created** | **datetime** | The date/time learning module was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **modified_by** | [**UserReference**](UserReference.html) | The user who modified learning module | [optional] |
| **date_modified** | **datetime** | The date/time learning module was modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z | [optional] |
| **version** | **int** | The version of published learning module | [optional] |
| **external_id** | **str** | The external ID of the learning module | [optional] |
| **source** | **str** | The source of the learning module | [optional] |
| **rule** | [**LearningModuleRule**](LearningModuleRule.html) | The rule for learning module; read-only, and only populated when requested via expand param. | [optional] |
| **self_uri** | **str** | The URI for this object | [optional] |
| **is_archived** | **bool** | If true, learning module is archived | [optional] |
| **is_published** | **bool** | If true, learning module is published | [optional] |
| **description** | **str** | The description of learning module | [optional] |
| **completion_time_in_days** | **int** | The completion time of learning module in days | |
| **inform_steps** | [**list[LearningModuleInformStep]**](LearningModuleInformStep.html) | The list of inform steps in a learning module | [optional] |
{: class="table table-striped"}


