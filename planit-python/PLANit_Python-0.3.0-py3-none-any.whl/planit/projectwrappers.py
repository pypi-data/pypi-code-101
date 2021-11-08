import os

from py4j.java_gateway import get_field
from planit import BaseWrapper
from planit import GatewayUtils
from planit import GatewayState
from planit import OutputType
from planit import UnitType
from planit import PathIdType
from planit import OutputProperty
from planit import PhysicalCost
from planit import VirtualCost
from planit import Smoothing
from _decimal import Decimal
from numpy import string_

class AssignmentWrapper(BaseWrapper):
    """ Wrapper around the Java traffic assignment builder class instance
    """
    
    def __init__(self, java_counterpart, network_instance):
        super().__init__(java_counterpart)
        self._output_configuration = OutputConfigurationWrapper(self.get_output_configuration()) # collect the output configuration from Java
        self._gap_function_instance = GapFunctionWrapper(self.get_gap_function()) # collect the gap function from Java
        self._network_instance = network_instance
        self._physical_cost_instance = BPRCostWrapper(self.get_physical_cost(), self._network_instance) 
        self._virtual_cost_instance = VirtualCostWrapper(self.get_virtual_cost()) 
        self._smoothing_instance = SmoothingWrapper(self.get_smoothing())    
        
        # initialize in case they have defaults available
        #=======================================================================
        # self._link_output_type_configuration = LinkOutputTypeConfigurationWrapper(self._output_configuration.get_output_type_configuration(self.__create_java_output_type(OutputType.LINK)))
        # self._origin_destination_output_type_configuration = OriginDestinationOutputTypeConfigurationWrapper(self._output_configuration.get_output_type_configuration(self.__create_java_output_type(OutputType.OD)))   
        # self._path_output_type_configuration = PathOutputTypeConfigurationWrapper(self._output_configuration.get_output_type_configuration(self.__create_java_output_type(OutputType.PATH)))
        #=======================================================================
        
        for output_type in OutputType:
            output_type_instance = self.__create_java_output_type(output_type)
            if self.is_output_type_active(output_type_instance):
                if output_type.value == "LINK":
                    self._link_output_type_configuration = LinkOutputTypeConfigurationWrapper(self._java_counterpart.activateOutput(output_type_instance))
                elif output_type.value == "OD":
                    self._origin_destination_output_type_configuration = OriginDestinationOutputTypeConfigurationWrapper(self._java_counterpart.activateOutput(output_type_instance))
                elif output_type.value == 'PATH':
                    self._path_output_type_configuration = PathOutputTypeConfigurationWrapper(self._java_counterpart.activateOutput(output_type_instance))
        
        
        
    def __create_java_output_type(self, output_type):
        """ create an output type enum suitable to pass to java 
        """   
        return GatewayState.python_2_java_gateway.entry_point.createEnum(output_type.java_class_name(), output_type.value)
    
    def set(self, assignment_component):
        """ Configure an assignment component on this assignment instance. Note that all these go via the traffic assignment builder in Java
            although we hide that on the Python side to not over-complicate things for the average user. We accept PhysicalCost, VirtualCost,
            Smoothing, and GapFunction choices at this point
        """    
        
        if isinstance(assignment_component, PhysicalCost):
            if (assignment_component == PhysicalCost.BPR):
                self._physical_cost_instance = BPRCostWrapper(self.create_and_register_physical_cost(assignment_component.value), self._network_instance)
            elif (assignment_component == PhysicalCost.FREEFLOW):
                self._physical_cost_instance = FreeFlowCostWrapper(self.create_and_register_physical_cost(assignment_component.value)) 
            else:
                raise Exception('Unrecognized link cost function ' + assignment_component.type + ' cannot be set on assignment instance')
        elif isinstance(assignment_component, VirtualCost):
            self._virtual_cost_instance = VirtualCostWrapper(self.create_and_register_virtual_cost(assignment_component.value))
        elif isinstance(assignment_component, Smoothing):
            self._smoothing_instance = SmoothingWrapper(self.create_and_register_smoothing(assignment_component.value))
        elif isinstance(assignment_component, GapFunction):
            self._gap_function_instance = GapFunctionWrapper(self.create_and_register_gap_function(assignment_component.value))            
        else:
            raise Exception('Unrecognized component ' + assignment_component.type + ' cannot be set on assignment instance')
         
    def activate_output(self, output_type : OutputType):
        """ Activate different output types on the assignment. 
            Pass on to Java not as an Enum as Py4J does not seem to properly handle this at this stage
            instead we pass on the enum string which on the Java side is converted into the proper enum instead           
            :param output_type Python enum of available output types
        """ 
        # collect an enum instance by collecting the <package>.<class_name> string from the Output type enum
        output_type_instance = self.__create_java_output_type(output_type)
        if not self.is_output_type_active(output_type_instance):
            if output_type.value == "LINK":
                self._link_output_type_configuration = LinkOutputTypeConfigurationWrapper(self._java_counterpart.activateOutput(output_type_instance))
            elif output_type.value == "OD":
                self._origin_destination_output_type_configuration = OriginDestinationOutputTypeConfigurationWrapper(self._java_counterpart.activateOutput(output_type_instance))
            elif output_type.value == 'PATH':
                self._path_output_type_configuration = PathOutputTypeConfigurationWrapper(self._java_counterpart.activateOutput(output_type_instance))
            else:
                raise ValueError("Attempted to activate unknown output type " + output_type.value)     
    
    def deactivate_output(self, output_type: OutputType):   
        """Deactivate specified output type on the assignment
        :param output_type Output type to be deactivated
        """ 
        output_type_instance = self.__create_java_output_type(output_type)
        if self.is_output_type_active(output_type_instance):
            if output_type.value == "LINK":
                self._java_counterpart.deactivateOutput(output_type_instance)
            elif output_type.value == "OD":
                self._java_counterpart.deactivateOutput(output_type_instance)
            elif output_type.value == 'PATH':
                self._java_counterpart.deactivateOutput(output_type_instance)
            else:
                raise ValueError("Attempted to de-activate unknown output type " + output_type.value)     
  
    @property
    def gap_function(self):
        """Access to current gap function
        """
        return self._gap_function_instance
    
    @property
    def link_configuration(self):
        """Access to current link output type configuration, if not activated, it is activated so it can be configured
        """
        self.activate_output(OutputType.LINK)
        return self._link_output_type_configuration
    
    @property
    def od_configuration(self):
        """Access to current origin-destination output type configuration, if not activated, it is activated so it can be configured
        """
        self.activate_output(OutputType.OD)
        return self._origin_destination_output_type_configuration
    
    @property
    def output_configuration(self):
        """Access to current output configuration
        """
        return self._output_configuration    
    
    @property
    def path_configuration(self):
        """Access to current path output type configuration, if not activated, it is activated so it can be configured
        """
        self.activate_output(OutputType.PATH)
        return self._path_output_type_configuration
           
    @property
    def physical_cost(self):
        """Access to the physical cost wrapper
        """
        return self._physical_cost_instance
    
    @property
    def smoothing(self):
        """Access to the smoothing wrapper
        """
        return self._smoothing_instance    
    
    @property
    def virtual_cost(self):
        """Access to the virtual cost wrapper
        """
        return self._virtual_cost_instance
        
