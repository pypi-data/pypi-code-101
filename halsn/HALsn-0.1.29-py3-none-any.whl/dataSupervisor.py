#!/usr/bin/env python3

'''
MIT License

Copyright (c) 2021 Mikhail Hyde & Cole Crescas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import os
import time
from botocore.exceptions import NoCredentialsError
import pandas as pd
import numpy as np
import boto3
from HALsn.sysLogger import sysLogger

class s3:
    def __init__(self):
        self.ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
        self.SECRET_KEY = os.environ['AWS_SECRET_KEY']
        self.bucket = os.environ['BUCKET']

        self.s3 = boto3.client('s3', aws_access_key_id=self.ACCESS_KEY,
                            aws_secret_access_key=self.SECRET_KEY)

    def upload_to_s3(self, filename):
        '''
        Uploads a single file to the AWS s3 bucket.
        '''
        try:
            self.s3.upload_file(Filename=filename,
                                Bucket=self.bucket,
                                Key=self.filename)
            return True
        except FileNotFoundError:
            self.logger.ERROR("The file was not found")
            return False
        except NoCredentialsError:
            self.logger.ERROR("Credentials not available")
            return False

class parser:

    def __init__(self, map, headers=False):
        
        self.df = pd.DataFrame()
        self.product_map = map

        self.lst         = []

        if headers != False:
            self.headers = headers

        self.convert_fnc = {'KC':  self._kc_conv,
                            'HEX': self._convertHex,
                            'PWM': self._pwm,
                            'INT': self._cast_int}

    def _get_key(self, entry):
    
        for value in self.product_map.values():
            
            if type(entry) == str:
            
                match = value[0][1:value[2]]
                key   = entry[1:value[2]]
                if key == match:
                    return key

    def _convertBDP(self, data):
        '''
        Univsersal function for converting BDP
        responses into readable data. References
        the query hash map of the device it is
        interpretting.

        ::returns:: List -> converted BDP value(s)
        '''

        key = self._get_key(data)

        if key is None:
            return data

        for inst in self.product_map.values():

            if key == inst[0][1:inst[2]]:
                if inst[-1] == 0:
                    return data[1:-1]
                fnc = self.convert_fnc[inst[-1]]
                return fnc(data[inst[2]:-1])

    def parse(self):
        """
        takes in query command list & parses

        ::returns:: parsed dataframe
        """

        for row in self.lst:

            clean_lst = []

            for data in row:
                clean_lst.append(self._convertBDP(data))

            self._flatten(clean_lst)
            self.df = self.df.append(
                    pd.DataFrame(((np.asarray(clean_lst)).reshape(1, -1)), columns=self.headers))

    def interpreted_parse(self):
        '''
        Iterates through the lst member and builds a
        dataframe using the keys as the headers. Does
        not reference list of headers
        '''
        for row in self.lst:
    
            headers   = []
            clean_lst = []
            ext_idx   = 1

            for data in row:

                key = self._get_key(data)
                
                if key == None:
                    key = 'ES' + str(ext_idx)
                    ext_idx += 1
                
                if key == 'KC':
                    key = ['KC1', 'KC2', 'KC3', 'KC4', 'KC5', 'KC6', 'KC7', 'KC8']
                
                clean_lst.append(self._convertBDP(data))
                headers.append(key)

            clean_lst = self._flatten(clean_lst)
            headers   = self._flatten(headers)

            self.df   = self.df.append(
                pd.DataFrame(((np.asarray(clean_lst)).reshape(1, -1)), columns=headers))

    def _flatten(self, lst):
        '''
        Takes a list as an input and recursively
        processes through the list to remove any
        embedded iterables. 

        ::returns:: List ONLY ints, floats, and strings
        '''

        flat_list = []

        for idx in lst:
            if type(idx) == list or type(idx) == tuple:
                flat_list += self._flatten(idx)
            else:
                flat_list.append(idx)

        return flat_list

    def _kc_conv(self, data):
        basket = int(data[0])
        size   = self._convertHex(data[1])
        style  = int(data[2])
        ounces = self._convertHex(data[3:5])
        block  = self._convertHex(data[5:7])
        temp   = self._convertHex(data[7:9])
        volume = self._convertHex(data[9:13])
        time   = self._convertHex(data[13:15])

        return [basket, size, style, ounces, block, temp, volume, time]

    @staticmethod
    def _pwm(data):
        return (int(data) / 64) * 100

    @staticmethod
    def _convertHex(value):
        return int(value, 16)

    @staticmethod
    def _cast_int(data):
        return int(data)

class dataSupervisor:
    def __init__(self, map, headers=False, s3_enable=False):
        
        self.logger = sysLogger(file=False)
        
        self.s3_enable = s3_enable
        if self.s3_enable:
            self.s3 = s3()
       
        self.parser = parser(map, headers)

        self.filename    = 'default.csv'
        self.localfile   = '~/' + self.filename

    def add_filename(self, filename):
        '''
        Generates a TimeStamp (string) to be appended
        to CSV file for export

        ::returns:: String
        '''
        self.filename = filename
        if filename[-4:] != '.csv':
            self.filename += '.csv'

        self.localfile = '~/' + self.filename

    def collect_row(self, *args):
        '''
        Takes an arbitrary amount of arguments
        of any type. Breaks down all inputs into
        a single list and appends the list to the
        dataframe. 

        Final list length must match the length
        of headers.
        '''
        if not self.parser.headers:
            row = []
            for arg in args:
                arg = self._flatten(arg)
                row += arg

            self.parser.lst.append(row)

    def generate(self, specific=False):
        if specific:
            self.parser.parse()
        else:
            self.parser.interpreted_parse()

    def export_csv(self):
        '''
        Exports the parsed and formatted Dataframe as a CSV
        file to the predetermined directory.
        '''
        self.parser.df.to_csv(self.localfile, index=False)
        self.logger.INFO(f'Created Report {self.filename}')

    def export(self):
        """
        creates report of visualizations & exports to html
        calls in markdown extension of pandas
        :return: report in html form
        """
        self.export_csv()
        if self.s3_enable:
            self.s3.upload_to_s3()

    def init_frames(self):
        '''
        Initializes class members for new cycle.
        '''
        self.parser.df = pd.DataFrame()
        self.parser.lst = []