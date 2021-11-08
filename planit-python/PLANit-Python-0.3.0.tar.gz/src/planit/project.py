import os
from planit import BaseWrapper 
from planit import MacroscopicNetworkWrapper 
from planit import DemandsWrapper
from planit import AssignmentWrapper
from planit import ZoningWrapper
from planit import PlanItOutputFormatterWrapper
from planit import MemoryOutputFormatterWrapper
from planit import TrafficAssignment
from planit import OutputFormatter
from planit import InitialCostWrapper
from planit import TimePeriodWrapper
from planit import InitialCost
from planit import GatewayState

class PlanitProject ():
    """ The Python equivalent of a PlanitsimpleProject used to conduct traffic assignment
        with a single network, zoning, demand combination that is parsed upon instantiation 
    """
    
    def __init__(self, project_path=None):
        """Constructor of PLApython project wrapper which acts as an interface to the underlying PLANit Java code
        :param project_path the path location of the XML input file(s) to be used by PLANitIO
        """
        self._project_instance = None
        self._assignment_instance = None
        self._input_builder_instance = None
        self._network_instance = None
        self._zoning_instance = None
        self._demands_instance = None                
        self._io_output_formatter_instance = None
        self._memory_output_formatter_instance = None
        self._initial_cost_instance = None
        
        self._activate_planitio_output_formatter = False
        self._activate_memory_output_formatter = False
        
        # create simple project and parse the network, zoning, and demands for it + default configuration setup
        self.__initialize_project__(project_path)                          
    
    def __initialize_project__(self, project_path):
        """Initialize the project using the input file in the directory specified by project_path
        """
        if project_path == None:
            project_path = os.getcwd()
        self._project_instance = BaseWrapper(GatewayState.python_2_java_gateway.entry_point.initialiseSimpleProject(project_path))
    
        # The one macroscopic network, zoning, demand is created and populated and wrapped in a Python object
        # (Note1: to access public members in Java, we must collect it via the field method in the wrapper)
        # (Note2: since we only have a single network, demand, zoning, we do not have a wrapper for the fields, so we must access the methods directly
        self._network_instance = MacroscopicNetworkWrapper(self._project_instance.getNetwork())
        # the one zoning is created and populated
        self._zoning_instance = ZoningWrapper(self._project_instance.field("zonings").getFirst())
        # the one demands is created and populated
        self._demands_instance = DemandsWrapper(self._project_instance.field("demands").getFirst())      
        self._initial_cost_instance = InitialCost()
        
        #PLANIT_IO output formatter is activated by default, MemoryOutputFormatter is off by default
        self._io_output_formatter_instance = PlanItOutputFormatterWrapper(self._project_instance.getDefaultOutputFormatter())
        self._activate_planitio_output_formatter = True
    
    def __getattr__(self, name):
        """ all methods invoked on the PLANit Java project wrapper as passed on to it without the user seeing the actual gateway. This is to be
        replaced by a more intricate interface which exposes only the properties users are allowed to configure to create a PLANit instance
        """        
        def method(*args): #collects the arguments of the function 'name' (wrapper function within getattr)                
            if GatewayState.gateway_is_running:
                java_name = GatewayUtils.to_camelcase(name)
                # pass all calls on to the underlying PLANit project java class which is obtained via the entry_point.getProject call
                return getattr(GatewayState.planit_project, java_name)(*args) # invoke without arguments
            else:
                raise Exception('PLANit java interface not available')      
        return method
    
    def __register_initial_costs__(self):   
        """Register the initial costs on the assignment with 1:1 mapping between parsed time periods and assignment time periods
        """
        time_periods_xml_id_set = self._initial_cost_instance.get_time_periods_xml_id_set()
        
        if self._initial_cost_instance.get_default_initial_cost_file_location() != None:
            default_initial_cost_counterpart = self._project_instance.create_and_register_initial_link_segment_cost(self._network_instance.java, self._initial_cost_instance.get_default_initial_cost_file_location())
            default_initial_cost_wrapper = InitialCostWrapper(default_initial_cost_counterpart)
            self._assignment_instance.register_initial_link_segment_cost(default_initial_cost_wrapper.java)
            
        if len(time_periods_xml_id_set) > 0:            
            time_period_counterparts = self._demands_instance.field("timePeriods").asSortedSetByStartTime()
            for time_period_counterpart in time_period_counterparts:
                time_period = TimePeriodWrapper(time_period_counterpart)
                time_period_xml_id = time_period.get_xml_id()
                if (time_period_xml_id in time_periods_xml_id_set):
                    initial_cost_file_location = self._initial_cost_instance.get_initial_cost_file_location_by_time_period_xml_id(time_period_xml_id)
                    initial_cost_counterpart = self._project_instance.create_and_register_initial_link_segment_cost(self._network_instance.java, initial_cost_file_location, time_period_counterpart)
                    initial_cost_wrapper = InitialCostWrapper(initial_cost_counterpart)
                    self._assignment_instance.register_initial_link_segment_cost(time_period.java, initial_cost_wrapper.get_time_period_costs(time_period).java)       
                            
    def set(self, assignment_component):
        """Set the traffic assignment component
        :param assignment_component the  assignment component
        """
        if isinstance(assignment_component, TrafficAssignment):
            assignment_counterpart = self._project_instance.create_and_register_traffic_assignment(assignment_component.value)
            self._assignment_instance = AssignmentWrapper(assignment_counterpart, self._network_instance)
            
    def activate(self, formatter_component):
        """Activate an output formatter
        :param formatter_component the formatter being set up
        """
        if formatter_component == OutputFormatter.PLANIT_IO:
            if (not self._activate_planitio_output_formatter):
                self._activate_planitio_output_formatter = True
                io_output_formatter_counterpart = self._project_instance.create_and_register_output_formatter(formatter_component.value)
                io_output_formatter = PlanItOutputFormatterWrapper(io_output_formatter_counterpart)
                self._io_output_formatter_instance = io_output_formatter
                        
        elif formatter_component == OutputFormatter.MEMORY:
            if (not self._activate_memory_output_formatter):
                self._activate_memory_output_formatter = True
                memory_output_formatter_counterpart =  self._project_instance.create_and_register_output_formatter(formatter_component.value)
                memory_output_formatter = MemoryOutputFormatterWrapper(memory_output_formatter_counterpart, self._demands_instance, self._network_instance)
                self._memory_output_formatter_instance = memory_output_formatter            
            
    def deactivate(self, formatter_component):
        """Deactivate an output formatter which has previously been activated
        :param formatter_component the formatter which has previously been activated
        """
        if formatter_component == OutputFormatter.PLANIT_IO:
            self._activate_planitio_output_formatter = False
            self._io_output_formatter_instance = None
        elif formatter_component == OutputFormatter.MEMORY:
            self._activate_memory_output_formatter = False
            self._memory_output_formatter_instance = None
        
    def run(self):
        """Run the traffic assignment.  Register any output formatters which have been set up
        """
        if (self._assignment_instance == None):
            raise Exception("Called plan_it.run() with no Traffic Assignment set")
        if (self._activate_planitio_output_formatter):
            self._assignment_instance.register_output_formatter(self._io_output_formatter_instance.java); 
        if (self._activate_memory_output_formatter):      
            self._assignment_instance.register_output_formatter(self._memory_output_formatter_instance.java)
        self.__register_initial_costs__()
        self._project_instance.execute_all_traffic_assignments()   
                                        
    @property
    def assignment(self):
        """ access to the assignment builder 
        """
        if (self._assignment_instance == None):
            raise Exception("assignment instance not yet available, configure via .set() method")
        return self._assignment_instance  
    
    @property
    def network(self):
        """access to the network
        """
        return self._network_instance
    
    @property
    def demands(self):
        """access to the demands
        """
        return self._demands_instance
    
    @property
    def output(self):
        """access to PLANitIO output formatter
        """
        return self._io_output_formatter_instance
    
    @property
    def memory(self):
        """access to memory output formatter
        """
        return self._memory_output_formatter_instance
    
    @property
    def initial_cost(self):
        """access to initial cost
        """
        return self._initial_cost_instance