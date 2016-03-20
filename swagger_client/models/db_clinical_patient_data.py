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


class DBClinicalPatientData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DBClinicalPatientData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'attr_id': 'str',
            'attr_val': 'str',
            'patient_id': 'str',
            'study_id': 'str'
        }

        self.attribute_map = {
            'attr_id': 'attr_id',
            'attr_val': 'attr_val',
            'patient_id': 'patient_id',
            'study_id': 'study_id'
        }

        self._attr_id = None
        self._attr_val = None
        self._patient_id = None
        self._study_id = None

    @property
    def attr_id(self):
        """
        Gets the attr_id of this DBClinicalPatientData.


        :return: The attr_id of this DBClinicalPatientData.
        :rtype: str
        """
        return self._attr_id

    @attr_id.setter
    def attr_id(self, attr_id):
        """
        Sets the attr_id of this DBClinicalPatientData.


        :param attr_id: The attr_id of this DBClinicalPatientData.
        :type: str
        """
        self._attr_id = attr_id

    @property
    def attr_val(self):
        """
        Gets the attr_val of this DBClinicalPatientData.


        :return: The attr_val of this DBClinicalPatientData.
        :rtype: str
        """
        return self._attr_val

    @attr_val.setter
    def attr_val(self, attr_val):
        """
        Sets the attr_val of this DBClinicalPatientData.


        :param attr_val: The attr_val of this DBClinicalPatientData.
        :type: str
        """
        self._attr_val = attr_val

    @property
    def patient_id(self):
        """
        Gets the patient_id of this DBClinicalPatientData.


        :return: The patient_id of this DBClinicalPatientData.
        :rtype: str
        """
        return self._patient_id

    @patient_id.setter
    def patient_id(self, patient_id):
        """
        Sets the patient_id of this DBClinicalPatientData.


        :param patient_id: The patient_id of this DBClinicalPatientData.
        :type: str
        """
        self._patient_id = patient_id

    @property
    def study_id(self):
        """
        Gets the study_id of this DBClinicalPatientData.


        :return: The study_id of this DBClinicalPatientData.
        :rtype: str
        """
        return self._study_id

    @study_id.setter
    def study_id(self, study_id):
        """
        Sets the study_id of this DBClinicalPatientData.


        :param study_id: The study_id of this DBClinicalPatientData.
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

