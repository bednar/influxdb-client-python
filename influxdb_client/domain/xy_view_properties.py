# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six
from influxdb_client.domain.view_properties import ViewProperties


class XYViewProperties(ViewProperties):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'time_format': 'str',
        'type': 'str',
        'queries': 'list[DashboardQuery]',
        'colors': 'list[DashboardColor]',
        'shape': 'str',
        'note': 'str',
        'show_note_when_empty': 'bool',
        'axes': 'Axes',
        'legend': 'Legend',
        'x_column': 'str',
        'y_column': 'str',
        'shade_below': 'bool',
        'position': 'str',
        'geom': 'XYGeom'
    }

    attribute_map = {
        'time_format': 'timeFormat',
        'type': 'type',
        'queries': 'queries',
        'colors': 'colors',
        'shape': 'shape',
        'note': 'note',
        'show_note_when_empty': 'showNoteWhenEmpty',
        'axes': 'axes',
        'legend': 'legend',
        'x_column': 'xColumn',
        'y_column': 'yColumn',
        'shade_below': 'shadeBelow',
        'position': 'position',
        'geom': 'geom'
    }

    def __init__(self, time_format=None, type=None, queries=None, colors=None, shape=None, note=None, show_note_when_empty=None, axes=None, legend=None, x_column=None, y_column=None, shade_below=None, position=None, geom=None):  # noqa: E501
        """XYViewProperties - a model defined in OpenAPI"""  # noqa: E501
        ViewProperties.__init__(self)  # noqa: E501

        self._time_format = None
        self._type = None
        self._queries = None
        self._colors = None
        self._shape = None
        self._note = None
        self._show_note_when_empty = None
        self._axes = None
        self._legend = None
        self._x_column = None
        self._y_column = None
        self._shade_below = None
        self._position = None
        self._geom = None
        self.discriminator = None

        if time_format is not None:
            self.time_format = time_format
        self.type = type
        self.queries = queries
        self.colors = colors
        self.shape = shape
        self.note = note
        self.show_note_when_empty = show_note_when_empty
        self.axes = axes
        self.legend = legend
        if x_column is not None:
            self.x_column = x_column
        if y_column is not None:
            self.y_column = y_column
        if shade_below is not None:
            self.shade_below = shade_below
        self.position = position
        self.geom = geom

    @property
    def time_format(self):
        """Gets the time_format of this XYViewProperties.  # noqa: E501


        :return: The time_format of this XYViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._time_format

    @time_format.setter
    def time_format(self, time_format):
        """Sets the time_format of this XYViewProperties.


        :param time_format: The time_format of this XYViewProperties.  # noqa: E501
        :type: str
        """

        self._time_format = time_format

    @property
    def type(self):
        """Gets the type of this XYViewProperties.  # noqa: E501


        :return: The type of this XYViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this XYViewProperties.


        :param type: The type of this XYViewProperties.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def queries(self):
        """Gets the queries of this XYViewProperties.  # noqa: E501


        :return: The queries of this XYViewProperties.  # noqa: E501
        :rtype: list[DashboardQuery]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Sets the queries of this XYViewProperties.


        :param queries: The queries of this XYViewProperties.  # noqa: E501
        :type: list[DashboardQuery]
        """
        if queries is None:
            raise ValueError("Invalid value for `queries`, must not be `None`")  # noqa: E501

        self._queries = queries

    @property
    def colors(self):
        """Gets the colors of this XYViewProperties.  # noqa: E501

        Colors define color encoding of data into a visualization  # noqa: E501

        :return: The colors of this XYViewProperties.  # noqa: E501
        :rtype: list[DashboardColor]
        """
        return self._colors

    @colors.setter
    def colors(self, colors):
        """Sets the colors of this XYViewProperties.

        Colors define color encoding of data into a visualization  # noqa: E501

        :param colors: The colors of this XYViewProperties.  # noqa: E501
        :type: list[DashboardColor]
        """
        if colors is None:
            raise ValueError("Invalid value for `colors`, must not be `None`")  # noqa: E501

        self._colors = colors

    @property
    def shape(self):
        """Gets the shape of this XYViewProperties.  # noqa: E501


        :return: The shape of this XYViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this XYViewProperties.


        :param shape: The shape of this XYViewProperties.  # noqa: E501
        :type: str
        """
        if shape is None:
            raise ValueError("Invalid value for `shape`, must not be `None`")  # noqa: E501

        self._shape = shape

    @property
    def note(self):
        """Gets the note of this XYViewProperties.  # noqa: E501


        :return: The note of this XYViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this XYViewProperties.


        :param note: The note of this XYViewProperties.  # noqa: E501
        :type: str
        """
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._note = note

    @property
    def show_note_when_empty(self):
        """Gets the show_note_when_empty of this XYViewProperties.  # noqa: E501

        If true, will display note when empty  # noqa: E501

        :return: The show_note_when_empty of this XYViewProperties.  # noqa: E501
        :rtype: bool
        """
        return self._show_note_when_empty

    @show_note_when_empty.setter
    def show_note_when_empty(self, show_note_when_empty):
        """Sets the show_note_when_empty of this XYViewProperties.

        If true, will display note when empty  # noqa: E501

        :param show_note_when_empty: The show_note_when_empty of this XYViewProperties.  # noqa: E501
        :type: bool
        """
        if show_note_when_empty is None:
            raise ValueError("Invalid value for `show_note_when_empty`, must not be `None`")  # noqa: E501

        self._show_note_when_empty = show_note_when_empty

    @property
    def axes(self):
        """Gets the axes of this XYViewProperties.  # noqa: E501


        :return: The axes of this XYViewProperties.  # noqa: E501
        :rtype: Axes
        """
        return self._axes

    @axes.setter
    def axes(self, axes):
        """Sets the axes of this XYViewProperties.


        :param axes: The axes of this XYViewProperties.  # noqa: E501
        :type: Axes
        """
        if axes is None:
            raise ValueError("Invalid value for `axes`, must not be `None`")  # noqa: E501

        self._axes = axes

    @property
    def legend(self):
        """Gets the legend of this XYViewProperties.  # noqa: E501


        :return: The legend of this XYViewProperties.  # noqa: E501
        :rtype: Legend
        """
        return self._legend

    @legend.setter
    def legend(self, legend):
        """Sets the legend of this XYViewProperties.


        :param legend: The legend of this XYViewProperties.  # noqa: E501
        :type: Legend
        """
        if legend is None:
            raise ValueError("Invalid value for `legend`, must not be `None`")  # noqa: E501

        self._legend = legend

    @property
    def x_column(self):
        """Gets the x_column of this XYViewProperties.  # noqa: E501


        :return: The x_column of this XYViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._x_column

    @x_column.setter
    def x_column(self, x_column):
        """Sets the x_column of this XYViewProperties.


        :param x_column: The x_column of this XYViewProperties.  # noqa: E501
        :type: str
        """

        self._x_column = x_column

    @property
    def y_column(self):
        """Gets the y_column of this XYViewProperties.  # noqa: E501


        :return: The y_column of this XYViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._y_column

    @y_column.setter
    def y_column(self, y_column):
        """Sets the y_column of this XYViewProperties.


        :param y_column: The y_column of this XYViewProperties.  # noqa: E501
        :type: str
        """

        self._y_column = y_column

    @property
    def shade_below(self):
        """Gets the shade_below of this XYViewProperties.  # noqa: E501


        :return: The shade_below of this XYViewProperties.  # noqa: E501
        :rtype: bool
        """
        return self._shade_below

    @shade_below.setter
    def shade_below(self, shade_below):
        """Sets the shade_below of this XYViewProperties.


        :param shade_below: The shade_below of this XYViewProperties.  # noqa: E501
        :type: bool
        """

        self._shade_below = shade_below

    @property
    def position(self):
        """Gets the position of this XYViewProperties.  # noqa: E501


        :return: The position of this XYViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this XYViewProperties.


        :param position: The position of this XYViewProperties.  # noqa: E501
        :type: str
        """
        if position is None:
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501

        self._position = position

    @property
    def geom(self):
        """Gets the geom of this XYViewProperties.  # noqa: E501


        :return: The geom of this XYViewProperties.  # noqa: E501
        :rtype: XYGeom
        """
        return self._geom

    @geom.setter
    def geom(self, geom):
        """Sets the geom of this XYViewProperties.


        :param geom: The geom of this XYViewProperties.  # noqa: E501
        :type: XYGeom
        """
        if geom is None:
            raise ValueError("Invalid value for `geom`, must not be `None`")  # noqa: E501

        self._geom = geom

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, XYViewProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
