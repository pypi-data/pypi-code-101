import json, logging, requests,os
from os import listdir
from os.path import isfile, join
from robot.api.deco import keyword
from robot.output import stdoutlogsplitter
from robot.api import logger

logging.basicConfig(level = logging.INFO)

class AllureClient(object):
    """A robot framework Library that contains keywords for controlling allure docker service using 
     the following api (http://47.114.163.85/swagger/allure-docker-service/). 
     the basic calling of the liberary is as follows: 
        | Library | AllureClient | ${stf_base_url} |
     the most common responses are:
        | 200 | Success |
        | 400 | Bad Request: Some parameters are missing or invalid |
        | 404 | Not found: The item not available |
    """
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LIBRARY_DOC_FORMAT = "ROBOT" 

    def __init__(self,  base_url=None):
        """ the base url of the allure server e.g., http://47.114.163.85/allure-docker-service/) """
        self.baseurl = base_url
    ############## Info #########################
    @keyword('Get allure version')
    def get_version(self):
        """get Allure version"""        
        response = requests.get(self.baseurl + "/version")
        if response.status_code == 200:
            version = response.json()['data']['version']
            logging.info(response.json()['meta_data']['message'])
            return version
        else:
            logging.error("Error in processing %s: %s",self.baseurl, response)

    @keyword('Get swagger API doc')
    def get_swagger_api_doc(self):
        """ Get Swagger API Doc """        
        response = requests.get(self.baseurl + "/swagger")
        if response.status_code == 200:
            return response.text
        else:
            logging.error("Error in processing %s: %s",self.baseurl, response)

    @keyword('Get Swagger API Specification')
    def get_swagger_api_spec(self):
        """ Get Swagger API Specification """        
        response = requests.get(self.baseurl + "/swagger.json")
        if response.status_code == 200:
            return response.json()
        else:
            logging.error("Error in processing %s: %s",self.baseurl, response)

    ############## Action #########################
    @keyword('Get Allure config')
    def get_allure_config(self):
        """ Get Swagger API Specification """        
        response = requests.get(self.baseurl + "/config")
        if response.status_code == 200:
            logging.info(response.json()['meta_data']['message'])
        else:
            logging.error("Error in processing %s: %s",self.baseurl, response)

    @keyword('Get latest report')
    def get_latest_report(self, project_id):        
        """ Get latest report """        
        params = {'project_id': project_id}
        response = requests.get(self.baseurl + "/latest-report", params=params)
        if response.status_code == 200:
            logging.info(response.text)
        else:
            logging.error("Error in processing %s: %s",self.baseurl, response)

    @keyword('Send results files')
    def Send_results_files(self, project_id, force_project_creation, report_folder):        
        """ Send results files """        
        prepfiles = [('files[]',(f,open(report_folder + "/"+ f,'rb'),'application/json')) for f in os.listdir(report_folder) if isfile(join(report_folder, f))]
        params = {'project_id': project_id, 'force_project_creation': force_project_creation}
        response = requests.post(self.baseurl + "/send-results", params=params, files=prepfiles)
        if response.status_code == 200:
            logging.info(response.json()['meta_data']['message'])
        else:
            logging.error("Error in processing %s: %s",self.baseurl, response)

    @keyword('Generate new report')
    def generate_new_report(self,project_id,execution_name=None,execution_from=None,execution_type=None):
        """ Generate new report """        
        params = {'project_id': project_id, 'execution_name':execution_name, 'execution_from':execution_from, 'execution_type':execution_type}
        response = requests.get(self.baseurl + "/generate-report", params=params)
        if response.status_code == 200:
            logging.info(response.json()['meta_data']['message'])
        else:
            logging.error("Error in processing %s: %s",self.baseurl, response)
    
    @keyword('Clean history')
    def clean_history(self,project_id):
        """ Clean Allure history & trends """        
        response = requests.get(self.baseurl + "/clean-history?project_id="+project_id)
        if response.status_code == 200:
            logging.info(response.json()['meta_data']['message'])
        else:
            logging.info("Error in processing %s: %s",self.baseurl, response.content)
    
    @keyword('​Clean results')
    def clean_results(self,project_id):
        """ Clean Allure results """        
        response = requests.get(self.baseurl +"/clean-results?project_id="+project_id)
        if response.status_code == 200:
            logging.info(response.json()['meta_data']['message'])
        else:
            logging.error("Error in processing %s: %s",self.baseurl, response)

    @keyword('​Export emailable Allure report')
    def export_emailable_report(self,project_id, path):
        """ Export emailable Allure report """        
        response = requests.get(self.baseurl + "/emailable-report/export?project_id="+project_id)
        if response.status_code == 200:
            with open(os.getcwd()+ path+'\\emailable-report-allure-docker-service.html', 'wb') as f:
                f.write(response.content)
            logging.info('done')
        else:
            logging.error("Error in processing %s: %s",self.baseurl, response)

    @keyword('​Render emailable Allure report')
    def render_emailable_report(self,project_id):
        """ Render emailable Allure report """        
        response = requests.get(self.baseurl + "/emailable-report/render?project_id="+project_id)
        if response.status_code == 200:
            logging.info(response.content)
        else:
            logging.error("Error in processing %s: %s",self.baseurl, response)

    @keyword('​Export Allure report')
    def export_allure_report(self,project_id):
        """ Export Allure report """        
        response = requests.get(self.baseurl + "/emailable-report/render?project_id="+project_id)
        if response.status_code == 200:
            logging.info(response.content)
        else:
            logging.error("Error in processing %s: %s",self.baseurl, response)          

    ############## project #########################
    @keyword('​Get all projects')
    def get_all_projects(self):
        """ Get all projects """        
        response = requests.get(self.baseurl + "/projects")
        if response.status_code == 200:
            logging.info(response.json()['data']['projects'])
            logging.info(response.json()['meta_data']['message'])
        else:
            logging.error("Error in processing %s: %s",self.baseurl, response)    

    @keyword('​Create a new project')
    def create_a_new_project(self,project_id):
        """ Create a new project """        
        payload = json.dumps({"id": project_id})
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.baseurl + "/projects",data=payload, headers=headers)
        if response.status_code == 201:
            logging.info(response.json()['data']['id'])
            logging.info(response.json()['meta_data']['message'])
        else:
            logging.error("Error in processing %s: %s",self.baseurl, response)    

    @keyword('​Search projects')
    def search_projects(self,project_id):
        """ Search projects """ 
        response = requests.get(self.baseurl + "/projects/search?id="+project_id)
        if response.status_code == 200:
            logging.info(response.json()['data']['projects'])
            logging.info(response.json()['meta_data']['message'])
        else:
            logging.error("Error in processing %s: %s",self.baseurl, response)    

    @keyword('​Delete an existent project')
    def delete_an_existent_project(self,project_id):
        """ Delete an existent project """ 
        response = requests.delete(self.baseurl + "/projects/"+project_id)
        if response.status_code == 200:
            logging.info(response.json()['meta_data']['message'])
        else:
            logging.error("Error in processing %s: %s",self.baseurl, response)    

    @keyword('​Get an existent project')
    def get_an_existent_project(self,project_id):
        """ Get an existent project """ 
        response = requests.delete(self.baseurl + "/projects/"+project_id)
        if response.status_code == 200:
            logging.info(response.json()['data']['projects'])
            logging.info(response.json()['meta_data']['message'])
        else:
            logging.error("Error in processing %s: %s",self.baseurl, response)    

    @keyword('​Get reports')
    def get_reports(self,project_id, path, redirect):
        """ Get reports """ 
        response = requests.get(self.baseurl + "/projects/"+project_id+"/reports/"+path+"?redirect="+redirect)
        if response.status_code == 200:
            logging.info(response.json()['data']['project'])
            logging.info(response.json()['meta_data']['message'])
        else:
            logging.error("Error in processing %s: %s",self.baseurl, response)