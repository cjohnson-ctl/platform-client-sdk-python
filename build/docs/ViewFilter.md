---
title: ViewFilter
---
## ViewFilter

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **media_types** | **list[str]** | The media types are used to filter the view | [optional] |
| **queue_ids** | **list[str]** | The queue ids are used to filter the view | [optional] |
| **skill_ids** | **list[str]** | The skill ids are used to filter the view | [optional] |
| **skill_groups** | **list[str]** | The skill groups used to filter the view | [optional] |
| **language_ids** | **list[str]** | The language ids are used to filter the view | [optional] |
| **language_groups** | **list[str]** | The language groups used to filter the view | [optional] |
| **directions** | **list[str]** | The directions are used to filter the view | [optional] |
| **originating_directions** | **list[str]** | The list of orginating directions used to filter the view | [optional] |
| **wrap_up_codes** | **list[str]** | The wrap up codes are used to filter the view | [optional] |
| **dnis_list** | **list[str]** | The dnis list is used to filter the view | [optional] |
| **session_dnis_list** | **list[str]** | The list of session dnis used to filter the view | [optional] |
| **filter_queues_by_user_ids** | **list[str]** | The user ids are used to fetch associated queues for the view | [optional] |
| **filter_users_by_queue_ids** | **list[str]** | The queue ids are used to fetch associated users for the view | [optional] |
| **user_ids** | **list[str]** | The user ids are used to filter the view | [optional] |
| **address_tos** | **list[str]** | The address To values are used to filter the view | [optional] |
| **address_froms** | **list[str]** | The address from values are used to filter the view | [optional] |
| **outbound_campaign_ids** | **list[str]** | The outbound campaign ids are used to filter the view | [optional] |
| **outbound_contact_list_ids** | **list[str]** | The outbound contact list ids are used to filter the view | [optional] |
| **contact_ids** | **list[str]** | The contact ids are used to filter the view | [optional] |
| **external_contact_ids** | **list[str]** | The external contact ids are used to filter the view | [optional] |
| **external_org_ids** | **list[str]** | The external org ids are used to filter the view | [optional] |
| **ani_list** | **list[str]** | The ani list ids are used to filter the view | [optional] |
| **durations_milliseconds** | [**list[NumericRange]**](NumericRange.html) | The durations in milliseconds used to filter the view | [optional] |
| **acd_durations_milliseconds** | [**list[NumericRange]**](NumericRange.html) | The acd durations in milliseconds used to filter the view | [optional] |
| **talk_durations_milliseconds** | [**list[NumericRange]**](NumericRange.html) | The talk durations in milliseconds used to filter the view | [optional] |
| **acw_durations_milliseconds** | [**list[NumericRange]**](NumericRange.html) | The acw durations in milliseconds used to filter the view | [optional] |
| **handle_durations_milliseconds** | [**list[NumericRange]**](NumericRange.html) | The handle durations in milliseconds used to filter the view | [optional] |
| **hold_durations_milliseconds** | [**list[NumericRange]**](NumericRange.html) | The hold durations in milliseconds used to filter the view | [optional] |
| **abandon_durations_milliseconds** | [**list[NumericRange]**](NumericRange.html) | The abandon durations in milliseconds used to filter the view | [optional] |
| **evaluation_score** | [**NumericRange**](NumericRange.html) | The evaluationScore is used to filter the view | [optional] |
| **evaluation_critical_score** | [**NumericRange**](NumericRange.html) | The evaluationCriticalScore is used to filter the view | [optional] |
| **evaluation_form_ids** | **list[str]** | The evaluation form ids are used to filter the view | [optional] |
| **evaluated_agent_ids** | **list[str]** | The evaluated agent ids are used to filter the view | [optional] |
| **evaluator_ids** | **list[str]** | The evaluator ids are used to filter the view | [optional] |
| **transferred** | **bool** | Indicates filtering for transfers | [optional] |
| **abandoned** | **bool** | Indicates filtering for abandons | [optional] |
| **answered** | **bool** | Indicates filtering for answered interactions | [optional] |
| **message_types** | **list[str]** | The message media types used to filter the view | [optional] |
| **division_ids** | **list[str]** | The divison Ids used to filter the view | [optional] |
| **survey_form_ids** | **list[str]** | The survey form ids used to filter the view | [optional] |
| **survey_total_score** | [**NumericRange**](NumericRange.html) | The survey total score used to filter the view | [optional] |
| **survey_nps_score** | [**NumericRange**](NumericRange.html) | The survey NPS score used to filter the view | [optional] |
| **mos** | [**NumericRange**](NumericRange.html) | The desired range for mos values | [optional] |
| **survey_question_group_score** | [**NumericRange**](NumericRange.html) | The survey question group score used to filter the view | [optional] |
| **survey_promoter_score** | [**NumericRange**](NumericRange.html) | The survey promoter score used to filter the view | [optional] |
| **survey_form_context_ids** | **list[str]** | The list of survey form context ids used to filter the view | [optional] |
| **conversation_ids** | **list[str]** | The list of conversation ids used to filter the view | [optional] |
| **sip_call_ids** | **list[str]** | The list of SIP call ids used to filter the view | [optional] |
| **is_ended** | **bool** | Indicates filtering for ended | [optional] |
| **is_surveyed** | **bool** | Indicates filtering for survey | [optional] |
| **survey_scores** | [**list[NumericRange]**](NumericRange.html) | The list of survey score ranges used to filter the view | [optional] |
| **promoter_scores** | [**list[NumericRange]**](NumericRange.html) | The list of promoter score ranges used to filter the view | [optional] |
| **is_campaign** | **bool** | Indicates filtering for campaign | [optional] |
| **survey_statuses** | **list[str]** | The list of survey statuses used to filter the view | [optional] |
| **conversation_properties** | [**ConversationProperties**](ConversationProperties.html) | A grouping of conversation level filters | [optional] |
| **is_blind_transferred** | **bool** | Indicates filtering for blind transferred | [optional] |
| **is_consulted** | **bool** | Indicates filtering for consulted | [optional] |
| **is_consult_transferred** | **bool** | Indicates filtering for consult transferred | [optional] |
| **remote_participants** | **list[str]** | The list of remote participants used to filter the view | [optional] |
| **flow_ids** | **list[str]** | The list of flow Ids | [optional] |
| **flow_outcome_ids** | **list[str]** | A list of outcome ids of the flow | [optional] |
| **flow_outcome_values** | **list[str]** | A list of outcome values of the flow | [optional] |
| **flow_destination_types** | **list[str]** | The list of destination types of the flow | [optional] |
| **flow_disconnect_reasons** | **list[str]** | The list of reasons for the flow to disconnect | [optional] |
| **flow_types** | **list[str]** | A list of types of the flow | [optional] |
| **flow_entry_types** | **list[str]** | A list of types of the flow entry | [optional] |
| **flow_entry_reasons** | **list[str]** | A list of reasons of flow entry | [optional] |
| **flow_versions** | **list[str]** | A list of versions of a flow | [optional] |
| **group_ids** | **list[str]** | A list of directory group ids | [optional] |
| **has_journey_customer_id** | **bool** | Indicates filtering for journey customer id | [optional] |
| **has_journey_action_map_id** | **bool** | Indicates filtering for Journey action map id | [optional] |
| **has_journey_visit_id** | **bool** | Indicates filtering for Journey visit id | [optional] |
| **has_media** | **bool** | Indicates filtering for presence of MMS media | [optional] |
| **role_ids** | **list[str]** | The role Ids used to filter the view | [optional] |
| **reports_tos** | **list[str]** | The report to user IDs used to filter the view | [optional] |
| **location_ids** | **list[str]** | The location Ids used to filter the view | [optional] |
| **flow_out_types** | **list[str]** | A list of flow out types | [optional] |
| **provider_list** | **list[str]** | A list of providers | [optional] |
| **callback_number_list** | **list[str]** | A list of callback numbers or substrings of numbers (ex: [\&quot;317\&quot;, \&quot;13172222222\&quot;]) | [optional] |
| **callback_interval** | **str** | An interval of time to filter for scheduled callbacks. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional] |
| **used_routing_types** | **list[str]** | A list of routing types used | [optional] |
| **requested_routing_types** | **list[str]** | A list of routing types requested | [optional] |
| **has_agent_assist_id** | **bool** | Indicates filtering for agent assist id | [optional] |
| **transcripts** | [**list[Transcripts]**](Transcripts.html) | A list of transcript contents requested | [optional] |
| **transcript_languages** | **list[str]** | A list of transcript languages requested | [optional] |
| **participant_purposes** | **list[str]** | A list of participant purpose requested | [optional] |
| **show_first_queue** | **bool** | Indicates filtering for first queue data | [optional] |
| **team_ids** | **list[str]** | The team ids used to filter the view data | [optional] |
| **filter_users_by_team_ids** | **list[str]** | The team ids are used to fetch associated users for the view | [optional] |
| **journey_action_map_ids** | **list[str]** | The journey action map ids are used to fetch action maps for the associated view | [optional] |
| **journey_outcome_ids** | **list[str]** | The journey outcome ids are used to fetch outcomes for the associated view | [optional] |
| **journey_segment_ids** | **list[str]** | The journey segment ids are used to fetch segments for the associated view | [optional] |
| **journey_action_map_types** | **list[str]** | The journey action map types are used to filter action map data for the associated view | [optional] |
| **development_role_list** | **list[str]** | The list of development roles used to filter agent development view | [optional] |
| **development_type_list** | **list[str]** | The list of development types used to filter agent development view | [optional] |
| **development_status_list** | **list[str]** | The list of development status used to filter agent development view | [optional] |
| **development_module_ids** | **list[str]** | The list of development moduleIds used to filter agent development view | [optional] |
| **development_activity_overdue** | **bool** | Indicates filtering for development activities | [optional] |
| **customer_sentiment_score** | [**NumericRange**](NumericRange.html) | The customer sentiment score used to filter the view | [optional] |
| **customer_sentiment_trend** | [**NumericRange**](NumericRange.html) | The customer sentiment trend used to filter the view | [optional] |
| **flow_transfer_targets** | **list[str]** | The list of transfer targets used to filter flow data | [optional] |
| **development_name** | **str** | Filter for development name | [optional] |
| **topic_ids** | **list[str]** | Represents the topics detected in the transcript | [optional] |
| **external_tags** | **list[str]** | The list of external Tags used to filter conversation data | [optional] |
| **is_not_responding** | **bool** | Indicates filtering for not responding users | [optional] |
| **is_authenticated** | **bool** | Indicates filtering for the authenticated chat | [optional] |
| **bot_ids** | **list[str]** | The list of bot IDs used to filter bot views | [optional] |
| **bot_versions** | **list[str]** | The list of bot versions used to filter bot views | [optional] |
| **bot_message_types** | **list[str]** | The list of bot message types used to filter bot views | [optional] |
| **bot_provider_list** | **list[str]** | The list of bot providers used to filter bot views | [optional] |
| **bot_product_list** | **list[str]** | The list of bot products used to filter bot views | [optional] |
| **bot_recognition_failure_reason_list** | **list[str]** | The list of bot recognition failure reasons used to filter bot views | [optional] |
| **bot_intent_list** | **list[str]** | The list of bot intents used to filter bot views | [optional] |
| **bot_final_intent_list** | **list[str]** | The list of bot final intents used to filter bot views | [optional] |
| **bot_slot_list** | **list[str]** | The list of bot slots used to filter bot views | [optional] |
| **bot_result_list** | **list[str]** | The list of bot results used to filter bot views | [optional] |
{: class="table table-striped"}


