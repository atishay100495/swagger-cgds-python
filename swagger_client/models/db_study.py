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


class DBStudy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DBStudy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'citation': 'str',
            'description': 'str',
            'groups': 'str',
            'id': 'str',
            'name': 'str',
            'pmid': 'int',
            'short_name': 'str',
            'type_of_cancer': 'str'
        }

        self.attribute_map = {
            'citation': 'citation',
            'description': 'description',
            'groups': 'groups',
            'id': 'id',
            'name': 'name',
            'pmid': 'pmid',
            'short_name': 'short_name',
            'type_of_cancer': 'type_of_cancer'
        }

        self._citation = None
        self._description = None
        self._groups = None
        self._id = None
        self._name = None
        self._pmid = None
        self._short_name = None
        self._type_of_cancer = None

    @property
    def citation(self):
        """
        Gets the citation of this DBStudy.


        :return: The citation of this DBStudy.
        :rtype: str
        """
        return self._citation

    @citation.setter
    def citation(self, citation):
        """
        Sets the citation of this DBStudy.


        :param citation: The citation of this DBStudy.
        :type: str
        """
        self._citation = citation

    @property
    def description(self):
        """
        Gets the description of this DBStudy.


        :return: The description of this DBStudy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DBStudy.


        :param description: The description of this DBStudy.
        :type: str
        """
        self._description = description

    @property
    def groups(self):
        """
        Gets the groups of this DBStudy.


        :return: The groups of this DBStudy.
        :rtype: str
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this DBStudy.


        :param groups: The groups of this DBStudy.
        :type: str
        """
        self._groups = groups

    @property
    def id(self):
        """
        Gets the id of this DBStudy.


        :return: The id of this DBStudy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DBStudy.


        :param id: The id of this DBStudy.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this DBStudy.


        :return: The name of this DBStudy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DBStudy.


        :param name: The name of this DBStudy.
        :type: str
        """
        self._name = name

    @property
    def pmid(self):
        """
        Gets the pmid of this DBStudy.


        :return: The pmid of this DBStudy.
        :rtype: int
        """
        return self._pmid

    @pmid.setter
    def pmid(self, pmid):
        """
        Sets the pmid of this DBStudy.


        :param pmid: The pmid of this DBStudy.
        :type: int
        """
        self._pmid = pmid

    @property
    def short_name(self):
        """
        Gets the short_name of this DBStudy.


        :return: The short_name of this DBStudy.
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """
        Sets the short_name of this DBStudy.


        :param short_name: The short_name of this DBStudy.
        :type: str
        """
        self._short_name = short_name

    @property
    def type_of_cancer(self):
        """
        Gets the type_of_cancer of this DBStudy.


        :return: The type_of_cancer of this DBStudy.
        :rtype: str
        """
        return self._type_of_cancer

    @type_of_cancer.setter
    def type_of_cancer(self, type_of_cancer):
        """
        Sets the type_of_cancer of this DBStudy.


        :param type_of_cancer: The type_of_cancer of this DBStudy.
        :type: str
        """
        self._type_of_cancer = type_of_cancer

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

