---
title: Leaderboard
---
## Leaderboard

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **division** | [**Division**](Division.html) | The targeted division for this leaderboard | [optional] |
| **metric** | [**Metric**](Metric.html) | The metric id if the leaderboard is about a specific metric | [optional] |
| **date_start_workday** | **date** | Start workday used as the date range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **date_end_workday** | **date** | End workday used as the date range. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd | [optional] |
| **leaders** | [**list[LeaderboardItem]**](LeaderboardItem.html) | The list of leaders generated. | [optional] |
{: class="table table-striped"}