class DemandsWrapper(BaseWrapper):
    """ Wrapper around the Java Demands class instance
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)    
        
class GapFunctionWrapper(BaseWrapper):
    """ Wrapper around the Java GapFunction class instance
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        self._stop_criterion = StopCriterionWrapper(self.get_stop_criterion())  # collect the stop criterion from Java
        
    @property
    def stop_criterion(self):
        return self._stop_criterion

class InitialCostWrapper(BaseWrapper):
    """ Wrapper around the Java initial cost class instance
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
    def get_time_period_costs(self, timePeriod):
        """ delegate to Java counterpart and wrap result in Python object
        """
        return InitialCostModesWrapper(self._java_counterpart.getTimePeriodCosts(timePeriod.java))
        
    def get_time_period_agnostic_costs(self):
        """ delegate to Java counterpart and wrap result in Python object
        """
        return InitialCostModesWrapper(self._java_counterpart.getTimePeriodAgnosticCosts())

class InitialCostModesWrapper(BaseWrapper):
    """ Wrapper around the Java InitialCostModes class instance which tracks initial costs across modes but without    
        any knowledge of what time period (if any) it belongs to
    """ 
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
class LinkSegmentWrapper(BaseWrapper):
    """ Wrapper around the Java LinkSegments class
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
class LinkSegmentsWrapper(BaseWrapper):
    """ Wrapper around the Java LinkSegments class
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
class LinkSegmentTypesWrapper(BaseWrapper):
    """ Wrapper around the Java LinkSegmentTypes class
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)        
        
