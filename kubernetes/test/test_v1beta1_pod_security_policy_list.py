# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1beta1_pod_security_policy_list import V1beta1PodSecurityPolicyList


class TestV1beta1PodSecurityPolicyList(unittest.TestCase):
    """ V1beta1PodSecurityPolicyList unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1PodSecurityPolicyList(self):
        """
        Test V1beta1PodSecurityPolicyList
        """
        model = kubernetes.client.models.v1beta1_pod_security_policy_list.V1beta1PodSecurityPolicyList()


if __name__ == '__main__':
    unittest.main()
