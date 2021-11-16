
import requests
import json


class CustomerClub:
    def __init__(self) -> None:
        pass

    # POST CustomerClubContact (AddContact)
    def add_contact(self, Prefix='', FirstName='', LastName='', Mobile='', BirthDay='', CategoryId='', Token=''):
        url = "http://restfulsms.com/api/CustomerClubContact"
        headers = {
            "Content-Type": "application/json",
            'x-sms-ir-secure-token': Token
        }
        body = {
            "Prefix": Prefix,
            "FirstName": FirstName,
            "LastName": LastName,
            "Mobile": Mobile,
            "BirthDay": BirthDay,
            "CategoryId": CategoryId
        }
        response = requests.post(url, data=json.dumps(body),
                                 headers=headers)

        return response

        # PUT CustomerClubContact (UpdateContact)

    def update_contact(self, Prefix='', FirstName='', LastName='', Mobile='', BirthDay='', CategoryId='', Token=''):
        url = 'http://restfulsms.com/api/CustomerClubContact'
        headers = {
            "Content-Type": "application/json",
            'x-sms-ir-secure-token': Token
        }
        body = {
            "Prefix": Prefix,
            "FirstName": FirstName,
            "LastName": LastName,
            "Mobile": Mobile,
            "BirthDay": BirthDay,
            "CategoryId": CategoryId
        }
        response = requests.put(url, data=json.dumps(body),
                                headers=headers)

        return response

        # GET CustomerClubContact (GetCategories)

    def get_categories(self, Token=''):
        url = 'http://restfulsms.com/api/CustomerClubContact/GetCategories'
        headers = {
            "Content-Type": "application/json",
            'x-sms-ir-secure-token': Token
        }
        response = requests.get(url, headers=headers)

        return response

        # GET CustomerClubContact (GetContactsByCategory&ById)

    def get_contacts_by_categoryId(self, categoryId='', pageNumber='', Token=''):
        url = f'http://restfulsms.com/api/CustomerClubContact/GetContactsByCategoryById?categoryId={categoryId}&pageNumber={pageNumber}'
        headers = {
            "Content-Type": "application/json",
            'x-sms-ir-secure-token': Token
        }
        response = requests.get(url, headers=headers)

        return response
        # GET CustomerClubContact (GetAllContactsByPageID)

    def get_allcontacts_By_pageid(self, pageNumber='', Token=''):
        url = f'http://restfulsms.com/api/CustomerClubContact/GetContacts?pageNumber={pageNumber}'
        headers = {
            "Content-Type": "application/json",
            'x-sms-ir-secure-token': Token
        }
        response = requests.get(url, headers=headers)

        return response
        # POST CustomerClub (Send)

    def send_customer_club(self, Messages='', MobileNumbers='',
                           SendDateTime='', CanContinueInCaseOfError="true", Token=''):
        url = 'http://RestfulSms.com/api/CustomerClub/Send'
        headers = {
            "Content-Type": "application/json",
            'x-sms-ir-secure-token': Token
        }
        body = {
            "Messages": Messages,
            "MobileNumbers": MobileNumbers,
            "SendDateTime": SendDateTime,
            "CanContinueInCaseOfError": CanContinueInCaseOfError
        }
        response = requests.post(url, data=json.dumps(body),
                                 headers=headers)

        return response

        # POST CustomerClub (AddContact&Send)

    def add_Contact_send(self, Prefix='', FirstName='', LastName='', Mobile='', BirthDay='', CategoryId='',
                         MessageText='', Token=''):
        url = 'http://RestfulSms.com/api/CustomerClub/AddContactAndSend'
        headers = {
            "Content-Type": "application/json",
            'x-sms-ir-secure-token': Token
        }
        body = {
            "Prefix": Prefix,
            "FirstName": FirstName,
            "LastName": LastName,
            "Mobile": Mobile,
            "BirthDay": BirthDay,
            "CategoryId": CategoryId,
            "MessageText": MessageText
        }
        response = requests.post(url, data=json.dumps(body),
                                 headers=headers)

        return response
        # POST CustomerClub (SendToCategories)

    def Send_To_categories(self, Messages='', contactsCustomerClubCategoryIds='', SendDateTime='',
                           CanContinueInCaseOfError='false', Token=''):
        url = 'http://RestfulSms.com/api/CustomerClub/SendToCategories'
        headers = {
            "Content-Type": "application/json",
            'x-sms-ir-secure-token': Token
        }
        body = {
            "Messages": Messages,
            "contactsCustomerClubCategoryIds": contactsCustomerClubCategoryIds,
            "SendDateTime": SendDateTime,
            "CanContinueInCaseOfError": CanContinueInCaseOfError
        }
        response = requests.post(url, data=json.dumps(body),
                                 headers=headers)

        return response

        # GET CustomerClub (GetSendMessagesByPagination)

    def get_send_messages_by_pagination(self, pageIndex=1, rowCount=10, Token=''):
        url = f'http://restfulsms.com/api/CustomerClub/GetSendMessagesByPagination?pageIndex={pageIndex}&rowCount={rowCount}'
        headers = {
            "Content-Type": "application/json",
            'x-sms-ir-secure-token': Token
        }
        response = requests.get(url, headers=headers)

        return response

        # GET CustomerClub (GetSendMessagesByPaginationAndLastId)

    def get_send_messages_by_pagination_And_lastId(self, lastId='', Token=''):
        url = f'http://restfulsms.com/api/CustomerClub/GetSendMessagesByPaginationAndLastId?lastId={lastId}'
        headers = {
            "Content-Type": "application/json",
            'x-sms-ir-secure-token': Token
        }
        response = requests.get(url, headers=headers)

        return response

        # POST CustomerClub (DeleteContactCustomerClub)

    def delete_contact_customerClub(self, Mobile='', CanContinueInCaseOfError='false', Token=''):
        url = 'http://restfulsms.com/api/CustomerClub/DeleteContactCustomerClub'
        headers = {
            "Content-Type": "application/json",
            'x-sms-ir-secure-token': Token
        }
        body = {
            "Mobile": Mobile,
            "CanContinueInCaseOfError": CanContinueInCaseOfError
        }
        response = requests.post(url, data=json.dumps(body),
                                 headers=headers)

        return response
