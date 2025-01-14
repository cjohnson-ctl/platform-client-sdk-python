---
title: ConversationEventTopicMessage
---
## ConversationEventTopicMessage

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **id** | **str** |  | [optional] |
| **state** | **str** |  | [optional] |
| **held** | **bool** |  | [optional] |
| **error_info** | [**ConversationEventTopicErrorDetails**](ConversationEventTopicErrorDetails.html) |  | [optional] |
| **provider** | **str** |  | [optional] |
| **script_id** | **str** |  | [optional] |
| **peer_id** | **str** |  | [optional] |
| **disconnect_type** | **str** |  | [optional] |
| **start_hold_time** | **datetime** |  | [optional] |
| **connected_time** | **datetime** |  | [optional] |
| **disconnected_time** | **datetime** |  | [optional] |
| **to_address** | [**ConversationEventTopicAddress**](ConversationEventTopicAddress.html) |  | [optional] |
| **from_address** | [**ConversationEventTopicAddress**](ConversationEventTopicAddress.html) |  | [optional] |
| **messages** | [**list[ConversationEventTopicMessageDetails]**](ConversationEventTopicMessageDetails.html) |  | [optional] |
| **messages_transcript_uri** | **str** |  | [optional] |
| **type** | **str** |  | [optional] |
| **recipient_country** | **str** |  | [optional] |
| **recipient_type** | **str** |  | [optional] |
| **journey_context** | [**ConversationEventTopicJourneyContext**](ConversationEventTopicJourneyContext.html) |  | [optional] |
| **wrapup** | [**ConversationEventTopicWrapup**](ConversationEventTopicWrapup.html) |  | [optional] |
| **after_call_work** | [**ConversationEventTopicAfterCallWork**](ConversationEventTopicAfterCallWork.html) |  | [optional] |
| **after_call_work_required** | **bool** |  | [optional] |
| **additional_properties** | **object** |  | [optional] |
{: class="table table-striped"}


