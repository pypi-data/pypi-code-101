import os

from py4j.java_gateway import get_field
from planit import GatewayUtils
from planit import GatewayState
from planit import BaseWrapper
from planit import OsmEntityType
from _decimal import Decimal
from numpy import string_

    
class ConverterWrapper(BaseWrapper):
    """ Wrapper around a Java Converter class instance which in turn has more specific implementations for which
    we also provide wrapper classes, e.g. Network, Zoning, Intermodal etc.
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart) 
    
            
class ReaderSettingsWrapper(BaseWrapper):
    """ Wrapper around settings for a reader used by converter
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
class ReaderWrapper(BaseWrapper):
    """ Wrapper around a Java Reader class instance which in turn has more specific implementations for which
    we also provide wrapper classes, e.g. NetworkReader, ZoningReader, IntermodalReader etc.
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart) 
        
        # wrap the java settings that we expose as a property for this reader in a "ReaderSettingsWrapper"
        # this way we have a general wrapper for all settings instances exposed to the user, while not having to create
        # separate wrapper classes for each specific implementation (as long as the settings themselves do not expose any other
        # classes that need to be wrapper this will work
        self._settings = ReaderSettingsWrapper(self.get_settings())
        
    @property
    def settings(self) -> ReaderSettingsWrapper:
        """ access to the settings of this reader wrapper 
        """
        return self._settings                                     
             
class WriterSettingsWrapper(BaseWrapper):
    """ Wrapper around settings for a reader used by converter
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)      
        
class WriterWrapper(BaseWrapper):
    """ Wrapper around a Java Writer class instance which in turn has more specific implementations for which
    we also provide wrapper classes, e.g. NetworkWriter, ZoningWriter, IntermodalWriter etc.
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        # wrap the java settings that we expose as a property for this writer in a "WriterSettingsWrapper"
        # this way we have a general wrapper for all settings instances exposed to the user, while not having to create
        # separate wrapper classes for each specific implementation (as long as the settings themselves do not expose any other
        # classes that need to be wrapper this will work
        self._settings = WriterSettingsWrapper(self.get_settings())
        
    @property
    def settings(self) -> WriterSettingsWrapper:
        """ access to the settings of this writer wrapper 
        """
        return self._settings                               
        
##########################################################
# Double derived wrappers
##########################################################
        
        
class IntermodalConverterWrapper(ConverterWrapper):
    """ Wrapper around the Java IntermodalConverter class instance
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)  
        
class IntermodalReaderWrapper(ReaderWrapper):
    """ Wrapper around the Java IntermodalReader class instance, derived implementation are more specific, e.g. OsmIntermodalReaderWrapper
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
            
class IntermodalWriterWrapper(WriterWrapper):
    """ Wrapper around the Java IntermodalWriter class instance, derived implementations are more specific, e.g. MatsimIntermodalWriterWrapper
    """  
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)          
   
class NetworkConverterWrapper(ConverterWrapper):
    """ Wrapper around the Java NetworkConverter class instance
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)    
    
class NetworkReaderWrapper(ReaderWrapper):
    """ Wrapper around the Java NetworkReader class instance, derived implementation are more specific, e.g. OsmNetworkReaderWrapper
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
    
class NetworkWriterWrapper(WriterWrapper):
    """ Wrapper around the Java NetworkWriter class instance, derived implementations are more specific, e.g. MatsimNetworkWriterWrapper
    """  
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)            
                
        
##########################################################
# Triple derived wrappers
##########################################################

class MatsimIntermodalWriterSettingsWrapper(WriterSettingsWrapper):
    """ Wrapper around settings for an intermodal Matsim writer used by converter
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
        # Matsim intermodal writer settings allow access to network and zoning settings component
        # which in turns are settings 
        self._network_settings = WriterSettingsWrapper(self.get_network_settings())
        self._zoning_settings = WriterSettingsWrapper(self.get_zoning_settings())
    
    @property
    def network_settings(self):
        return self._network_settings
    
    @property
    def zoning_settings(self):
        return self._zoning_settings

class MatsimIntermodalWriterWrapper(IntermodalWriterWrapper):
    """ Wrapper around the Java PlanitMatsimNetworkWriter class
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
         # replace regular reader settings by Matsim intermodal reader settings
        self._settings = MatsimIntermodalWriterSettingsWrapper(self._settings.java)       

class MatsimNetworkWriterWrapper(NetworkWriterWrapper):
    """ Wrapper around the Java PlanitMatsimNetworkWriter class
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
class OsmPublicTransportSettingsWrapper(ReaderSettingsWrapper):
    """ Wrapper around pt settings for an OSM intermodal reader used by converter. Wrapper is needed to deal with the methods
    that require enum parameters
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
    def __create_java_entity_type(self,  osm_entity_type:OsmEntityType):
        """ convert Python osm entity type to Java entity type
        :param osm_entity_type to convert
        :return java counterpart 
        """
        return GatewayState.python_2_java_gateway.entry_point.createEnum(osm_entity_type.java_class_name(),osm_entity_type.value) 
        
    def overwrite_stop_location_waiting_area(self, osm_stop_location_id, osm_entity_type:OsmEntityType, osm_waiting_area_id):
        self.overwriteStopLocationWaitingArea(osm_stop_location_id, self.__create_java_entity_type(osm_entity_type), osm_waiting_area_id)
        
    def overwrite_waiting_area_nominated_osm_way_for_stop_location(self, osm_waiting_area_id, osm_entity_type:OsmEntityType, osm_way_id):
        self.overwriteWaitingAreaNominatedOsmWayForStopLocation(osm_waiting_area_id, self.__create_java_entity_type(osm_entity_type), osm_way_id)
        
class OsmIntermodalReaderSettingsWrapper(ReaderSettingsWrapper):
    """ Wrapper around settings for an OSM intermodal reader used by converter
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
        # OSM intermodal reader settings allow access to network and pt settings component
        # which in turns are settings 
        self._network_settings = OsmNetworkReaderSettingsWrapper(self.getNetworkSettings())
        self._pt_settings = OsmPublicTransportSettingsWrapper(self.getPublicTransportSettings())
    
    @property
    def network_settings(self):
        return self._network_settings
    
    @property
    def pt_settings(self):
        return self._pt_settings         
        