class LinkSegmentExpectedResultsDtoWrapper(BaseWrapper):
    """ Wrapper around the Java Link Segment Expected Results DTO class instance
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)

class MacroscopicLinkSegmentWrapper(BaseWrapper):
    """ Wrapper around the MacroscopicLinkSegmentType class instance
    """
     
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)      
 
class MacroscopicLinkSegmentTypeWrapper(BaseWrapper):
    """ Wrapper around the MacroscopicLinkSegmentType class instance
    """
     
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)      
 
class MacroscopicNetworkWrapper(BaseWrapper):
    """ Wrapper around the Java physical network class instance
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
class MemoryOutputIteratorWrapper(BaseWrapper):
    """Wrapper class around MemoryOutputIterator class
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
       
class ModeWrapper(BaseWrapper):
    """ Wrapper around the Java mode class instance
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)

class ModesWrapper(BaseWrapper):
    """ Wrapper around the Java modes class instance
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
            
class OutputConfigurationWrapper(BaseWrapper):
    """ Wrapper around the Java output configuration class instance
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
 
class OutputFormatterWrapper(BaseWrapper):
    """ Wrapper around the Java OutputFormatter wrapper class instance
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
class UnitsWrapper(BaseWrapper):
    """ Wrapper around the Java OutputFormatter wrapper class instance
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)        

class OutputTypeConfigurationWrapper(BaseWrapper): 
    """ Wrapper around the Java link output type configuration class instance
    """
     
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
    def __create_java_unit_type(self, unit_type: UnitType):
        """ create a unit type enum suitable to pass to java 
        """   
        return GatewayState.python_2_java_gateway.entry_point.createEnum(unit_type.java_class_name(), unit_type.value)
    
    def __create_java_unit_types(self, unit_types):
        """ create a java unit type array instance based on the given type enum suitable to pass to java
        :param unit_types list of Python UnitTypes
        :return Java array of java UnitTypes 
        """              
        _unit_type_class = GatewayState.python_2_java_gateway.jvm.org.goplanit.utils.unit.UnitType
        return GatewayUtils.to_java_array(_unit_type_class,[self.__create_java_unit_type(unit_type) for unit_type in unit_types])     
        
    def __create_java_unit(self, unit_type: UnitType):
        """ create a java unit instance based on the given type enum suitable to pass to java 
        """           
        return GatewayState.python_2_java_gateway.jvm.org.goplanit.utils.unit.Unit.of(self.__create_java_unit_type(unit_type))
    
    def __create_java_unit(self, numerator_unit_types, denominator_unit_types):
        """ create a java unit instance based on the given numerator and denominator types in Python list form
            :param output_property tp change units for
            :param numerator_unit_types list of python unit types 
            :return java unit instance
        """           
        java_numerator_unit_types = self.__create_java_unit_types(numerator_unit_types)
        java_denominator_unit_types = self.__create_java_unit_types(denominator_unit_types)
        return GatewayState.python_2_java_gateway.jvm.org.goplanit.utils.unit.Unit.of(java_numerator_unit_types, java_denominator_unit_types)            
        
    def __create_java_output_property(self, output_property : OutputProperty):
        """ create an output type enum suitable to pass to java 
        """   
        return GatewayState.python_2_java_gateway.entry_point.createEnum(output_property.java_class_name(), output_property.value)                  
        
    def add(self, output_property : OutputProperty):
        """Add an output type property to the current output type configuration
        """
        self._java_counterpart.addProperty(self.__create_java_output_property(output_property))
        
    def remove(self, output_property : OutputProperty):
        """Remove an output type property from the current output type configuration
        """
        return self._java_counterpart.removeProperty(self.__create_java_output_property(output_property))
        
    def remove_all_properties(self):
        """Remove all output properties currently registered
        """
        self._java_counterpart.removeAllProperties()
        
    def override_output_property_units(self, output_property : OutputProperty, unit_type : UnitType):
        """Change the units of the output property, where the property is a single unit
        """
        self._java_counterpart.overrideOutputPropertyUnits(self.__create_java_output_property(output_property), self.__create_java_unit(unit_type))
        
    def override_output_property_units(self, output_property : OutputProperty, numerator_unit_types, denominator_unit_types):
        """Change the units of the output property, where the property comprises more than one unit, e.g., km/h. Provide
            the desired units in the format of all numerator units as an array as the first argument and the denominator units
            as the second argument, also in array form
            :param output_property tp change units for
            :param numerator_unit_types list of python unit types
            :param denominator_unit_types list of python unit types
        """
        _java_unit_instance = self.__create_java_unit(numerator_unit_types, denominator_unit_types)
        self._java_counterpart.overrideOutputPropertyUnits(self.__create_java_output_property(output_property), _java_unit_instance)
        
