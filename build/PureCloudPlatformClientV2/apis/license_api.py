# coding: utf-8

"""
LicenseApi.py
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


class LicenseApi(object):
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

    def get_license_definition(self, license_id, **kwargs):
        """
        Get PureCloud license definition.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_license_definition(license_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str license_id: ID (required)
        :return: LicenseDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['license_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_license_definition" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'license_id' is set
        if ('license_id' not in params) or (params['license_id'] is None):
            raise ValueError("Missing the required parameter `license_id` when calling `get_license_definition`")


        resource_path = '/api/v2/license/definitions/{licenseId}'.replace('{format}', 'json')
        path_params = {}
        if 'license_id' in params:
            path_params['licenseId'] = params['license_id']

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
                                            response_type='LicenseDefinition',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_license_definitions(self, **kwargs):
        """
        Get all PureCloud license definitions available for the organization.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_license_definitions(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[LicenseDefinition]
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
                    " to method get_license_definitions" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/license/definitions'.replace('{format}', 'json')
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
                                            response_type='list[LicenseDefinition]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_license_organization(self, **kwargs):
        """
        Get license assignments for the organization.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_license_organization(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: LicenseOrganization
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
                    " to method get_license_organization" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/license/organization'.replace('{format}', 'json')
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
                                            response_type='LicenseOrganization',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_license_toggle(self, feature_name, **kwargs):
        """
        Get PureCloud license feature toggle value.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_license_toggle(feature_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str feature_name: featureName (required)
        :return: LicenseOrgToggle
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['feature_name']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_license_toggle" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'feature_name' is set
        if ('feature_name' not in params) or (params['feature_name'] is None):
            raise ValueError("Missing the required parameter `feature_name` when calling `get_license_toggle`")


        resource_path = '/api/v2/license/toggles/{featureName}'.replace('{format}', 'json')
        path_params = {}
        if 'feature_name' in params:
            path_params['featureName'] = params['feature_name']

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
                                            response_type='LicenseOrgToggle',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_license_user(self, user_id, **kwargs):
        """
        Get licenses for specified user.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_license_user(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str user_id: ID (required)
        :return: LicenseUser
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_license_user" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_license_user`")


        resource_path = '/api/v2/license/users/{userId}'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

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
                                            response_type='LicenseUser',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_license_organization(self, **kwargs):
        """
        Update the organization's license assignments in a batch.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_license_organization(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param LicenseBatchAssignmentRequest body: The license assignments to update.
        :return: list[LicenseUpdateStatus]
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
                    " to method post_license_organization" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/license/organization'.replace('{format}', 'json')
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
                                            response_type='list[LicenseUpdateStatus]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_license_toggle(self, feature_name, **kwargs):
        """
        Switch PureCloud license feature toggle value.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_license_toggle(feature_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str feature_name: featureName (required)
        :return: LicenseOrgToggle
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['feature_name']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_license_toggle" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'feature_name' is set
        if ('feature_name' not in params) or (params['feature_name'] is None):
            raise ValueError("Missing the required parameter `feature_name` when calling `post_license_toggle`")


        resource_path = '/api/v2/license/toggles/{featureName}'.replace('{format}', 'json')
        path_params = {}
        if 'feature_name' in params:
            path_params['featureName'] = params['feature_name']

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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='LicenseOrgToggle',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def post_license_users(self, **kwargs):
        """
        Fetch user licenses in a batch.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_license_users(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] body: The user IDs to fetch.
        :return: dict(str, object)
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
                    " to method post_license_users" % key
                )
            params[key] = val
        del params['kwargs']



        resource_path = '/api/v2/license/users'.replace('{format}', 'json')
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
                                            response_type='dict(str, object)',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
