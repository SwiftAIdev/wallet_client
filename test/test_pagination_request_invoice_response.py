# coding: utf-8

"""
    Wallet Service API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wallet_client.models.pagination_request_invoice_response import PaginationRequestInvoiceResponse

class TestPaginationRequestInvoiceResponse(unittest.TestCase):
    """PaginationRequestInvoiceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginationRequestInvoiceResponse:
        """Test PaginationRequestInvoiceResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginationRequestInvoiceResponse`
        """
        model = PaginationRequestInvoiceResponse()
        if include_optional:
            return PaginationRequestInvoiceResponse(
                page = 56,
                size = 56,
                total = 56,
                data = [
                    wallet_client.models.invoice_response.InvoiceResponse(
                        id = 56, 
                        inn = '', 
                        kpp = '', 
                        email = '0', 
                        phone_number = '+79998887766', 
                        name = '', )
                    ]
            )
        else:
            return PaginationRequestInvoiceResponse(
                page = 56,
                size = 56,
                total = 56,
                data = [
                    wallet_client.models.invoice_response.InvoiceResponse(
                        id = 56, 
                        inn = '', 
                        kpp = '', 
                        email = '0', 
                        phone_number = '+79998887766', 
                        name = '', )
                    ],
        )
        """

    def testPaginationRequestInvoiceResponse(self):
        """Test PaginationRequestInvoiceResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
