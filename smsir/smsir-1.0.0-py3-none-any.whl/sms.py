import requests
import json
class sms:
    def __init__(self) -> None:
        pass
        # POST MessageSend
    def send_by_mobile_number(self,Messages='',MobileNumbers='',LineNumber='',SendDateTime='',Token=''):
        url ="http://RestfulSms.com/api/MessageSend"
        headers = {
        "Content-Type": "application/json",
        'x-sms-ir-secure-token': Token
        }
        body = {
        "Messages": [Messages],
        "MobileNumbers": [MobileNumbers],
        "LineNumber": LineNumber,
        "SendDateTime": SendDateTime ,
        "CanContinueInCaseOfError": "false",
        }
        response = requests.post(url, data=json.dumps(body),
                                headers=headers)
        
        return response

        # GET SMSLine
    def get_sms_line(self,Token=''):
        url ="http://RestfulSms.com/api/SMSLine"
        headers = {
        "Content-Type": "application/json",
        'x-sms-ir-secure-token': Token
        }
        response = requests.get(url,headers=headers)
        return response

        # GET MessageSend (ReportByDate)
    def get_report_by_date(self,StartDate_SHAMSI='',EndDate_SHAMSI='',RowsPerPage=10,RequestedPageNumber=1,Token=''):
        url = f'http://RestfulSms.com/api/MessageSend?Shamsi_FromDate={StartDate_SHAMSI}&Shamsi_ToDate={EndDate_SHAMSI}&RowsPerPage={RowsPerPage}&RequestedPageNumber={RequestedPageNumber}'
        headers = {
        "Content-Type": "application/json",
        'x-sms-ir-secure-token': Token
        }
        response = requests.get(url,headers=headers)
        return response

        # GET MessageSend (ReportById)
    def get_report_by_id(self,sms_id,Token=''):
        url =f'http://RestfulSms.com/api/MessageSend?id={sms_id}'
        headers = {
        "Content-Type": "application/json",
        'x-sms-ir-secure-token': Token
        }
        response = requests.get(url,headers=headers)
        return response

        # GET MessageSend (ReportByBachkey)
    def get_report_by_bachkey(self,PageID='',BatchKey='',Token=''):
        url =f'http://restfulsms.com/api/MessageSend?pageId={PageID}&batchKey={BatchKey}'
        headers = {
        "Content-Type": "application/json",
        'x-sms-ir-secure-token': Token
        }
        response = requests.get(url,headers=headers)
        return response

        # GET ReceiveMessage (ByLastID)
    def get_receive_message_by_last_id(self,ByLastID='',Token=''):
        url =f'http://RestfulSms.com/api/ReceiveMessage?id={ByLastID}'
        headers = {
        "Content-Type": "application/json",
        'x-sms-ir-secure-token': Token
        }
        response = requests.get(url,headers=headers)
        return response

        # GET ReceiveMessage (ByDate)
    def get_receive_message_by_date(self,StartDate_SHAMSI='',EndDate_SHAMSI='',RowsPerPage='10',RequestedPageNumber='1',Token=''):
        url =f'http://RestfulSms.com/api/ReceiveMessage?Shamsi_FromDate={StartDate_SHAMSI}&Shamsi_ToDate={EndDate_SHAMSI}&RowsPerPage={RowsPerPage}&RequestedPageNumber={RequestedPageNumber}'
        headers = {
        "Content-Type": "application/json",
        'x-sms-ir-secure-token': Token
        }
        response = requests.get(url,headers=headers)
        return response

        # POST VerificationCode
    def VerificationCode(self,Code='',MobileNumber='',Token=''):
        url ='http://RestfulSms.com/api/VerificationCode'
        headers = {
        "Content-Type": "application/json",
        'x-sms-ir-secure-token': Token
        }
        body ={
            "Code": Code,
            "MobileNumber": MobileNumber
        }
        response = requests.post(url, data=json.dumps(body),
                                headers=headers)
        
        return response

        # POST UltraFastSend 
    def UltraFastSend(self,ParameterArray=[],Mobile='',TemplateId='',Token=''):
        url= 'http://RestfulSms.com/api/UltraFastSend'
        headers = {
        "Content-Type": "application/json",
        'x-sms-ir-secure-token': Token
        }
        body={
            "ParameterArray":ParameterArray,
            "Mobile": Mobile,
            "TemplateId": TemplateId
        } 
        response = requests.post(url, data=json.dumps(body),
                                headers=headers)
        
        return response

        #POST MessageReport
    def MessageReport(self,ReportType='1',SentReturnId='null',FromDate='',ToDate='',Token=''):
        url='https://RestfulSms.com/api/MessageReport'
        headers = {
        "Content-Type": "application/json",
        'x-sms-ir-secure-token': Token
        }
        body={
            "ReportType": ReportType,
            "SentReturnId": SentReturnId,
            "FromDate": FromDate,
            "ToDate": ToDate
        }
        response = requests.post(url, data=json.dumps(body),
                                headers=headers)
        
        return response




