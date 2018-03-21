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
        auth_settings = ['PureCloud Auth']

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
        Set the division of a list of objects. The objects must all be of the same type: CAMPAIGN, CONTACTLIST, DNCLIST, MANAGEMENTUNIT, FLOW, QUEUE, USER
        

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
        :return: list[AuthzTypedObject]
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
        auth_settings = ['PureCloud Auth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[AuthzTypedObject]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
