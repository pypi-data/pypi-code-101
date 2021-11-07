
from entity.observations import Observations
import json
o = Observations()
import uuid

class Entity:
    """ SHORT DESCRIPTION OF CLASS

    entity represent on object (entity), simplifies calls to observations by storing @type and @id
    observations is a db of all observation objects
    observation is a single observation(key, value) for a given entity

    Attributes:
        record_type(string): The '@type' value of the entity
        record_id(string): The '@id' value of the entity
    
    Methods:
    
        add: Add a datapoint
        get: Get all observations
        update_record_id: changes record_id and all other entities ref to it

    OBSERVATIONS:
    get_observations
    get_min
    get_max

    JSON:
    get_json
    load_json

    """

    def __init__(self, record_type = None, record_id = None, value = None):
        self._record_id = record_id
        self._record_type = record_type

        if value:
            self.post_json_entity(value)



    def __str__(self):
        return json.dumps(self.record, default = str, indent = 4)

    def __repr__(self):
        return str(self.record)


    def __eq__(self, other):

        if self.record_type == other.record_type and self.record_id == other.record_id:
            return True
        else:
            return False

    def __in__(self, others):

        for i in others:
            if self.__eq__(other):
                return True

        return False



    """
    Properties
    """
    
    
    
    @property
    def record_type(self):
        return self._record_type

    @record_type.setter
    def record_type(self, value):

        if value:
            self._record_type = value

        
    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):

        if value:
            self._record_id = value

    

    @property
    def record_link(self):
        """ Identifier
        """
        record = {
            'record_type': self.record_type, 
            'record_id': self.record_id
        }
        return record
        
    @property
    def record(self):
        """ Identifier
        """
        
        return o.get_json_entity(self.record_type, self.record_id)

    @property
    def record_full(self):
        """ Identifier
        """
        
        return o.get_json_entity(self.record_type, self.record_id, False, True)

    def keys(self):
        # Return list of keys
        return o(self.record_type, self.record_id).keys()
    

    """
    API
    """

    def get(self, format = 'json'):

        if format == 'json':
            return self.get_json_entity()
        elif format == 'json_detailed':
            return self.get_json_entity(True)


    def post(self, value, **kwargs):

        if isinstance(value, (dict, list)):
            self.post_json_entity(value, **kwargs)


    def search(self, record_type = None, record_id = None, **kwargs):
        
        observations = o.search(record_type, record_id, **kwargs)

        entities = []

        for i in observations:
            e = Entity(i.record_type, i.record_id)
            if e not in entities:
                entities.append(e)

        return entities


    """
    Methods - Observations
    methodds that returns data as observation class
    """

    def post_observation(self, observation):
        """Add one or many Observations objects
        """
        o.post_observation(observation)

    def get_observations(self, attr):
        """Returns Observations objects for a given attribute/key
        """
        
        return o.get_observations(self.record_type, self.record_id, attr)

    def get_min(self, attr):
        """Returns smallest observation for a given attribute/key
        """
        return o.get_min(self.record_type, self.record_id, attr)

    def get_max(self, attr):
        """Returns greatest observation for a given attribute/key
        """        
        return o.get_max(self.record_type, self.record_id, attr)


    # Work with observations
    def get_entity(self):
        # Return all keys and all observations for entity
        return o.get_entity(self.record_type, self.record_id)



    def update_record_id(self, new_record_id):
        """Update record_id and all associated references
        """
        o.update_record_id(self.record_type, self.record_id, new_record_id)
        self.record_id = new_record_id
        
        
        return

    """
    Methods - JSON
    Methods that returns data as json
    """
    # WOrk with json

    def get_json_entity(self, expanded = False, full = False):
        # Returns json object (dict). Expanded returns also nested child records. Full returns metadata as well
        return o.get_json_entity(self.record_type, self.record_id, expanded, full)

    
    def post_json_entity(self, value, **kwargs):
        """Load a dict into entity, creating a series of Observations.
        """ 


        # If value contains @id, use it
        if isinstance(value, dict):
            self.record_type = value.get('@type', 'schema:na')
            self.record_id = value.get('@id', str(uuid.uuid4()))
            value['@type'] = self.record_type
            value['@id'] = self.record_id


        o.post_json_entity(self.record_type, self.record_id, None, value, **kwargs)

        return 


    """
    API text
    """
    def get_text_entity(self, key = None):
        return o.get_text_entity(self.record_type, self.record_id, key)

    """
    I/O
    """
    
    def read(self): 
        return o.read(self.record_type, self.record_id)
    
    def write(self):

        return o.write(self.record_type, self.record_id)
        

    def write_all(self):
        o.write_all()