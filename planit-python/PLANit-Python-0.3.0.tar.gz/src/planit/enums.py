from enum import Enum

class ConverterType(Enum):
    """ Enum for the different converters that exist
    """
    NETWORK = "NetworkConverter"
    ZONING = "ZoningConverter"
    INTERMODAL = "IntermodalConverter"
    SERVICE_NETWORK = "ServiceNetworkConverter"
    ROUTED_SERVICES = "RoutedServicesConverter"
    
class GapFunction(Enum):
    """ Enum for the different gap functions that exist on supporting traffic assignments
    """
    LINK_BASED_RELATIVE = "org.goplanit.gap.LinkBasedRelativeGapFunction"
    NORM_BASED = "org.goplanit.gap.NormBasedGapFunction"     
    
class IntermodalReaderType(Enum):
    """ Enum for the different intermodal readers that are supported
    """
    OSM = "OsmIntermodalReader"
    PLANIT = "PlanitIntermodalReader"
    
class IntermodalWriterType(Enum):
    """ Enum for the different intermodal writers that are supported
    """
    MATSIM = "MatsimIntermodalWriter"
    PLANIT = "PlanitIntermodalWriter"
          
class Network(Enum):
    """ Enum for the different virtual costs the user can choose, they map to the Java equivalent class name for easy mapping
    """
    MACROSCOPIC = "org.goplanit.network.physical.macroscopic.MacroscopicNetwork"
    PHYSICAL = "org.goplanit.network.physical.PhysicalNetwork"
    VIRTUAL = "org.goplanit.network.virtual.VirtualNetwork"
    
class NetworkReaderType(Enum):
    """ Enum for the different network readers that exist compatible with a network converter
    """
    OSM = "OsmNetworkReader"
    PLANIT = "PlanitNetworkReader"
    
class ServiceNetworkReaderType(Enum):
    """ Enum for the different service network readers that exist compatible with a service network converter
    """
    PLANIT = "PlanitServiceNetworkReader"
    
class RoutedServicesReaderType(Enum):
    """ Enum for the different routed services readers that exist compatible with a routed services converter
    """
    PLANIT = "PlanitRoutedServicesReader"    
    
class NetworkWriterType(Enum):
    """ Enum for the different network writers that exist compatible with a network converter
    """
    MATSIM = "MatsimNetworkWriter"
    PLANIT = "PlanitNetworkWriter"
    
class OdSkimSubOutputType(Enum):
    
    NONE = "NONE"
    COST = "COST"

    def java_class_name(self) -> str:
        return "org.goplanit.output.enums.OdSkimSubOutputType"      
    
class OsmEntityType(Enum):
    """ Enum for the different OSM entities that the user can differentiate between in the OSM converters
    """
    NODE = "Node"
    WAY = "Way"
    RELATION = "Relation"

    def java_class_name(self) -> str:
        return "de.topobyte.osm4j.core.model.iface.EntityType"  
    
    
class OutputFormatter(Enum):
    """ Enum for the different output formatters the user can choose, they map to the Java equivalent class name for easy mapping
        Only the output formatters available in the PLANitIO project have been defined here
    """
    
    MEMORY = "org.goplanit.output.formatter.MemoryOutputFormatter"
    PLANIT_IO = "org.goplanit.io.output.formatter.PlanItOutputFormatter"
    
