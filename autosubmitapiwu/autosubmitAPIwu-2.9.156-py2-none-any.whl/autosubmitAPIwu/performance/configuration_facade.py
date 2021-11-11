#!/usr/bin/env python
import os
import math
from autosubmitAPIwu.config.basicConfig import BasicConfig
from autosubmitAPIwu.config.config_common import AutosubmitConfig
from bscearth.utils.config_parser import ConfigParserFactory
from autosubmitAPIwu.job.job_utils import datechunk_to_year
from abc import ABCMeta, abstractmethod
from utils import JobSection, parse_number_processors
from typing import List


class ConfigurationFacade:
  """ """
  __metaclass__ = ABCMeta
  
  def __init__(self, expid):
    self.basic_configuration = BasicConfig # type : BasicConfig
    self.basic_configuration.read()
    self.configuration_parser = ConfigParserFactory
    self.expid = expid # type : str    
    self.pkl_path = None # type : str
    self.tmp_path = None # type : str
    self.chunk_unit = None # type : str
    self.chunk_size = None # type : str
    self.current_years_per_sim = 0.0 # type : float
    self.sim_processors = 0  # type : int
    self.warnings = [] # type : List 
    self._process_basic_config()


  def _process_basic_config(self):
    pkl_filename = "job_list_{0}.pkl".format(self.expid)    
    self.pkl_path = os.path.join(self.basic_configuration.LOCAL_ROOT_DIR, self.expid, "pkl", pkl_filename)
    self.tmp_path = os.path.join(BasicConfig.LOCAL_ROOT_DIR, self.expid, BasicConfig.LOCAL_TMP_DIR)
    if not os.path.exists(self.pkl_path): raise Exception("Required file {0} not found.".format(self.pkl_path))
    if not os.path.exists(self.tmp_path): raise Exception("Required folder {0} not found.".format(self.tmp_path))
  
  @abstractmethod
  def _process_advanced_config(self):
    """ """

class BasicConfigurationFacade(ConfigurationFacade):
  """ BasicConfig and paths """
  def __init__(self, expid):
    # type : (str) -> None
    super(BasicConfigurationFacade, self).__init__(expid)

class AutosubmitConfigurationFacade(ConfigurationFacade):
  """ Autosubmit Configuration includes Basic Config """
  def __init__(self, expid):
    # type : (str) -> None
    super(AutosubmitConfigurationFacade, self).__init__(expid)
    self._process_advanced_config()
  
  def _process_advanced_config(self):
    """ Advanced Configuration from AutosubmitConfig """
    # type : () -> None
    autosubmit_conf = AutosubmitConfig(self.expid, BasicConfig, ConfigParserFactory())    
    autosubmit_conf.reload()    
    self.chunk_unit = autosubmit_conf.get_chunk_size_unit()
    self.chunk_size = autosubmit_conf.get_chunk_size()
    self.current_years_per_sim = datechunk_to_year(self.chunk_unit, self.chunk_size)
    self.sim_processors = self._get_processors_number(autosubmit_conf.get_processors(JobSection.SIM))
  
  def update_sim_jobs(self, sim_jobs):
    """ Update the jobs with the latest configuration values: Processors, years per sim """    
    # type : (List[Job]) -> None
    for job in sim_jobs:
      job.set_ncpus(self.sim_processors)
      job.set_years_per_sim(self.current_years_per_sim)

  def _get_processors_number(self, conf_sim_processors):
    # type : (str) -> int
    num_processors = 0
    try:
        if str(conf_sim_processors).find(":") >= 0:            
            num_processors = parse_number_processors(conf_sim_processors)
            self._add_warning("Parallelization parsing | {0} was interpreted as {1} cores.".format(
                conf_sim_processors, num_processors))
        else:
            num_processors = int(conf_sim_processors)
    except Exception as exp:
        # print(exp)
        self._add_warning(
            "CHSY Critical | Autosubmit API could not parse the number of processors for the SIM job.")
        
    return num_processors
  
  def _add_warning(self, message):
    # type : (str) -> None
    self.warnings.append(message)
  



    





