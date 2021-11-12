import requests

def raise_for_status_with_message(resp):
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as error:
        if resp.text:
            raise requests.exceptions.HTTPError('{} \nError message: {}'.format(str(error), resp.text))
        else:
            raise error


class WiW(object):
    """.. py:class: WhenIWork([:param token:=None, :param options:=dict()])
    :param token: The user WhenIWork API token
    :param options: Allows you to set the `headers` and the `endpoint` from a dict.

    Methods:

    """
    # Private Variables
    __api_token = None
    __api_headers = {}
    __api_endpoint = "https://api.wheniwork.com/2"
    __tags_api_endpoint = "https://worktags.api.wheniwork-production.com"
    __verify_ssl = False
    __api_resp = None

    def __init__(self, token=None, options=None):
        """
        .. py:method:: init
        Create a new instance.
        :param token: The user WhenIWork API token
        :param options: Allows you to set the `headers` and the `endpoint` from a dict.
        """
        self.__api_token = token

        if isinstance(options, dict):
            if 'headers' in options:
                self.__api_headers = options['headers']

            if 'endpoint' in options:
                self.__api_endpoint = options['endpoint']

    @property
    def token(self):
        """
        Used to set or retrieve the user's api token::

            from wheniwork import WhenIWork

            a = WhenIWork()
            a.token = "ilovemyboss"
            print(a.token)
        """
        return self.__api_token

    @property
    def endpoint(self):
        """
        Used to set or retrieve the standard api endpoint::

            from wheniwork import WhenIWork

            a = WhenIWork()
            a.endpoint = "https://api.wheniwork.com/2"
            print(a.endpoint)
        """
        return self.__api_endpoint

    @property
    def endpoint_tags(self):
        """
        Used to set or retrieve the tagging api endpoint::

            from wheniwork import WhenIWork

            a = WhenIWork()
            a.endpoint_tags = "https://worktags.api.wheniwork-production.com"
            print(a.endpoint)
        """
        return self.__tags_api_endpoint

    @property
    def headers(self):
        """
        Used to set or retrieve the api endpoint::

            from wheniwork import WhenIWork

            a = WhenIWork()
            a.headers = {W-Key:"iworksoharditsnotfunny"}
            print(a.headers['W-Key'])
        """
        return self.__api_headers

    @headers.setter
    def headers(self, headers):
        """

        :param headers:
        :return:
        """
        self.__api_headers = headers

    @property
    def resp(self):
        """
        Used to get the last API Response Data::

            from wheniwork import WhenIWork

            a = WhenIWork(token="iworksomuchitsnotfunny")
            a.get("/locations")
            print(a.resp)

        Note: This is a read only variable.
        """
        return self.__api_resp
    
    @property
    def user_id(self):
        """
        Used to set or retrieve the api endpoint::

            from wheniwork import WhenIWork

            a = WhenIWork()
            a.headers = {W-Key:"iworksoharditsnotfunny"}
            print(a.headers['W-Key'])
        """
        if self.headers['W-UserID'] :
            return self.headers['W-UserID']

    @headers.setter
    def user_id(self, user_id):
        """

        :param headers:
        :return:
        """
        self.headers['W-UserID'] = user_id

    def get(self, method, params=None, headers=None, api=None):
        """
        Send a get request to the WhenIWork api

        :param method: The API method to call, e.g. '/users'
        :param params: a dictionary of arguments to pass the method
        :param headers: a dictionary of custom headers to be passed.
        :return: a dictionary of the decoded json API response.

        """
        if isinstance(method, str):
            if self.token is not None:
                if api == 'tags':
                    url = self.endpoint_tags+method
                else:
                    url = self.endpoint+method
                head = {'W-Token': self.token}
                head.update(self.headers)
                if headers:
                    head.update(headers)
                resp = requests.get(url, params, headers=head)
                raise_for_status_with_message(resp)
                self.__api_resp = resp.json()
                return self.resp
            else:
                return {'error': 'Token is not set'}
        else:
            return {'error': 'Wrong method format'}

    def post(self, method, params=None, headers=None, api=None):
        """
        POST to the WhenIWork api

        :param method: The API method to call, e.g. '/users'
        :param params: a dictionary of arguments to pass the method
        :param headers: a dictionary of custom headers to be passed.
        :return: a dictionary of the decoded json API response.
        """
        if isinstance(method, str):
            if self.token is not None:
                if api == 'tags':
                    url = self.endpoint_tags+method
                else:
                    url = self.endpoint+method
                head = {'W-Token': self.token}
                head.update(self.headers)
                if headers:
                    head.update(headers)
                resp = requests.post(url, json=params, headers=head)
                raise_for_status_with_message(resp)
                self.__api_resp = resp.json()
                return self.resp
            else:
                return {'error': 'Token is not set'}
        else:
            return {'error': 'Wrong method format'}


    def update(self, method, params=None, headers=None, api=None):
        """
        Update an object on WhenIWork

        :param method: The API method to call, e.g. '/users/1' MUST INCLUDE ID OF OBJECT.
        :param params: a dictionary of arguments to pass the method
        :param headers: a dictionary of custom headers to be passed.
        :return: a dictionary of the decoded json API response.
        """
        if isinstance(method, str):
            if self.token is not None:
                if api == 'tags':
                    url = self.endpoint_tags+method
                else:
                    url = self.endpoint+method
                head = {'W-Token': self.token}
                head.update(self.headers)
                if headers:
                    head.update(headers)
                resp = requests.put(url, json=params, headers=head)
                raise_for_status_with_message(resp)
                self.__api_resp = resp.json()
                return self.resp
            else:
                return {'error': 'Token is not set'}
        else:
            return {'error': 'Wrong method format'}

    def delete(self, method, headers=None, api=None):
        """
                Delete an object on WhenIWork

                :param method: The API method to call, e.g. '/users/1' MUST INCLUDE ID OF OBJECT.
                :param headers: a dictionary of custom headers to be passed.
                :return: a dictionary of the decoded json API response.
                """
        if isinstance(method, str):
            if self.token is not None:
                if api == 'tags':
                    url = self.endpoint_tags+method
                else:
                    url = self.endpoint+method
                head = {'W-Token': self.token}
                head.update(self.headers)
                if headers:
                    head.update(headers)
                resp = requests.delete(url, headers=head)
                raise_for_status_with_message(resp)
                self.__api_resp = resp.json()
                return self.resp
            else:
                return {'error': 'Token is not set!!'}
        else:
            return {'error': 'Method is not str!!'}

    def get_positions(self, show_deleted = False):
        params = {'show_deleted': show_deleted}
        return self.get('/positions', params=params)['positions']

    def get_jobsites(self, include_deleted = False):
        params = {'include_deleted': include_deleted}
        return self.get('/sites', params=params)['sites']
    
    def get_schedules(self):
        return self.get('/locations')['locations']

    def get_position(self, position_id : int):
        if position_id :
            return self.get('/positions/' + str(position_id))['position']
        else :
            return {'error' : 'id not specified'}

    def get_jobsite(self, jobsite_id : int):
        if jobsite_id :
            return self.get('/sites/' + str(jobsite_id))['site']
        else :
            return {'error' : 'id not specified'}
    
    def get_schedule(self, schedule_id : int):
        if schedule_id :
            return self.get('/locations/' + str(schedule_id))['location']
        else :
            return {'error' : 'id not specified'}

    def create_position(self, position_name : str):
        if position_name : 
            param = {
                'name' : position_name
                }
            return self.post('/positions', params = param)
        else :
            return {'error' : 'name not specified'}

    def create_jobsite(self, jobsite_name : str, schedule_id : int):
        if jobsite_name and schedule_id: 
            param = {
                'name' : jobsite_name, 
                'location_id' : schedule_id
                }
            return self.post('/sites', params = param)
        else :
            return {'error' : 'site name or schedule_id not specified'}

    def create_schedule(self, schedule_name : str):
        if schedule_name : 
            param = {
                'name' : schedule_name
                }
            return self.post('/locations', params = param)
        else :
            return {'error' : 'name not specified'}
    
    def get_users(self, location_id =None, show_pending = None, only_pending = None, show_deleted = None, search = None):
        if 1 == 1 :
            param = {
                # 'location_id' : location_id, 
                'show_pending' : show_pending, 
                'only_pending' : only_pending, 
                'show_deleted' : show_deleted,
                'search' : search
                }
            return self.get('/users', params = param)['users']
        else :
            return {'error' : 'location_id not specified'}
    
    def get_user(self, id : int):
        if id :
            return self.get('/users/' + str(id))['user']
        else :
            return {'error' : 'user_id not specified'}

    def create_user(self, email : str, first_name : str, last_name : str, stuart_id : str, positions = None, schedules = None):
        if email and first_name and last_name and stuart_id :
            param = {
                'email' : email,
                'first_name' : first_name,
                'last_name' : last_name,
                'employee_code' : stuart_id,
                'positions' : positions,
                'locations' : schedules,
                'is_hidden' : False,
                'is_payroll' : False,
                'is_private' : True,
                'is_trusted' : False
            }
            return self.post('/users', params=param)
        else :
            return {'error' : 'missing argument'}

    def invite_users(self, ids : list):
        if ids :
            param = {
                'ids' : ids
            }
            return self.post('/users/invite', params=param)
        else :
            return {'error' : 'missing ids or wrong type'}

    def update_user(self, id : int, **kwargs):
        if id :
            param = {}
            for key, value in kwargs.items():
                param.update({str(key): value})
            return self.update('/users/' + str(id), params=param)
        else :
            return {'error' : 'missing id or wrong type'}

    def list_shifts(self, start : str, end : str, unpublished : bool, schedule_id, position_id, include_open = True, include_allopen = True, include_onlyopen = False, deleted = False, all_locations = False) :
        if all_locations == True :
            location_id = None
            position_id = None
        param = {
            'start' : start,
            'end' : end,
            'unpublished' : unpublished,
            'include_open' : include_open,
            'include_allopen' : include_allopen,
            'include_onlyopen' : include_onlyopen,
            'deleted' : deleted,
            'all_locations' : all_locations,
            'location_id' : schedule_id,
            'position_id' : position_id
        }
        return self.get('/shifts', params=param)

    def get_shift(self, id : int):
        if id :
            return self.get('/shifts/' + str(id))
        else :
            return {'error' : 'missing id or wrong type'}
    
    def get_shift_history(self, id : int):
        if id :
            return self.get('/shifts/history/' + str(id))['history']
        else :
            return {'error' : 'missing id or wrong type'}
    
    def delete_shift(self, id : int):
        if id :
            return self.delete('/shifts/' + str(id))
        else :
            return {'error' : 'missing id or wrong type'}
    
    def create_shift(self, schedule_id, position_id, site_id, start, end, coverage, user_id = 0):
        if schedule_id and position_id and site_id and start and end and coverage :
            param = {
                'user_id' : user_id, 
                'location_id' : schedule_id, 
                'position_id' : position_id, 
                'site_id' : site_id, 
                'start_time' : start, 
                'end_time' : end, 
                'instances' : coverage
            }
            return self.post('/shifts', params=param)
        else :
            return {'error' : 'missing argments or wrong type'}

    def publish_schedule(self, ids:list):
        param = {
            'ids' : ids
        }
        return self.post('/shifts/publish', params=param)

    def unpublish_schedule(self, ids:list):
        param = {
            'ids' : ids
        }
        return self.post('/shifts/unpublish', params=param)

    def add_driver_position(self, id : int, prio_position: int):
        if id :
            positions = self.get_user(id)['positions']
            positions.append(prio_position)
            param = {
                'positions' : positions
            }
            return self.update('/users/' + str(id), params=param)
        else :
            return {'error' : 'missing id or wrong type'}

    def remove_driver_position(self, id : int, prio_position: int):
        if id :
            positions = self.get_user(id)['positions']
            positions.remove(prio_position)
            param = {
                'positions' : positions
            }
            return self.update('/users/' + str(id), params=param)
        else :
            return {'error' : 'missing id or wrong type'}

    def unassign_shifts(self, ids : list):
        if ids:
            param = {
                'shift_ids' : ids
            }
            return self.post('/shifts/unassign', params=param)
        else:
            {'error' : 'missing id or wrong type'}


    def get_tags(self):
        return self.get('/tags', api='tags')

    def get_tag(self, id: str):
        if id: 
            param = {
                'id' : id
            }
            return self.get('/tags/' + id, params=param, api='tags')
        else:
            {'error' : 'missing id or wrong type'}

    def get_user_tags(self, id: int):
        if id: 
            param = {
                'id' : id
            }
            return self.get('/users/' + str(id), params=param, api='tags')
        else:
            {'error' : 'missing id or wrong type'}

    def get_shift_tags(self, id: int):
        if id: 
            param = {
                'id' : id
            }
            return self.get('/shifts/' + str(id), params=param, api='tags')
        else:
            {'error' : 'missing id or wrong type'}

    def create_tag(self, tag_name: str):
        if tag_name:
            param = {
                'name': tag_name
            }
            return self.post('/tags', params=param, api='tags')
        else: 
            return {'error': 'tag name not specified or wrong type'}

    def list_user_tags(self, user_ids: list):
        ''' user id's in list must be strings '''
        if user_ids:
            param = {
                'ids': user_ids
            }
            return self.post('/users', params=param, api='tags')
        else: 
            return {'error': 'missing ids or wrong type'}

    def list_shift_tags(self, shift_ids: list):
        ''' shift id's in list must be strings '''
        if shift_ids:
            param = {
                'ids': shift_ids
            }
            return self.post('/shifts', params=param, api='tags')
        else: 
            return {'error': 'missing ids or wrong type'}

    def update_tag(self, id: str, tag_name: str):
        if tag_name:
            param = {
                'name': tag_name
            }
            return self.update('/tags/' + id, params=param, api='tags')
        else: 
            return {'error': 'id not specifed or wrong type'}

    def update_user_tags(self, id: int, tags: list):
        if id:
            param = {
                'tags': tags
            }
            return self.update('/users/' + str(id), params=param, api='tags')
        else: 
            return {'error': 'id not specifed or wrong type'}

    def update_shift_tags(self, id: int, tags: list):
        if id:
            param = {
                'tags': tags
            }
            return self.update('/shifts/' + str(id), params=param, api='tags')
        else: 
            return {'error': 'id not specifed or wrong type'}

    def delete_tag(self, id: str):
        if id:
            return self.delete('/tags/' + id, api='tags')
        else:
            return {'error' : 'missing id or wrong type'}