class PhysicalCostWrapper(BaseWrapper):
    """ Wrapper around the Java physical cost class instance
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
  
class PlanItInputBuilderWrapper(BaseWrapper):
    """ Wrapper around the Java InputBuilderListener class instance
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)    
  
class SmoothingWrapper(BaseWrapper):
    """ Wrapper around the Java Smoothing class instance
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
class StopCriterionWrapper(BaseWrapper):
    """ Wrapper around the Java StopCriterion class instance
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
    
class TimePeriodWrapper(BaseWrapper):
    """ Wrapper around the Java time period class instance
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)

class TimePeriodsWrapper(BaseWrapper):
    """ Wrapper around the Java time periods class instance
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
class TransportLayersWrapper(BaseWrapper):
    """ Wrapper around the Java TransportLayers class instance
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)

class VirtualCostWrapper(BaseWrapper):
    """ Wrapper around the Java assignment class instance
    """    
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
             
class ZoningWrapper(BaseWrapper):
    """ Wrapper around the Java Zoning class instance
    """    
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
##########################################################
# Double derived wrappers
##########################################################
        
class BPRCostWrapper(PhysicalCostWrapper):
    """Wrapper around the BPRLinkTravelTimeCost instance
    """
    
    def __init__(self, java_counterpart, network_instance):
        super().__init__(java_counterpart)
        self._network_instance = network_instance
        modes_counterpart = self._network_instance.get_modes()
        self._modes_instance = ModesWrapper(modes_counterpart)
        
        layers_counterpart = network_instance.getTransportLayers()
        self._layers_instance = TransportLayersWrapper(layers_counterpart)        
        
        
    def set_default_parameters(self, alpha: float, beta: float, mode_xml_id:str =None, link_segment_type_xml_id:str =None):
        """Set the default BPR functions parameters 
        :param alpha value of alpha parameter
        :param beta value of beta parameter
        :param mode_xml_id if included, default parameters only apply to this mode
        :param link_segment_type_xml_id if included, default parameters apply to this link segment type and mode
        """
        if (mode_xml_id == None):
            self._java_counterpart.setDefaultParameters(alpha, beta)
        else:
            mode_counterpart = self._modes_instance.get_by_xml_id(mode_xml_id)
            if (link_segment_type_xml_id == None):
                self._java_counterpart.setDefaultParameters(mode_counterpart, alpha, beta)
            else:
                layer_counterpart = self._layers_instance.get(mode_counterpart)
                # cannot use field "linkSegmentTypes" for some reason, likely because layer_counterpart is a InfrastructureLayer to py4j and it cannot access field of 
                # derived type, hence we must call method for it to find the derived implementation
                link_segment_types_counterpart = layer_counterpart.getLinkSegmentTypes()
                link_segment_types_instance = LinkSegmentTypesWrapper(link_segment_types_counterpart)
                
                link_segment_type_counterpart = link_segment_types_instance.get_by_xml_id(link_segment_type_xml_id)
                self.setDefaultParameters(link_segment_type_counterpart, mode_counterpart, alpha, beta)
                
    def set_parameters(self, alpha: float, beta:float, mode_xml_id: str, link_segment_xml_id: str):
        """Set the default BPR functions parameters 
        :param alpha value of alpha parameter
        :param beta value of beta parameter
        :param mode_xml_id, parameters only apply to this mode
        :param link_segment_xml_id, parameters apply to this link segment 
        """        
        mode_counterpart = self._modes_instance.get_by_xml_id(mode_xml_id)
        layer_counterpart = self._layers_instance.get(mode_counterpart)
        link_segments_counterpart = layer_counterpart.getLinkSegments()
        link_segments_instance = LinkSegmentsWrapper(link_segments_counterpart)
        
        link_segment_counterpart = link_segments_instance.get_by_xml_id(link_segment_xml_id)        
        self._java_counterpart.setParameters(link_segment_counterpart, mode_counterpart, alpha, beta)  
        
class FreeFlowCostWrapper(PhysicalCostWrapper):
    """Wrapper around the FreeFlowLinkTravelTimeCost instance
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
class MemoryOutputFormatterWrapper(OutputFormatterWrapper):
    """ Wrapper around the Java PlanItOutputFormatter class instance
    """
    
    def __init__(self, java_counterpart, demands_instance, network_instance):
        """
        :param self this object
        :param java_counterpart Java counterpart for MemoryOutputFormatter object
        :param project_instance the instance of the project being run
        """
        super().__init__(java_counterpart)
        self._demands_instance = demands_instance
        self._network_instance = network_instance
                   
    def iterator(self, mode_xml_id: str, time_period_xml_id: str, no_iterations: int, output_type: OutputType):
        """Return the  wrapper for MemoryOutputIterator object for this MemoryOutputFormatter
        :param mode_xml_id the external Id of the current mode
        :param time_period_xml_id the external Id of the current time period
        :param no_iterations the iteration the output iterator applies to
        :param output_type the output type for the current output
        :return the wrapper for the memory output iterator
        """
        time_periods_counterpart = self._demands_instance.field("timePeriods")
        time_periods = TimePeriodsWrapper(time_periods_counterpart)
        time_period_counterpart = time_periods.get_by_xml_id(time_period_xml_id);
        time_period = TimePeriodWrapper(time_period_counterpart)        
        modes_counterpart = self._network_instance.get_modes()
        modes = ModesWrapper(modes_counterpart)
        mode_counterpart = modes.get_by_xml_id(mode_xml_id)
        mode = ModeWrapper(mode_counterpart)       
        output_type_instance = GatewayState.python_2_java_gateway.entry_point.createEnum(output_type.java_class_name(), output_type.value)
        memory_output_iterator_counterpart = self._java_counterpart.getIterator(mode.java, time_period.java, no_iterations, output_type_instance)
        memory_output_iterator = MemoryOutputIteratorWrapper(memory_output_iterator_counterpart)
        return memory_output_iterator
   
    def get_position_of_output_value_property(self, output_type, output_property):
        """Returns the position in the results array of the specified output value property
        :param output_type the output type for the current output
        :param output_property the specified output value property
        :result the position in the results array of the specified property
        """
        output_type_instance = GatewayState.python_2_java_gateway.entry_point.createEnum(output_type.java_class_name(), output_type.value)
        output_property_instance = GatewayState.python_2_java_gateway.entry_point.createEnum(output_property.java_class_name(), output_property.value)
        position = self._java_counterpart.getPositionOfOutputValueProperty(output_type_instance, output_property_instance)
        return position
    
    def get_position_of_output_key_property(self, output_type, output_property):
        """Returns the position in the results array of the specified output key property
          :param output_type the output type for the current output
          :param output_property the specified output property
          :result the position in the results array of the specified key property
        """
        output_type_instance = GatewayState.python_2_java_gateway.entry_point.createEnum(output_type.java_class_name(), output_type.value)
        output_property_instance = GatewayState.python_2_java_gateway.entry_point.createEnum(output_property.java_class_name(), output_property.value)
        position = self._java_counterpart.getPositionOfOutputKeyProperty(output_type_instance, output_property_instance)
        return position
                   
