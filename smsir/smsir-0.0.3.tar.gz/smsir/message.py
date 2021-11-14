import requests
import json
class sms:
    
    def send_by_mobile_number(self,Messages='',MobileNumbers='',LineNumber='',SendDateTime='',Token=''):
        secure_token = self.secure_token
        headers = {
        "Content-Type": "application/json",
        'x-sms-ir-secure-token': secure_token
        }
        body = {
        "Messages": [Messages],
        "MobileNumbers": [MobileNumbers],
        "LineNumber": LineNumber,
        "SendDateTime": SendDateTime ,
        "CanContinueInCaseOfError": "false",
        }
        response = requests.post('http://RestfulSms.com/api/MessageSend', data=json.dumps(body),
                                headers=headers)
        print(response.json())
        return 'send'    