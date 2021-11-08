
'''
   Copyright © 2019  Atos Spain SA. All rights reserved.
  
   This file is part of the ReMAP platform.
  
   The ReMAP platform is free software: you can redistribute it 
   and/or modify it under the terms of GNU GPL v3.
   
   THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT ANY WARRANTY OF ANY KIND, 
   EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
   MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT, 
   IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
   CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN ACTION OF CONTRACT, TORT 
   OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
   OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
  
   See README file for the full disclaimer information and LICENSE file 
   for full license information in the project root.  
  '''

import csv
import json
from datetime import datetime
import requests


class Sdk:
    '''ReMAP SDK for RUL Algorithms'''

    DIR_BASE = '/app/'
    DATASET_FILE = 'dataset.csv'
    SLOTS_FILE = 'slots.csv'
    WORKFORCE_FILE = 'workforce.csv'
    NONPROGNOSTASKS_FILE = 'nonPrognosTasks.csv'
    PROGNOSTASKS_FILE = 'prognosTasks.csv'
    RUL_FILE = 'rul.csv'
    HI_FILE = 'hi.csv'
    LOCAL_STORAGE_FILE = 'localStorage'
    METADATA_FILE = 'metadata.json'
    CONFIG_FILE = 'sdk_config.json'
    GLOBAL_VARIABLES_FILE = 'global_variables.json'
    METADATA = 'metadata'

    config = None
    start_date = None
    end_date = None
    tailNumber = None
    metadata = None
    aircraft = None
    fleet = None
    global_variables = None

    def __init__(self):
        '''SDK constructor'''
        with open(self.DIR_BASE+self.CONFIG_FILE) as File:
            self.config = json.load(File)

    def getStartTime(self):
        '''get the start time of metadata'''
        if self.start_date is None:
            with open(self.DIR_BASE+self.METADATA_FILE) as file:
                self.metadata = json.load(file)
            self.start_date = self.metadata['startTime']
        else:
            pass
        return self.start_date

    def getEndTime(self):
        '''get the end time of metadata'''
        if self.end_date is None:
            with open(self.DIR_BASE+self.METADATA_FILE) as file:
                self.metadata = json.load(file)
            self.end_date = self.metadata['endTime']
        else:
            pass
        return self.end_date

    def getTailNumber(self):
        if self.tailNumber is None:
            if self.metadata is None:
                with open(self.DIR_BASE+self.METADATA_FILE) as file:
                    self.metadata = json.load(file)
            self.tailNumber = self.metadata['tailNumber']
        else:
            pass
        return self.tailNumber

    def getAircraft(self):
        ''' get the aircraft '''
        if self.aircraft is None:
            if self.metadata is None:
                with open(self.DIR_BASE+self.METADATA_FILE) as file:
                    self.metadata = json.load(file)
            self.aircraft = self.metadata['aircraft']
        else:
            pass
        return self.aircraft

    def getAircraftByTailNo(self, param):
        aircraft = "TailNo Not Found"
        ''' get the fleet '''
        if self.fleet is None:
            if self.metadata is None:
                with open(self.DIR_BASE+self.METADATA_FILE) as file:
                    self.metadata = json.load(file)
            self.fleet = self.metadata['fleet']

        for x in self.fleet:
            if x.tailNo == param:
                aircraft = x

        return aircraft

    def getFleet(self):
        ''' get the fleet '''
        if self.fleet is None:
            if self.metadata is None:
                with open(self.DIR_BASE+self.METADATA_FILE) as file:
                    self.metadata = json.load(file)
            self.fleet = self.metadata['fleet']
        else:
            pass
        return self.fleet

    def getMetadata(self):
        with open(self.DIR_BASE+self.METADATA_FILE) as file:
            self.metadata = json.load(file)
        return self.metadata['metadata']

    def getComponents(self):
        with open(self.DIR_BASE+self.METADATA_FILE) as file:
            self.metadata = json.load(file)
        return self.metadata['components']

    def getReplacements(self):
        if self.metadata is None:
            with open(self.DIR_BASE+self.METADATA_FILE) as file:
                self.metadata = json.load(file)
        return self.metadata['replacements']

    def getGlobalVariables(self):
        with open(self.DIR_BASE+self.GLOBAL_VARIABLES_FILE) as file:
            self.global_variables = json.load(file)
        return self.global_variables

    def getDataset(self):
        return self.DIR_BASE+self.DATASET_FILE

    def getSlots(self):
        return self.DIR_BASE+self.SLOTS_FILE

    def getNonPrognosTasks(self):
        return self.DIR_BASE+self.NONPROGNOSTASKS_FILE

    def getPrognosTasks(self):
        return self.DIR_BASE+self.PROGNOSTASKS_FILE

    def getRul(self):
        return self.DIR_BASE+self.RUL_FILE

    def getHI(self):
        return self.DIR_BASE+self.HI_FILE

    def getWorkforce(self):
        return self.DIR_BASE+self.WORKFORCE_FILE

    def getLocalStorage(self):
        return self.DIR_BASE+self.LOCAL_STORAGE_FILE

    # return the Serial of the component the parameter passed as param belongs to
    def getSerialByParam(self, param):
        serial = "serial Not Found"
        if self.metadata is None:
            with open(self.DIR_BASE+self.METADATA_FILE) as file:
                self.metadata = json.load(file)
        metadata = self.metadata[self.METADATA]
        for x in metadata:
            if x.__contains__('parameter'):
                parameter = x['parameter']
                if parameter is not None:
                    name = parameter['name']
                    if name == param:
                        component = parameter['component']
                        serial = component['serial']
        return serial

    # return the PartNo of the component the parameter passed as param belongs to
    def getPartNumberByParam(self, param):
        PartNo = "P/N Not Found"
        if self.metadata is None:
            with open(self.DIR_BASE+self.METADATA_FILE) as file:
                self.metadata = json.load(file)
        metadata = self.metadata[self.METADATA]
        for x in metadata:
            if x.__contains__('parameter'):
                parameter = x['parameter']
                if parameter is not None:
                    name = parameter['name']
                    if name == param:
                        component = parameter['component']
                        PartNo = component['partNo']
        return PartNo
    
    # return the PartNo of the component the parameter passed as param belongs to
    def getParamPartNumber(self, param):
        PartNo = "P/N Not Found"
        if self.metadata is None:
            with open(self.DIR_BASE+self.METADATA_FILE) as file:
                self.metadata = json.load(file)
        metadata = self.metadata[self.METADATA]
        for x in metadata:
            if x.__contains__('parameter'):
                parameter = x['parameter']
                if parameter is not None:
                    name = parameter['name']
                    if name == param:
                        component = parameter['component']
                        PartNo = component['partNo']
        return PartNo

    def sendOutput(self, jsonoutput):
        secret = self.__getClientSecret()
        payload = jsonoutput
        payload['serial'] = self.config['serial']
        payload['dataset'] = self.config['dataset']
        payload['model'] = self.config['model']
        payload['status'] = "FINISHED"
        payload['runnerId'] = self.config['runnerId']

        token = self.__getKCToken(secret)
        json_dump = json.dumps(payload)
        headers = {"Content-Type": "application/json",
                   "Authorization": "Bearer "+token}
        r = requests.post(self.config['OUTPUT_URL'],
                          headers=headers, data=json_dump)
        return (r.text)

    def sendHealthIndicator(self, jsonoutput):
        secret = self.__getClientSecret()
        payload = jsonoutput
        payload['serial'] = self.config['serial']
        payload['dataset'] = self.config['dataset']
        payload['model'] = self.config['model']
        payload['runnerId'] = self.config['runnerId']

        token = self.__getKCToken(secret)
        json_dump = json.dumps(payload)
        headers = {"Content-Type": "application/json",
                   "Authorization": "Bearer "+token}
        r = requests.post(self.config['HEALTH_OUTPUT_URL'],
                          headers=headers, data=json_dump)
        return (r.text)

    def sendNonPrognosTasks(self, file):
        secret = self.__getClientSecret()
        token = self.__getKCToken(secret)
        headers = { "Authorization": "Bearer "+token }

        with open(file, 'rb') as f:
            r = requests.post(self.config['NONPROGNOSTASKS_OUTPUT_URL'],
                              headers=headers, files={'nonPrognosTasks.csv': f})
        return (r.text)

    def sendSlots(self, file):
        secret = self.__getClientSecret()
        token = self.__getKCToken(secret)
        headers = { "Authorization": "Bearer "+token }

        with open(file, 'rb') as f:
            r = requests.post(self.config['SLOTS_OUTPUT_URL'],
                              headers=headers, files={'slots.csv': f})
        return (r.text)

    def sendWorkforce(self, file):
        secret = self.__getClientSecret()
        token = self.__getKCToken(secret)
        headers = { "Authorization": "Bearer "+token }

        with open(file, 'rb') as f:
            r = requests.post(self.config['WORKFORCE_OUTPUT_URL'],
                              headers=headers, files={'slots.csv': f})
        return (r.text)

    def sendLocalStorage(self, file):
        secret = self.__getClientSecret()
        token = self.__getKCToken(secret)
        headers = { "Authorization": "Bearer "+token }

        with open(file, 'rb') as f:
            r = requests.post(self.config['LOCAL_STORAGE_URL'],
                              headers=headers, files={self.config['model']: f})
        return (r.text)

    def __getKCToken(self, secret):

        url = self.config['KC_TOKEN_URL']
        payload = {
            "client_id": self.config['CLIENT_ID'],
            "grant_type": "client_credentials",
            "client_secret": secret}
        r = requests.post(url, data=payload)
        res = json.loads(r.text)
        token = res['access_token']

        payload = {
            "client_id": self.config['CLIENT_ID'],
            "client_secret": secret,
            "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
            "audience": self.config['TOKEN_AUDIENCE'],
            "subject_token": token
        }
        r = requests.post(url, data=payload)
        res = json.loads(r.text)
        token = res['access_token']
        return token

    def __getClientSecret(self):

        secret = "Secret Not Found"
        with open(self.DIR_BASE+'secret') as file:
            secret = file.read()
        return secret
