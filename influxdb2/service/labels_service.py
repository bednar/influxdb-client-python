# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from influxdb2.api_client import ApiClient


class LabelsService(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_labels_id(self, label_id, **kwargs):  # noqa: E501
        """Delete a label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_labels_id(label_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str label_id: ID of label to delete (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_labels_id_with_http_info(label_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_labels_id_with_http_info(label_id, **kwargs)  # noqa: E501
            return data

    def delete_labels_id_with_http_info(self, label_id, **kwargs):  # noqa: E501
        """Delete a label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_labels_id_with_http_info(label_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str label_id: ID of label to delete (required)
        :param str zap_trace_span: OpenTracing span context
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['label_id', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_labels_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'label_id' is set
        if ('label_id' not in local_var_params or
                local_var_params['label_id'] is None):
            raise ValueError("Missing the required parameter `label_id` when calling `delete_labels_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'label_id' in local_var_params:
            path_params['labelID'] = local_var_params['label_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/labels/{labelID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_labels(self, **kwargs):  # noqa: E501
        """Get all labels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_labels(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str org_id: specifies the organization of the resource
        :return: LabelsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_labels_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_labels_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_labels_with_http_info(self, **kwargs):  # noqa: E501
        """Get all labels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_labels_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zap_trace_span: OpenTracing span context
        :param str org_id: specifies the organization of the resource
        :return: LabelsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['zap_trace_span', 'org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_labels" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'org_id' in local_var_params:
            query_params.append(('orgID', local_var_params['org_id']))  # noqa: E501

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/labels', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LabelsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_labels_id(self, label_id, **kwargs):  # noqa: E501
        """Get a label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_labels_id(label_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str label_id: ID of label to update (required)
        :param str zap_trace_span: OpenTracing span context
        :return: LabelResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_labels_id_with_http_info(label_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_labels_id_with_http_info(label_id, **kwargs)  # noqa: E501
            return data

    def get_labels_id_with_http_info(self, label_id, **kwargs):  # noqa: E501
        """Get a label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_labels_id_with_http_info(label_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str label_id: ID of label to update (required)
        :param str zap_trace_span: OpenTracing span context
        :return: LabelResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['label_id', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_labels_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'label_id' is set
        if ('label_id' not in local_var_params or
                local_var_params['label_id'] is None):
            raise ValueError("Missing the required parameter `label_id` when calling `get_labels_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'label_id' in local_var_params:
            path_params['labelID'] = local_var_params['label_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/labels/{labelID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LabelResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_labels_id(self, label_id, label_update, **kwargs):  # noqa: E501
        """Update a single label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_labels_id(label_id, label_update, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str label_id: ID of label to update (required)
        :param LabelUpdate label_update: label update (required)
        :param str zap_trace_span: OpenTracing span context
        :return: LabelResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_labels_id_with_http_info(label_id, label_update, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_labels_id_with_http_info(label_id, label_update, **kwargs)  # noqa: E501
            return data

    def patch_labels_id_with_http_info(self, label_id, label_update, **kwargs):  # noqa: E501
        """Update a single label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_labels_id_with_http_info(label_id, label_update, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str label_id: ID of label to update (required)
        :param LabelUpdate label_update: label update (required)
        :param str zap_trace_span: OpenTracing span context
        :return: LabelResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['label_id', 'label_update', 'zap_trace_span']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_labels_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'label_id' is set
        if ('label_id' not in local_var_params or
                local_var_params['label_id'] is None):
            raise ValueError("Missing the required parameter `label_id` when calling `patch_labels_id`")  # noqa: E501
        # verify the required parameter 'label_update' is set
        if ('label_update' not in local_var_params or
                local_var_params['label_update'] is None):
            raise ValueError("Missing the required parameter `label_update` when calling `patch_labels_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'label_id' in local_var_params:
            path_params['labelID'] = local_var_params['label_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'zap_trace_span' in local_var_params:
            header_params['Zap-Trace-Span'] = local_var_params['zap_trace_span']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'label_update' in local_var_params:
            body_params = local_var_params['label_update']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/labels/{labelID}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LabelResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_labels(self, label_create_request, **kwargs):  # noqa: E501
        """Create a label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_labels(label_create_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LabelCreateRequest label_create_request: label to create (required)
        :return: LabelResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_labels_with_http_info(label_create_request, **kwargs)  # noqa: E501
        else:
            (data) = self.post_labels_with_http_info(label_create_request, **kwargs)  # noqa: E501
            return data

    def post_labels_with_http_info(self, label_create_request, **kwargs):  # noqa: E501
        """Create a label  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_labels_with_http_info(label_create_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param LabelCreateRequest label_create_request: label to create (required)
        :return: LabelResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['label_create_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_labels" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'label_create_request' is set
        if ('label_create_request' not in local_var_params or
                local_var_params['label_create_request'] is None):
            raise ValueError("Missing the required parameter `label_create_request` when calling `post_labels`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'label_create_request' in local_var_params:
            body_params = local_var_params['label_create_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/labels', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LabelResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)