class OsmIntermodalReaderWrapper(IntermodalReaderWrapper):
    """ Wrapper around the Java PlanitOsmIntermodalReader class
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)     
        
         # replace regular reader settings by planit intermodal reader settings
        self._settings = OsmIntermodalReaderSettingsWrapper(self._settings.java)
                
class OsmNetworkReaderSettingsWrapper(ReaderSettingsWrapper):
    """ Wrapper around settings for an OSM network reader used by converter
    to keep things simpler compared to Java side, we always provide access to highway and
    railway settings. In case the respective parsers are deactivated, it is assumed the user
    wants them activated since it is unlikely they would want to change settings for them otherwise,
    so we automatically activate the parser when the property is accessed and update the jave counterpart
    in the wrapper
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
        # OSM network reader settings allow access to network and pt settings component
        # which in turn are settings.  
        self._highway_settings = ReaderSettingsWrapper(self.get_highway_settings())
        self._railway_settings = ReaderSettingsWrapper(self.get_railway_settings())
        
        # lane configuration is also wrapped in a reader settings wrapper and acessed via property
        self._lane_configuration = ReaderSettingsWrapper(self.get_lane_configuration())
    
    @property
    def highway_settings(self):
        if not self.is_highway_parser_active() or not self._highway_settings._java_counterpart:
            self.activate_highway_parser(True)
            self._highway_settings = ReaderSettingsWrapper(self.get_highway_settings())
        return self._highway_settings
    
    @property
    def railway_settings(self):
        if not self.is_railway_parser_active() or not self._railway_settings._java_counterpart:
            self.activate_railway_parser(True)
            self._railway_settings = ReaderSettingsWrapper(self.get_railway_settings())
        return self._railway_settings     
    
    @property
    def lane_configuration(self):
        return self._lane_configuration 
    
    def set_keep_osm_ways_outside_bounding_box(self, osm_way_ids):
        """ delegate to equivalent Java method, but because we only expose the option to set a bounding box
        rather than a bounding polygon, we renamed the method on the Python side to avoid confusion
        """
        self.set_keep_osm_ways_outside_bounding_polygon(osm_way_ids)     

class OsmNetworkReaderWrapper(NetworkReaderWrapper):
    """ Wrapper around the Java PlanitOsmNetworkReader class
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
        # OSM network reader settings allow access to highway and railway settings component
        # requiring a dedicated wrapper -> use this wrapper instead of generic settings wrapper
        self._settings = OsmNetworkReaderSettingsWrapper(self.settings.java)
        
class PlanitIntermodalReaderSettingsWrapper(ReaderSettingsWrapper):
    """ Wrapper around settings for a planit intermodal reader (native format) used by converter
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
        # planit intermodal reader settings allow access to network and zoning settings component
        # which in turns are settings 
        self._network_settings = ReaderSettingsWrapper(self.getNetworkSettings())
        self._zoning_settings = ReaderSettingsWrapper(self.getZoningSettings())
    
    @property
    def network_settings(self):
        return self._network_settings
    
    @property
    def zoning_settings(self):
        return self._zoning_settings 
        
class PlanitIntermodalReaderWrapper(IntermodalReaderWrapper):
    """ Wrapper around the Java native format based PlanitIntermodalReader class
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
        # replace regular reader settings by planit intermodal reader settings
        self._settings = PlanitIntermodalReaderSettingsWrapper(self._settings.java) 
               
class PlanitIntermodalWriterSettingsWrapper(WriterSettingsWrapper):
    """ Wrapper around settings for a intermodal planit writer (native format) used by converter
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
        # planit intermodal writer settings allow access to network and zoning settings component
        # which in turns are settings 
        self._network_settings = WriterSettingsWrapper(self.get_network_settings())
        self._zoning_settings = WriterSettingsWrapper(self.get_zoning_settings())
    
    @property
    def network_settings(self):
        return self._network_settings
    
    @property
    def zoning_settings(self):
        return self._zoning_settings
        
class PlanitIntermodalWriterWrapper(IntermodalWriterWrapper):
    """ Wrapper around the Java native format based PlanitIntermodalWriter class
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
         # replace regular writer settings by Planit intermodal reader settings
        self._settings = MatsimIntermodalWriterSettingsWrapper(self._settings.java)  
        
class PlanitNetworkReaderWrapper(NetworkReaderWrapper):
    """ Wrapper around the Java native format based PlanitNetworkReader class
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)
        
class PlanitNetworkWriterWrapper(NetworkWriterWrapper):
    """ Wrapper around the Java native format based PlanitNetworkWriter class
    """
    
    def __init__(self, java_counterpart):
        super().__init__(java_counterpart)