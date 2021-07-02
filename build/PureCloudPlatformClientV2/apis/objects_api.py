# coding: utf-8

"""
ObjectsApi.py
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


class ObjectsApi(object):
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

    def delete_authorization_division(self, division_id, **kwargs):
        """
        Delete a division.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_authorization_division(division_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str division_id: Division ID (required)
        :param bool force: Force delete this division as well as the grants and objects associated with it
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['division_id', 'force']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_authorization_division" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'division_id' is set
        if ('division_id' not in params) or (params['division_id'] is None):
            raise ValueError("Missing the required parameter `division_id` when calling `delete_authorization_division`")


        resource_path = '/api/v2/authorization/divisions/{divisionId}'.replace('{format}', 'json')
        path_params = {}
        if 'division_id' in params:
            path_params['divisionId'] = params['division_id']

        query_params = {}
        if 'force' in params:
            query_params['force'] = params['force']

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

        response = self.api_client.call_api(resource_path, 'DELETE',
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

    def get_authorization_division(self, division_id, **kwargs):
        """
        Returns an authorization division.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_authorization_division(division_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str division_id: Division ID (required)
        :param bool object_count: Get count of objects in this division, grouped by type
        :return: AuthzDivision
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['division_id', 'object_count']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_authorization_division" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'division_id' is set
        if ('division_id' not in params) or (params['division_id'] is None):
            raise ValueError("Missing the required parameter `division_id` when calling `get_authorization_division`")


        resource_path = '/api/v2/authorization/divisions/{divisionId}'.replace('{format}', 'json')
        path_params = {}
        if 'division_id' in params:
            path_params['divisionId'] = params['division_id']

        query_params = {}
        if 'object_count' in params:
            query_params['objectCount'] = params['object_count']

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
                                            response_type='AuthzDivision',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_authorization_divisions(self, **kwargs):
        """
        Retrieve a list of all divisions defined for the organization
        Request specific divisions by id using a query param \"id\", e.g.  ?id=5f777167-63be-4c24-ad41-374155d9e28b&id=72e9fb25-c484-488d-9312-7acba82435b3

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_authorization_divisions(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page_size: The total page size requested
        :param int page_number: The page number requested
        :param str sort_by: variable name requested to sort by
        :param list[str] expand: variable name requested by expand list
        :param str next_page: next page token
        :param str previous_page: Previous page token
        :param bool object_count: Include the count of objects contained in the division
        :param list[str] id: Optionally request specific divisions by their IDs
        :param str name: Search term to filter by division name
        :return: AuthzDivisionEntityListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page_number', 'sort_by', 'expand', 'next_page', 'previous_page', 'object_count', 'id', 'name']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_authorization_divisions" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/authorization/divisions'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'sort_by' in params:
            query_params['sortBy'] = params['sort_by']
        if 'expand' in params:
            query_params['expand'] = params['expand']
        if 'next_page' in params:
            query_params['nextPage'] = params['next_page']
        if 'previous_page' in params:
            query_params['previousPage'] = params['previous_page']
        if 'object_count' in params:
            query_params['objectCount'] = params['object_count']
        if 'id' in params:
            query_params['id'] = params['id']
        if 'name' in params:
            query_params['name'] = params['name']

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
                                            response_type='AuthzDivisionEntityListing',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_authorization_divisions_home(self, **kwargs):
        """
        Retrieve the home division for the organization.
        Will not include object counts.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_authorization_divisions_home(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: AuthzDivision
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_authorization_divisions_home" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/authorization/divisions/home'.replace('{format}', 'json')
        path_params = {}

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
                                            response_type='AuthzDivision',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_authorization_divisions_limit(self, **kwargs):
        """
        Returns the maximum allowed number of divisions.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_authorization_divisions_limit(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_authorization_divisions_limit" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/authorization/divisions/limit'.replace('{format}', 'json')
        path_params = {}

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
                                            response_type='int',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_authorization_division_object(self, division_id, object_type, body, **kwargs):
        """
        Assign a list of objects to a division
        Set the division of a specified list of objects. The objects must all be of the same type, one of:  CAMPAIGN, MANAGEMENTUNIT, FLOW, QUEUE, DATATABLES or USER.  The body of the request is a list of object IDs, which are expected to be  GUIDs, e.g. [\"206ce31f-61ec-40ed-a8b1-be6f06303998\",\"250a754e-f5e4-4f51-800f-a92f09d3bf8c\"]

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_authorization_division_object(division_id, object_type, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str division_id: Division ID (required)
        :param str object_type: The type of the objects. Must be one of the valid object types (required)
        :param list[str] body: Object Id List (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['division_id', 'object_type', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_authorization_division_object" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'division_id' is set
        if ('division_id' not in params) or (params['division_id'] is None):
            raise ValueError("Missing the required parameter `division_id` when calling `post_authorization_division_object`")
        # verify the required parameter 'object_type' is set
        if ('object_type' not in params) or (params['object_type'] is None):
            raise ValueError("Missing the required parameter `object_type` when calling `post_authorization_division_object`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_authorization_division_object`")


        resource_path = '/api/v2/authorization/divisions/{divisionId}/objects/{objectType}'.replace('{format}', 'json')
        path_params = {}
        if 'division_id' in params:
            path_params['divisionId'] = params['division_id']
        if 'object_type' in params:
            path_params['objectType'] = params['object_type']

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

    def post_authorization_division_restore(self, division_id, body, **kwargs):
        """
        Recreate a previously deleted division.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_authorization_division_restore(division_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str division_id: Division ID (required)
        :param AuthzDivision body: Recreated division data (required)
        :return: AuthzDivision
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['division_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_authorization_division_restore" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'division_id' is set
        if ('division_id' not in params) or (params['division_id'] is None):
            raise ValueError("Missing the required parameter `division_id` when calling `post_authorization_division_restore`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_authorization_division_restore`")


        resource_path = '/api/v2/authorization/divisions/{divisionId}/restore'.replace('{format}', 'json')
        path_params = {}
        if 'division_id' in params:
            path_params['divisionId'] = params['division_id']

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
                                            response_type='AuthzDivision',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_authorization_divisions(self, body, **kwargs):
        """
        Create a division.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_authorization_divisions(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param AuthzDivision body: Division (required)
        :return: AuthzDivision
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
                    " to method post_authorization_divisions" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_authorization_divisions`")


        resource_path = '/api/v2/authorization/divisions'.replace('{format}', 'json')
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
                                            response_type='AuthzDivision',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def put_authorization_division(self, division_id, body, **kwargs):
        """
        Update a division.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_authorization_division(division_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str division_id: Division ID (required)
        :param AuthzDivision body: Updated division data (required)
        :return: AuthzDivision
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['division_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_authorization_division" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'division_id' is set
        if ('division_id' not in params) or (params['division_id'] is None):
            raise ValueError("Missing the required parameter `division_id` when calling `put_authorization_division`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_authorization_division`")


        resource_path = '/api/v2/authorization/divisions/{divisionId}'.replace('{format}', 'json')
        path_params = {}
        if 'division_id' in params:
            path_params['divisionId'] = params['division_id']

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

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='AuthzDivision',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
