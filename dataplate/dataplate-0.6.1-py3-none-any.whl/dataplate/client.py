import os, sys
import requests
import tempfile
import logging
import boto3
import time
import json
from shutil import copyfileobj
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import awswrangler as wr
import pandas as pd
import inspect
from inspect import signature
from urllib.parse import urlparse

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


class NoTraceBackWithLineNumber(Exception):
    def __init__(self, msg):
        try:
            ln = sys.exc_info()[-1].tb_lineno
        except AttributeError:
            ln = inspect.currentframe().f_back.f_lineno
        self.args = "{0.__name__} (line {1}): {2}".format(type(self), ln, msg),
        sys.exit(self)

class Error(NoTraceBackWithLineNumber):
    pass

class DataPlate:
    """
    Initializes Data Access API client.

    Parameters
    -----------
    access_key : str (optional)
        Your own private key that can be obtained through DataPlate Data Access Portal. Default value is taken from the
        `DA_KEY` environment variable.

    dataplate_uri : str (optional)
        DataPlate Portal URI. If not specified, the value is taken from the `DA_URI` environment variable.
    """
    def __init__(self, access_key=None, dataplate_uri=None):
        if dataplate_uri is None:
            if not 'DA_URI' in os.environ:
                raise Error(ValueError(
                    'Can\'t find DA_URI environment variable, dataplate_uri parameter is not provided either!'
                ))
            dataplate_uri = os.environ['DA_URI']

        if access_key is None:
            if not 'DA_KEY' in os.environ:
                raise Error(ValueError(
                    'Can\'t find DA_KEY environment variable, access_key parameter is not provided either!'
                ))
            access_key = os.environ['DA_KEY']

        self.access_key = access_key
        self.session = requests.sessions.Session()
        retry = Retry(total=5,
                      read=5,
                      connect=5,
                      backoff_factor=0.3,
                      status_forcelist=(500, 502, 504))
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        self.base_url = '/'.join(dataplate_uri.split('/')[0:3])

    def _set_proxy_if_needed(self, proxy):
        os.environ.pop('HTTP_PROXY', None)
        try:
            self.session.head('{}/version'.format(self.base_url))
        except requests.exceptions.ConnectionError:
            self.session.proxies = {'http': proxy}
            self.session.head('{}/version'.format(self.base_url))

    def _get_list_of_files(self, s3_client, bucket, prefix, suffix='json.gz'):
        next_token = ''
        base_kwargs = {
            'Bucket': bucket,
            'Prefix': prefix,
        }
        keys = []
        while next_token is not None:
            kwargs = base_kwargs.copy()
            if next_token != '':
                kwargs.update({'ContinuationToken': next_token})
            results = s3_client.list_objects_v2(**kwargs)
            contents = results.get('Contents')
            for i in contents:
                k = i.get('Key')
                if k[-1] != '/' and k.endswith(suffix):
                    keys.append(k)
            next_token = results.get('NextContinuationToken')
        logging.info('Got the following files: {}'.format(keys))

        return keys

    def _read_file(self, s3_client, bucket, key):
        kwargs = {'Bucket': bucket, 'Key': key}
        return s3_client.get_object(**kwargs)['Body']

    def _download_files_as_one(self, s3_client, bucket, keys, output_file):
        with open(output_file, 'wb') as out:
            for key in keys:
                fh = self._read_file(s3_client, bucket, key)
                while True:
                    chunk = fh.read(8192)
                    out.write(chunk)
                    if len(chunk) <= 0:
                        break

    def _files_to_df(self, bucket, prefix, **kwargs):
        import pandas as pd
        with tempfile.NamedTemporaryFile(suffix='.gz') as t:
            output_file = t.name
            s3 = boto3.client('s3')
            files = self._get_list_of_files(s3, bucket, prefix)
            self._download_files_as_one(s3, bucket, files, output_file)
            with open(output_file, 'rb') as fh:
                return pd.read_json(fh, compression='gzip', lines=True, **kwargs)

    def query(self,
              query,
              output_file,
              refresh=False,
              async_m=None,
              request_timeout=None,
              es_index_type=None,
              bucket_suffixes=None,
              bucket_filter=None):
        """
        Executes remote SQL query, and saves results to the specified file.

        Parameters
        ----------
        query : str
            SQL query supported by Apache Spark
        output_file : str
            Full path to the file where results will be saved (results are represented by JSON records separated by the newline)
        refresh : boolean
            Whether to use force running query even cached results already exist (default: False)
        async_m : int
            How many minutes should the client poll the server.
        request_timeout : int/tuple
            requests timeout parameter for a single request.
            https://requests.readthedocs.io/en/master/user/advanced/#timeouts
        es_index_type: str
            elasticSearch option - add change dataset index/type for the allowed cluster [e.g.: index1/type1,index2/type2] ,to search for all types in index ignore the type name (default: None)
        bucket_suffixes: str
            bucket option - bucket path suffix added to your dataset path name, [e.g.: MyPathSuffix1,MyPathSuffix2] (default: None)
        bucket_filter: str
            bucket option - include files in the bucket with file names matching the pattern (default: None)
        """
        headers = {'X-Access-Key': self.access_key}
        params = {}
        if refresh:
            params['refresh'] = '1'
        if async_m:
            timeout = time.time() + async_m * 60
            params['async'] = '1'
        if es_index_type:
            params['es_index_type'] = es_index_type
        if bucket_suffixes:
            params['bucket_suffixes'] = bucket_suffixes
        if bucket_filter:
            params['bucket_filter'] = bucket_filter

        retries = 1
        while True:
            if async_m and timeout < time.time():
                raise Error('Timeout waiting for query.')
            try:
                logging.info('Sending query...')
                r = self.session.post(\
                        '{}/api/query'.format(self.base_url), params=params, data=query,
                        headers=headers, stream=True, allow_redirects=False, timeout=request_timeout)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('Query is processing, waiting a bit...')
                        time.sleep(5)
                        continue
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                        format(r.status_code, r.text))

                logging.info('Got query result, writing to file.')
                with open(output_file, 'wb') as fh:
                    copyfileobj(r.raw, fh)
                logging.info('Done writing to file.')
                break
            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                retries -= 1
                if retries <= 0:
                    raise Error(e)
                logging.info('Retrying request.')
                continue

    def query_to_df(self,
                    query,
                    refresh=False,
                    async_m=None,
                    request_timeout=None,
                    es_index_type=None,
                    bucket_suffixes=None,
                    bucket_filter=None,
                    **kwargs):
        """
        Executes remote SQL query, and returns Pandas dataframe.
        Use with care as all the content is materialized.

        Parameters
        ----------
        query : str
            SQL query supported by Apache Spark
        refresh : boolean
            Whether to use force running query even cached results already exist (default: False)
        async_m : int
            How many minutes should the client poll the server.
        request_timeout : int/tuple
            requests timeout parameter for a single request.
            https://requests.readthedocs.io/en/master/user/advanced/#timeouts
        es_index_type: str
            elasticSearch option - add change dataset index/type for the allowed cluster [e.g.: index1/type1,index2/type2] ,to search for all types in index ignore the type name (default: None)
        bucket_suffixes: str
            bucket option - bucket path suffix added to your dataset path name, [e.g.: MyPathSuffix1,MyPathSuffix2] (default: None)
        bucket_filter: str
            bucket option - include files in the bucket with file names matching the pattern (default: None)
        **kwargs : params
            Arbitrary parameters to pass to `pandas.read_json()` method

        Returns
        -------
        Pandas dataframe.
        """
        import pandas as pd
        with tempfile.NamedTemporaryFile(suffix='.gz') as t:
            output_file = t.name
            self.query(query, output_file, refresh, async_m, request_timeout, es_index_type, bucket_suffixes, bucket_filter)
            with open(output_file, 'rb') as fh:
                return pd.read_json(fh, compression='gzip', lines=True, **kwargs)


    def execute_pyspark_toFile(self,
                         code,
                         output_file,
                         refresh=True,
                         retries = 1,
                         async_m=None,
                         request_timeout=None,
                         **kwargs):
        """
        Executes remote pyspark code, and saves results to the specified file - use only if the code specify writes to a target file.

        Parameters
        ----------
        code : str
            Code supported by Apache Spark (pyspark code)
        output_file : str
            Full path to the file where results will be saved (results are represented by JSON records separated by the newline)
        refresh : boolean
            Whether to use force running query even cached results already exist (default: True)
        async_m : int
            How many minutes should the client poll the server.
        request_timeout : int/tuple
            requests timeout parameter for a single request.
            https://requests.readthedocs.io/en/master/user/advanced/#timeouts
        """
        headers = {'X-Access-Key': self.access_key}
        params = {}
        if refresh:
            params['refresh'] = '1'
        if async_m:
            timeout = time.time() + async_m * 60
            params['async'] = '1'

        while True:
            if async_m and timeout < time.time():
                raise Error('Timeout waiting for code.')
            try:
                logging.info('Sending spark code...')
                r = self.session.post( \
                    '{}/api/pyspark_code'.format(self.base_url), params=params, data=code,
                    headers=headers, stream=True, allow_redirects=False, timeout=request_timeout)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('Pyspark code is processing, waiting a bit...')
                        time.sleep(5)
                        continue
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Got pyspark code result, writing to file.')
                with open(output_file, 'wb') as fh:
                    copyfileobj(r.raw, fh)
                logging.info('Done writing to file.')
                break
            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                retries -= 1
                if retries <= 0:
                    raise Error(e)
                logging.info('Retrying request.')
                continue

    def execute_pyspark_toJson(self,
                         code,
                         retries = 1,
                         async_m=None,
                         request_timeout=None,
                         **kwargs):

        """
        Executes remote pyspark code, and output the result as Json.

        Parameters
        ----------
        code : str
            Code supported by Apache Spark (pyspark code)
        async_m : int
            How many minutes should the client poll the server.
        request_timeout : int/tuple
            requests timeout parameter for a single request.
            https://requests.readthedocs.io/en/master/user/advanced/#timeouts
        """

        headers = {'X-Access-Key': self.access_key}
        params = {}
        refresh = True
        if refresh:
            params['refresh'] = '1'
        if async_m:
            timeout = time.time() + async_m * 60
            params['async'] = '1'

        while True:
            if async_m and timeout < time.time():
                raise Error('Timeout waiting for code.')
            try:
                logging.info('Sending pyspark code...')
                r = self.session.post( \
                    '{}/api/pyspark_code_toJson'.format(self.base_url), params=params, data=code,
                    headers=headers, stream=True, allow_redirects=False, timeout=request_timeout)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('Pyspark code is processing, waiting a bit...')
                        time.sleep(5)
                        continue
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Got pyspark code result, dump json response')
                # logging.info(str(r.text))
                if r.text:
                    rJson = json.loads(r.text)
                    return json.dumps(rJson.get('text/plain'))
                else:
                    logging.exception('Could not find proper output, please check your code')
                # return r.text
                # logging.info('Done writing to file.')
                break
            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                retries -= 1
                if retries <= 0:
                    raise Error(e)
                logging.info('Retrying request.')
                continue

    def write_to_s3_csv(self, *args, **kwargs):
        try:
            # json_object = json.dumps(kwargs)
            # if kwargs:
            #     print(f'Kwargs: {kwargs}')
            # if args:
            #     print(f'Kwargs: {args}')
            sig = signature(wr.s3.to_csv)
            sba = sig.bind(*args, **kwargs)

            if 'df' in kwargs:
                # df = pd.read_json(args['df'])
                kwargs['df'] = kwargs['df'].to_json()
                json_kwargs_object = json.dumps(kwargs)
            else:
                return wr.s3.to_csv(*sba.args, **sba.kwargs)


            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}
            params = json.dumps(args)#{}

            try:
                logging.info('Uploading data...')
                r = self.session.post( \
                    '{}/api/aws/toS3_csv'.format(self.base_url), params=params, data=json_kwargs_object,
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('writing data to AWS...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing write response')
                # logging.info(str(r.text))
                if r.text:
                    rJson = json.loads(r.text)
                    logging.info('Done writing.')
                    response_text = rJson.get('text/plain')
                    if (response_text):
                        return json.dumps(rJson.get('text/plain'))
                else:
                    logging.exception('Could not find proper output, please check your parameters')
                # return r.text
            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('aws_to_s3_csv , ' + str(e))
            raise Error(e)

    write_to_s3_csv.__doc__ = wr.s3.to_csv.__doc__.replace('import awswrangler as wr','from dataplate.client import DataPlate')
    write_to_s3_csv.__doc__ = write_to_s3_csv.__doc__.replace('wr.s3.to_csv','dataplate.write_to_s3_csv')

    def write_to_s3_json(self, *args, **kwargs):
        try:
            # json_object = json.dumps(kwargs)
            # if kwargs:
            #     print(f'Kwargs: {kwargs}')
            # if args:
            #     print(f'Kwargs: {args}')
            sig = signature(wr.s3.to_json)
            sba = sig.bind(*args, **kwargs)

            if 'df' in kwargs:
                # df = pd.read_json(args['df'])
                kwargs['df'] = kwargs['df'].to_json()
                json_kwargs_object = json.dumps(kwargs)
            else:
                return wr.s3.to_json(*sba.args, **sba.kwargs)


            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}
            params = json.dumps(args)#{}

            try:
                logging.info('Uploading data...')
                r = self.session.post( \
                    '{}/api/aws/toS3_json'.format(self.base_url), params=params, data=json_kwargs_object,
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('writing data to AWS...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing write response')
                # logging.info(str(r.text))
                if r.text:
                    rJson = json.loads(r.text)
                    logging.info('Done writing.')
                    response_text = rJson.get('text/plain')
                    if (response_text):
                        return json.dumps(rJson.get('text/plain'))
                else:
                    logging.exception('Could not find proper output, please check your parameters')
                # return r.text
            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('aws_to_s3_json , ' + str(e))
            raise Error(e)

    write_to_s3_json.__doc__ = wr.s3.to_json.__doc__.replace('awswrangler','dataplate')


    def write_to_s3_parquet(self, *args, **kwargs):
        try:
            # json_object = json.dumps(kwargs)
            # if kwargs:
            #     print(f'Kwargs: {kwargs}')
            # if args:
            #     print(f'Kwargs: {args}')
            sig = signature(wr.s3.to_parquet)
            sba = sig.bind(*args, **kwargs)

            if 'df' in kwargs:
                # df = pd.read_json(args['df'])
                kwargs['df'] = kwargs['df'].to_json()
                json_kwargs_object = json.dumps(kwargs)
            else:
                return wr.s3.to_json(*sba.args, **sba.kwargs)


            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}
            params = json.dumps(args)#{}

            try:
                logging.info('Uploading data...')
                r = self.session.post( \
                    '{}/api/aws/toS3_parquet'.format(self.base_url), params=params, data=json_kwargs_object,
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('writing data to AWS...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing write response')
                # logging.info(str(r.text))
                if r.text:
                    rJson = json.loads(r.text)
                    logging.info('Done writing.')
                    response_text = rJson.get('text/plain')
                    if (response_text):
                        return json.dumps(rJson.get('text/plain'))
                else:
                    logging.exception('Could not find proper output, please check your parameters')
                # return r.text
            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('aws_to_s3_parquet , ' + str(e))
            raise Error(e)

    write_to_s3_parquet.__doc__ = wr.s3.to_parquet.__doc__.replace('awswrangler','dataplate')


    def run_notebook(self, notebook_file_path, instance_type = "ml.m5.large", parameters = "{}", max_time_limit_minutes = 180, securityGroupIds = [], subnets= []):
        """Run a notebook in SageMaker Processing producing a new output notebook.
        Args:
            notebook (str): The notebook file path.
            input_path (str): The S3 object containing the notebook. If this is None, the `notebook` argument is
                              taken as a local file to upload (default: None).
            parameters (dict): The dictionary of parameters to pass to the notebook (default: {}).
            instance_type (str): The SageMaker instance to use for executing the job (default: ml.m5.large).

        Returns:
            The name of the processing job created to run the notebook.
        """
        try:
            if not notebook_file_path or not os.path.isfile(notebook_file_path) or not notebook_file_path.endswith('.ipynb'):
                raise FileNotFoundError(f'notebook file is not legal/valid : {notebook_file_path if notebook_file_path else "None"}')

            f = open(notebook_file_path, 'r')
            if f:
                # Reading from file
                notebook_json_data = json.loads(f.read())
                # Closing file
                f.close()

            if not notebook_json_data or len(json.dumps(notebook_json_data)) < 10 or not 'cells' in notebook_json_data:
                raise Error(f'notebook file is not legal : {notebook_file_path if notebook_file_path else "None"}')

            notebook_name = os.path.basename(notebook_file_path)
            params = {}
            if instance_type:
                params['instance_type'] = instance_type
            if parameters:
                params['parameters'] = parameters
            if max_time_limit_minutes:
                params['timelimit_minutes'] = max_time_limit_minutes
            params['SecurityGroupIds'] = securityGroupIds
            params['Subnets'] = subnets
            params['notebook_name'] = notebook_name if notebook_name else ""


            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('Uploading data...')
                r = self.session.post( \
                    '{}/api/aws/runNotebook'.format(self.base_url), params=params, data=json.dumps(notebook_json_data),
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('running notebook, processing...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    rJson = json.loads(r.text)
                    logging.info('run notebook finished successfully.')
                    return json.dumps(rJson)
                else:
                    logging.exception('Could not find proper output, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('run_notebook , ' + str(e))
            raise Error(e)


    def list_runs_notebook(self, n=10, notebook = None, rule = None):
        """Returns a pandas data frame of the runs, with the most recent at the top.
        Args:
        n (int): The number of runs to return or all runs if 0 (default: 10)
        notebook (str): If not None, return only runs of this notebook (default: None)
        rule (str): If not None, return only runs invoked by this rule (default: None)
        """

        try:

            params = {}
            if n:
                params['n'] = n
            if notebook:
                params['notebook'] = notebook
            if rule:
                params['rule'] = rule

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('sending request...')
                r = self.session.post( \
                    '{}/api/aws/listRunsNotebook'.format(self.base_url), params=params, data="",
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('analysing notebook runs...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    rJson = json.loads(r.text)
                    logging.info('list notebook runs finished successfully.')
                    df = pd.read_json(rJson)
                    df['Created'] = pd.to_datetime(df['Created'], unit='ms',utc=True)
                    df['Start'] = pd.to_datetime(df['Start'], unit='ms', utc=True)
                    df['End'] = pd.to_datetime(df['End'], unit='ms', utc=True)
                    df['Elapsed'] = pd.to_timedelta(df['Elapsed'], unit='ms')
                    return df
                else:
                    logging.exception('Could not find proper output, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('list_runs_notebook , ' + str(e))
            raise Error(e)



    def stop_run_notebook(self, job_name= None):
        """Stop the named processing job.
        Args:
        job_name (string): The name of the job to stop. use list_runs_notebook to get specific notebook Job name
        """

        try:

            params = {}
            if job_name:
                params['jobname'] = job_name
            else:
                raise Error('Not a valid job name, use list_runs_notebook function to get specific notebook Job name.')

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('sending request...')
                r = self.session.post( \
                    '{}/api/aws/stopNotebook'.format(self.base_url), params=params, data="",
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('analysing notebook stops...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    logging.info(r.text)
                    return
                else:
                    logging.exception('Could not find proper result, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('stop_run_notebook , ' + str(e))
            raise Error(e)


    def download_notebook_result(self, result_s3_file= None, output="."):
        """Download the output notebook from a previously completed job.

        Args:
          result_s3_file (str): The name of the SageMaker Processing Job Result that executed the notebook. (Required). use list_runs_notebook to get specific Result of Job
          output (str): The directory to copy the output file to. (Default: the current working directory)

        Returns:
          The filename of the downloaded notebook.
        """

        try:
            params = {}
            if result_s3_file:
                params['result_file'] = result_s3_file
            else:
                raise Error('Not a valid job name, use list_runs_notebook function to get specific notebook Job name.')

            headers = {'X-Access-Key': self.access_key, 'Content-Type': 'application/json'}

            try:
                logging.info('sending request...')
                r = self.session.post( \
                    '{}/api/aws/downloadNotebook'.format(self.base_url), params=params, data="",
                    headers=headers, stream=True, allow_redirects=False)

                if r.status_code != 200:
                    if r.status_code == 302:
                        raise Error(
                            'Bad Access Key! Get your access key at: {}'.format(
                                self.base_url))
                    if r.status_code == 206:
                        logging.info('analysing notebook stops...')
                        time.sleep(5)
                    raise Error(
                        'Bad HTTP exit status returned from the API: {}. Error was: {}'.
                            format(r.status_code, r.text))

                logging.info('Parsing response')
                # logging.info(str(r.text))
                if r.text:
                    # rJson = json.loads(r.text)
                    logging.info('Got notebook result successfully.')
                    # return json.dumps(rJson)
                    if not os.path.exists(output):
                        try:
                            os.makedirs(output)
                        except OSError as e:
                            raise Error(f'Could not crate output directory {output}')


                    o = urlparse(result_s3_file, allow_fragments=False)
                    # ParseResult(scheme='s3', netloc='bucket_name', path='/folder1/folder2/file1.json', params='', query='',
                    #             fragment='')
                    base_notebook_name = ""
                    split_path = o.path.split('/')
                    if split_path and len(split_path) > 0:
                        if len(split_path[-1]) > 0 and split_path[-1].find('.') >= 0:
                            base_notebook_name = split_path[-1]

                    filename_out = '/'.join([str(output.rstrip("/")), str(base_notebook_name)])
                    # with open(filename_out.rstrip("/"), 'wb') as fh:
                    #     copyfileobj(json.loads(r.text), fh)
                    f = open(filename_out.rstrip("/"), 'w', encoding = 'utf-8')
                    if f:
                        # writing file
                        json.dump(json.loads(r.text), f, ensure_ascii=False)#, indent=4)
                        # Closing file
                        f.close()

                    logging.info('Done writing to file.')
                else:
                    logging.exception('Could not find proper result, please check your parameters')
                # return r.text

            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout) as e:
                logging.exception('Got ConnectionError/ReadTimeout exception.')
                raise Error(e)

        except Exception as e:
            logging.exception('download_notebook_result , ' + str(e))
            raise Error(e)
