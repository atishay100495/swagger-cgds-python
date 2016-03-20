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


class DBSample(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DBSample - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'internal_id': 'str',
            'patient_id': 'str',
            'sample_type': 'str',
            'study_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'internal_id': 'internal_id',
            'patient_id': 'patient_id',
            'sample_type': 'sample_type',
            'study_id': 'study_id'
        }

        self._id = None
        self._internal_id = None
        self._patient_id = None
        self._sample_type = None
        self._study_id = None

    @property
    def id(self):
        """
        Gets the id of this DBSample.


        :return: The id of this DBSample.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DBSample.


        :param id: The id of this DBSample.
        :type: str
        """
        self._id = id

    @property
    def internal_id(self):
        """
        Gets the internal_id of this DBSample.


        :return: The internal_id of this DBSample.
        :rtype: str
        """
        return self._internal_id

    @internal_id.setter
    def internal_id(self, internal_id):
        """
        Sets the internal_id of this DBSample.


        :param internal_id: The internal_id of this DBSample.
        :type: str
        """
        self._internal_id = internal_id

    @property
    def patient_id(self):
        """
        Gets the patient_id of this DBSample.


        :return: The patient_id of this DBSample.
        :rtype: str
        """
        return self._patient_id

    @patient_id.setter
    def patient_id(self, patient_id):
        """
        Sets the patient_id of this DBSample.


        :param patient_id: The patient_id of this DBSample.
        :type: str
        """
        self._patient_id = patient_id

    @property
    def sample_type(self):
        """
        Gets the sample_type of this DBSample.


        :return: The sample_type of this DBSample.
        :rtype: str
        """
        return self._sample_type

    @sample_type.setter
    def sample_type(self, sample_type):
        """
        Sets the sample_type of this DBSample.


        :param sample_type: The sample_type of this DBSample.
        :type: str
        """
        self._sample_type = sample_type

    @property
    def study_id(self):
        """
        Gets the study_id of this DBSample.


        :return: The study_id of this DBSample.
        :rtype: str
        """
        return self._study_id

    @study_id.setter
    def study_id(self, study_id):
        """
        Sets the study_id of this DBSample.


        :param study_id: The study_id of this DBSample.
        :type: str
        """
        self._study_id = study_id

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
