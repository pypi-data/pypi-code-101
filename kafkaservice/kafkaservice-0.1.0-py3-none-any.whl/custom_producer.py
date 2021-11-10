import yaml
from .constant import Constant
from .utils import Utils
from kafka import KafkaProducer

class CustomKafkaProducer:
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file
        self._initConfig()
        
    def _initConfig(self):
        self.doc = self.load_doc()
        self.config = self.get_config()
        self.producer = KafkaProducer(bootstrap_servers=self.config['bootstrap_servers'])
    
    def load_doc(self):
        with open(self.yaml_file, 'r') as stream:
            try:
                return yaml.full_load(stream)
            except yaml.YAMLError as exception:
                raise exception
                
    def get_config(self):
        doc_keys = self.doc.keys()
        
        config = {}
        for key in Constant.CONFIG_KEYS:
            try:
                config[key] = self.doc[key]
            except:
                print("Missing {} config".format(key))
        return config
    
    def kafka_python_producer_sync(self, msg):
        future = self.producer.send(self.config['topic'], msg)
        result = future.get(timeout=self.config['timeout'])
        self.producer.flush()
        
    def kafka_python_producer_async(self, msg):
        self.producer.send(self.config['topic'], msg).add_callback(Utils.success).add_errback(Utils.error)
        self.producer.flush()