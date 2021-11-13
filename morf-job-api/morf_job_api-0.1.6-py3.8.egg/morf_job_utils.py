import requests
from http import HTTPStatus as status
from requests.exceptions import ConnectTimeout
from requests.models import MissingSchema


def submit_job(job_config):
    """
    Submits a job to the morf backend.

        Parameters:
            job_config (dict): A dictionary containing the location of the job zip file that will be submitted, the API endpoint, and an API key.
                Keys:
                    job_zip_file (str): The path to the job zip file that will be uploaded
                    morf_api_endpoint (str): The API endpoint URL the job will be submitted to.
                    api_key (str): The API key that will be used to access the endpoint.
                    output_function (str): Optional. If present, the MORF backend will execute this function on the extracted data.
    """
    # Create an HTTP request header and add the API key to it
    headers = {'Authorization': 'Bearer {}'.format(job_config['api_key'])}
    if('output_function' in job_config.keys()):
        headers['output-function'] = job_config['output_function']
    # Submit an HTTP request with the job config parameters.
    try:
        response = requests.post(job_config['morf_api_endpoint'], files={
            "job_zip_file": open(job_config['job_zip_file'], "rb")}, headers=headers, timeout=3)
        # If the response is OK (200), job has been submitted successfully.
        if(response.status_code == status.OK):
            print('Job submitted successfuly.')
        # Otherwise, something is not OK. The response content should include information about what went wrong.
        else:
            print(response.content.decode('utf-8'))
    # Error - Job zip file not found.
    except FileNotFoundError:
        print("The job zip file was not found in the location you provided.")
    # Error - The connection has timed out. Is the backend running and exposing an API at this URL?
    except (ConnectTimeout):
        print("Connection timed out.")
    # Error - The URL provided is not valid.
    except MissingSchema:
        print('The API endpoint you provided is invalid.')