class PlanItOutputFormatterWrapper(OutputFormatterWrapper):
    """ Wrapper around the Java PlanItOutputFormatter class instance
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        # Initialize the output project path to the current run directory
        # Modellers may overwrite this default later
        project_path = os.getcwd()
        self.set_output_directory(project_path)        
              
class LinkOutputTypeConfigurationWrapper(OutputTypeConfigurationWrapper):
    """ Wrapper around the Java link output type configuration class instance
    """
     
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
       
class OriginDestinationOutputTypeConfigurationWrapper(OutputTypeConfigurationWrapper):
    """ Wrapper around the Java origin-destination output type configuration class instance
    """
     
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)

    def activate(self, od_skim_sub_output_type):
        """Activate an OD skim output type
        """
        od_skim_sub_output_type_instance = GatewayState.python_2_java_gateway.entry_point.createEnum(od_skim_sub_output_type.java_class_name(), od_skim_sub_output_type.value)
        self._java_counterpart.activateOdSkimOutputType(od_skim_sub_output_type_instance)
 
    def deactivate(self, od_skim_sub_output_type):
        """Deactivate an OD skim output type
        """
        od_skim_sub_output_type_instance = GatewayState.python_2_java_gateway.entry_point.createEnum(od_skim_sub_output_type.java_class_name(), od_skim_sub_output_type.value)
        self._java_counterpart.deactivateOdSkimOutputType(od_skim_sub_output_type_instance)         
        
class PathOutputTypeConfigurationWrapper(OutputTypeConfigurationWrapper):
    """ Wrapper around the Java path output type configuration class instance
    """
     
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
    def set_path_id_type(self,  path_id_type : PathIdType):
        path_id_type_instance = GatewayState.python_2_java_gateway.entry_point.createEnum(path_id_type.java_class_name(), path_id_type.value)
        self._java_counterpart.setPathIdentificationType(path_id_type_instance)
        