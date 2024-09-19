# coding: utf-8

"""
    Wallet Service API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wallet_client.models.invoice_create_response import InvoiceCreateResponse

class TestInvoiceCreateResponse(unittest.TestCase):
    """InvoiceCreateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceCreateResponse:
        """Test InvoiceCreateResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceCreateResponse`
        """
        model = InvoiceCreateResponse()
        if include_optional:
            return InvoiceCreateResponse(
                inn = '',
                email = 'user@mail.ru',
                phone_number = '+79999999999'
            )
        else:
            return InvoiceCreateResponse(
                inn = '',
        )
        """

    def testInvoiceCreateResponse(self):
        """Test InvoiceCreateResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
