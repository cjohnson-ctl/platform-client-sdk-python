# coding: utf-8

"""
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

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

class ContentGeneric(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ContentGeneric - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'title': 'str',
            'description': 'str',
            'image': 'str',
            'video': 'str',
            'actions': 'ContentActions',
            'components': 'list[ButtonComponent]'
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'description': 'description',
            'image': 'image',
            'video': 'video',
            'actions': 'actions',
            'components': 'components'
        }

        self._id = None
        self._title = None
        self._description = None
        self._image = None
        self._video = None
        self._actions = None
        self._components = None

    @property
    def id(self):
        """
        Gets the id of this ContentGeneric.
        An ID assigned to this rich message content. Each instance inside the content array has a unique ID.

        :return: The id of this ContentGeneric.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ContentGeneric.
        An ID assigned to this rich message content. Each instance inside the content array has a unique ID.

        :param id: The id of this ContentGeneric.
        :type: str
        """
        
        self._id = id

    @property
    def title(self):
        """
        Gets the title of this ContentGeneric.
        Text to show in the title row

        :return: The title of this ContentGeneric.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this ContentGeneric.
        Text to show in the title row

        :param title: The title of this ContentGeneric.
        :type: str
        """
        
        self._title = title

    @property
    def description(self):
        """
        Gets the description of this ContentGeneric.
        Text to show in the description row. This is immediately below the title

        :return: The description of this ContentGeneric.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ContentGeneric.
        Text to show in the description row. This is immediately below the title

        :param description: The description of this ContentGeneric.
        :type: str
        """
        
        self._description = description

    @property
    def image(self):
        """
        Gets the image of this ContentGeneric.
        Path or URI to an image file

        :return: The image of this ContentGeneric.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this ContentGeneric.
        Path or URI to an image file

        :param image: The image of this ContentGeneric.
        :type: str
        """
        
        self._image = image

    @property
    def video(self):
        """
        Gets the video of this ContentGeneric.
        Path or URI to a video file

        :return: The video of this ContentGeneric.
        :rtype: str
        """
        return self._video

    @video.setter
    def video(self, video):
        """
        Sets the video of this ContentGeneric.
        Path or URI to a video file

        :param video: The video of this ContentGeneric.
        :type: str
        """
        
        self._video = video

    @property
    def actions(self):
        """
        Gets the actions of this ContentGeneric.
        User actions available on the content. All actions are optional and all actions are executed simultaneously.

        :return: The actions of this ContentGeneric.
        :rtype: ContentActions
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this ContentGeneric.
        User actions available on the content. All actions are optional and all actions are executed simultaneously.

        :param actions: The actions of this ContentGeneric.
        :type: ContentActions
        """
        
        self._actions = actions

    @property
    def components(self):
        """
        Gets the components of this ContentGeneric.
        An array of component objects

        :return: The components of this ContentGeneric.
        :rtype: list[ButtonComponent]
        """
        return self._components

    @components.setter
    def components(self, components):
        """
        Sets the components of this ContentGeneric.
        An array of component objects

        :param components: The components of this ContentGeneric.
        :type: list[ButtonComponent]
        """
        
        self._components = components

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_json(self):
        """
        Returns the model as raw JSON
        """
        return json.dumps(sanitize_for_serialization(self.to_dict()))

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