class OutputProperty(Enum):    
    """ Enum for the different output properties the user can configure in the output files 
        Equivalent of Java enumeration org.goplanit.output.property.OutputProperty
    """
    
    # alphabetical order by priority type (ID, INPUT, OUTPUT
    DESTINATION_ZONE_ID = "DESTINATION_ZONE_ID"                     # ID
    DESTINATION_ZONE_EXTERNAL_ID = "DESTINATION_ZONE_EXTERNAL_ID"   # ID
    DESTINATION_ZONE_XML_ID = "DESTINATION_ZONE_XML_ID"             # ID
    DOWNSTREAM_NODE_ID = "DOWNSTREAM_NODE_ID"                       # ID
    DOWNSTREAM_NODE_XML_ID = "DOWNSTREAM_NODE_XML_ID"               # ID
    DOWNSTREAM_NODE_EXTERNAL_ID = "DOWNSTREAM_NODE_EXTERNAL_ID"     # ID
    ITERATION_INDEX = "ITERATION_INDEX"                             # ID
    LINK_SEGMENT_ID = "LINK_SEGMENT_ID"                             # ID
    LINK_SEGMENT_TYPE_ID = "LINK_SEGMENT_TYPE_ID"                   # ID
    LINK_SEGMENT_XML_ID = "LINK_SEGMENT_XML_ID"                     # ID
    LINK_SEGMENT_TYPE_XML_ID = "LINK_SEGMENT_TYPE_XML_ID"           # ID
    LINK_SEGMENT_EXTERNAL_ID = "LINK_SEGMENT_EXTERNAL_ID"           # ID
    MODE_ID = "MODE_ID"                                             # ID
    MODE_XML_ID = "MODE_XML_ID"                                     # ID
    MODE_EXTERNAL_ID = "MODE_EXTERNAL_ID"                           # ID
    ORIGIN_ZONE_ID = "ORIGIN_ZONE_ID"                               # ID
    ORIGIN_ZONE_XML_ID = "ORIGIN_ZONE_XML_ID"                       # ID
    ORIGIN_ZONE_EXTERNAL_ID = "ORIGIN_ZONE_EXTERNAL_ID"             # ID
    PATH_ID = "PATH_ID"                                             # ID
    RUN_ID = "RUN_ID"                                               # ID
    TIME_PERIOD_ID = "TIME_PERIOD_ID"                               # ID
    TIME_PERIOD_XML_ID = "TIME_PERIOD_XML_ID"                       # ID
    TIME_PERIOD_EXTERNAL_ID = "TIME_PERIOD_EXTERNAL_ID"             # ID
    UPSTREAM_NODE_ID = "UPSTREAM_NODE_ID"                           # ID
    UPSTREAM_NODE_XML_ID = "UPSTREAM_NODE_XML_ID"                   # ID
    UPSTREAM_NODE_EXTERNAL_ID = "UPSTREAM_NODE_EXTERNAL_ID"         # ID
    CAPACITY_PER_LANE = "CAPACITY_PER_LANE"                         # INPUT
    DOWNSTREAM_NODE_LOCATION = "DOWNSTREAM_NODE_LOCATION"           # INPUT
    LENGTH = "LENGTH"                                               # INPUT
    LINK_SEGMENT_TYPE_NAME = "LINK_SEGMENT_TYPE_NAME"               # INPUT    
    MAXIMUM_DENSITY = "MAXIMUM_DENSITY"       # INPUT
    MAXIMUM_SPEED = "MAXIMUM_SPEED"                                 # INPUT
    NUMBER_OF_LANES = "NUMBER_OF_LANES"                             # INPUT
    UPSTREAM_NODE_LOCATION = "UPSTREAM_NODE_LOCATION"               # INPUT        
    CALCULATED_SPEED = "CALCULATED_SPEED"                           # OUTPUT
    COST_TIMES_FLOW = "COST_TIMES_FLOW"                             # OUTPUT
    DENSITY = "DENSITY"                                             # OUTPUT        
    FLOW = "FLOW"                                                   # OUTPUT
    LINK_SEGMENT_COST = "LINK_SEGMENT_COST"                         # OUTPUT
    OD_COST = "OD_COST"                                             # OUTPUT
    TOTAL_COST_TO_END_NODE = "TOTAL_COST_TO_END_NODE"               # OUTPUT
    PATH_STRING = "PATH_STRING"                                     # OUTPUT
    VC_RATIO = "VC_RATIO"                                           # OUTPUT
        
    
    def java_class_name(self) -> str:
        return "org.goplanit.output.property.OutputPropertyType"     
    
class OutputType(Enum):
    """ Enum for the different output types the user can choose to activate, 
         Equivalent of Java enumeration org.goplanit.output.OutputType
    """
    LINK = "LINK"
    GENERAL = "GENERAL"
    SIMULATION = "SIMULATION"
    OD = "OD"
    PATH = "PATH"
    
    def java_class_name(self) -> str:
        return "org.goplanit.output.enums.OutputType"   
    
class PhysicalCost(Enum):
    """ Enum for the different physical costs the user can choose, they map to the Java equivalent class name for easy mapping
    """
    BPR = "org.goplanit.cost.physical.BPRLinkTravelTimeCost"
    FREEFLOW = "org.goplanit.cost.physical.FreeFlowLinkTravelTimeCost"

class PathIdType(Enum):

    LINK_SEGMENT_EXTERNAL_ID = "LINK_SEGMENT_EXTERNAL_ID"
    LINK_SEGMENT_XML_ID = "LINK_SEGMENT_XML_ID"
    LINK_SEGMENT_ID = "LINK_SEGMENT_ID"
    NODE_EXTERNAL_ID = "NODE_EXTERNAL_ID"
    NODE_XML_ID = "NODE_XML_ID"
    NODE_ID = "NODE_ID"

    def java_class_name(self) -> str:
        return "org.goplanit.output.enums.PathOutputIdentificationType"     
   
class Smoothing(Enum):
    """ Enum for the different smoothing options the user can choose, they map to the Java equivalent class name for easy mapping
    """
    MSA = "org.goplanit.sdinteraction.smoothing.MSASmoothing"

class TrafficAssignment(Enum):
    """ Enum for the different assignment the user can choose, they map to the Java equivalent class name for easy mapping
    """
    TRADITIONAL_STATIC = "org.goplanit.assignment.traditionalstatic.TraditionalStaticAssignment"
    SLTM = "org.goplanit.assignment.ltm.sltm.StaticLtm"
    ETLM = "org.goplanit.assignment.ltm.eltm.EventBasedLtm"
    
class UnitType(Enum):
    
    NONE = "NONE"
    VEH = "VEH"
    PCU = "PCU"
    KM = "KM"
    METER = "METER"
    HOUR = "HOUR"
    MINUTE = "MINUTE"
    SECOND = "SECOND"
    SRS = "SRS"
    
    def java_class_name(self) -> str:
        return "org.goplanit.utils.unit.UnitType"  

class VirtualCost(Enum):
    """ Enum for the different virtual costs the user can choose, they map to the Java equivalent class name for easy mapping
    """
    FIXED = "org.goplanit.cost.virtual.FixedConnectoidTravelTimeCost"
    SPEED = "org.goplanit.cost.virtual.SpeedConnectiodTravelTimeCost"
       
