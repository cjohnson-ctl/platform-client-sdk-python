# coding: utf-8

"""
JourneyApi.py
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class JourneyApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_journey_actiontarget(self, action_target_id, **kwargs):
        """
        Retrieve a single action target.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_journey_actiontarget(action_target_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str action_target_id: ID of the action target. (required)
        :return: ActionTarget
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['action_target_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_journey_actiontarget" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'action_target_id' is set
        if ('action_target_id' not in params) or (params['action_target_id'] is None):
            raise ValueError("Missing the required parameter `action_target_id` when calling `get_journey_actiontarget`")


        resource_path = '/api/v2/journey/actiontargets/{actionTargetId}'.replace('{format}', 'json')
        path_params = {}
        if 'action_target_id' in params:
            path_params['actionTargetId'] = params['action_target_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ActionTarget',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_journey_actiontargets(self, **kwargs):
        """
        Retrieve all action targets.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_journey_actiontargets(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_number: Page number
        :param int page_size: Page size
        :return: ActionTargetListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_number', 'page_size']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_journey_actiontargets" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/journey/actiontargets'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ActionTargetListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_journey_customer_customer_id_segments(self, customer_id_type, customer_id, **kwargs):
        """
        Retrieve segment assignments by customer ID.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_journey_customer_customer_id_segments(customer_id_type, customer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str customer_id_type: Type of ID used to identify customer (e.g. email, cookie, and phone). (required)
        :param str customer_id: Primary identifier of the customer to query for segment assignments. (required)
        :param str page_size: Number of entities to return. Maximum of 200.
        :param str after: The cursor that points to the end of the set of entities that has been returned.
        :param str segment_scope: Scope to filter on. If not specified, both session-scoped and customer-scoped assignments are returned.
        :param str assignment_state: Assignment state to filter on. If not specified, both assigned and unassigned assignments are returned.
        :return: SegmentAssignmentListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id_type', 'customer_id', 'page_size', 'after', 'segment_scope', 'assignment_state']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_journey_customer_customer_id_segments" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'customer_id_type' is set
        if ('customer_id_type' not in params) or (params['customer_id_type'] is None):
            raise ValueError("Missing the required parameter `customer_id_type` when calling `get_journey_customer_customer_id_segments`")
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params) or (params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `get_journey_customer_customer_id_segments`")


        resource_path = '/api/v2/journey/customers/{customerIdType}/{customerId}/segments'.replace('{format}', 'json')
        path_params = {}
        if 'customer_id_type' in params:
            path_params['customerIdType'] = params['customer_id_type']
        if 'customer_id' in params:
            path_params['customerId'] = params['customer_id']

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'after' in params:
            query_params['after'] = params['after']
        if 'segment_scope' in params:
            query_params['segmentScope'] = params['segment_scope']
        if 'assignment_state' in params:
            query_params['assignmentState'] = params['assignment_state']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='SegmentAssignmentListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_journey_externalcontact_segments(self, external_contact_id, **kwargs):
        """
        Retrieve segment assignments by external contact ID.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_journey_externalcontact_segments(external_contact_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str external_contact_id: ID of the external contact to query for segment assignments. (required)
        :param str page_size: Number of entities to return. Maximum of 200.
        :param str after: The cursor that points to the end of the set of entities that has been returned.
        :param str segment_scope: Scope to filter on. If not specified, both session-scoped and customer-scoped assignments are returned.
        :param str assignment_state: Assignment state to filter on. If not specified, both assigned and unassigned assignments are returned.
        :return: SegmentAssignmentListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['external_contact_id', 'page_size', 'after', 'segment_scope', 'assignment_state']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_journey_externalcontact_segments" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'external_contact_id' is set
        if ('external_contact_id' not in params) or (params['external_contact_id'] is None):
            raise ValueError("Missing the required parameter `external_contact_id` when calling `get_journey_externalcontact_segments`")


        resource_path = '/api/v2/journey/externalcontacts/{externalContactId}/segments'.replace('{format}', 'json')
        path_params = {}
        if 'external_contact_id' in params:
            path_params['externalContactId'] = params['external_contact_id']

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'after' in params:
            query_params['after'] = params['after']
        if 'segment_scope' in params:
            query_params['segmentScope'] = params['segment_scope']
        if 'assignment_state' in params:
            query_params['assignmentState'] = params['assignment_state']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='SegmentAssignmentListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_journey_session_segments(self, session_id, **kwargs):
        """
        Retrieve segment assignments by session ID.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_journey_session_segments(session_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str session_id: ID of the session to query for segment assignments. (required)
        :param str page_size: Number of entities to return. Maximum of 200.
        :param str after: The cursor that points to the end of the set of entities that has been returned.
        :param str segment_scope: Scope to filter on. If not specified, both session-scoped and customer-scoped assignments are returned.
        :param str assignment_state: Assignment state to filter on. If not specified, both assigned and unassigned assignments are returned.
        :return: SegmentAssignmentListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['session_id', 'page_size', 'after', 'segment_scope', 'assignment_state']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_journey_session_segments" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'session_id' is set
        if ('session_id' not in params) or (params['session_id'] is None):
            raise ValueError("Missing the required parameter `session_id` when calling `get_journey_session_segments`")


        resource_path = '/api/v2/journey/sessions/{sessionId}/segments'.replace('{format}', 'json')
        path_params = {}
        if 'session_id' in params:
            path_params['sessionId'] = params['session_id']

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'after' in params:
            query_params['after'] = params['after']
        if 'segment_scope' in params:
            query_params['segmentScope'] = params['segment_scope']
        if 'assignment_state' in params:
            query_params['assignmentState'] = params['assignment_state']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='SegmentAssignmentListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def patch_journey_actiontarget(self, action_target_id, **kwargs):
        """
        Update a single action target.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_journey_actiontarget(action_target_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str action_target_id: ID of the action target. (required)
        :param PatchActionTarget body: 
        :return: ActionTarget
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['action_target_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_journey_actiontarget" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'action_target_id' is set
        if ('action_target_id' not in params) or (params['action_target_id'] is None):
            raise ValueError("Missing the required parameter `action_target_id` when calling `patch_journey_actiontarget`")


        resource_path = '/api/v2/journey/actiontargets/{actionTargetId}'.replace('{format}', 'json')
        path_params = {}
        if 'action_target_id' in params:
            path_params['actionTargetId'] = params['action_target_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'PATCH',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ActionTarget',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_analytics_journeys_aggregates_query(self, body, **kwargs):
        """
        Query for journey aggregates
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_analytics_journeys_aggregates_query(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param JourneyAggregationQuery body: query (required)
        :return: JourneyAggregateQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_analytics_journeys_aggregates_query" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_analytics_journeys_aggregates_query`")


        resource_path = '/api/v2/analytics/journeys/aggregates/query'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='JourneyAggregateQueryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_journey_externalcontact_segments(self, external_contact_id, **kwargs):
        """
        Assign/Unassign a segment to/from an external contact or, if a segment is already assigned, update the expiry date of the segment assignment.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_journey_externalcontact_segments(external_contact_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str external_contact_id: ID of the external contact to query for segment assignments. (required)
        :param list[SegmentAssignmentsUpdate] body: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['external_contact_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_journey_externalcontact_segments" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'external_contact_id' is set
        if ('external_contact_id' not in params) or (params['external_contact_id'] is None):
            raise ValueError("Missing the required parameter `external_contact_id` when calling `post_journey_externalcontact_segments`")


        resource_path = '/api/v2/journey/externalcontacts/{externalContactId}/segments'.replace('{format}', 'json')
        path_params = {}
        if 'external_contact_id' in params:
            path_params['externalContactId'] = params['external_contact_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['PureCloud OAuth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
