from abc import ABCMeta, abstractmethod
from planit import ConverterType
from planit import GatewayState
from planit import ConverterWrapper
from planit import IntermodalReaderWrapper
from planit import IntermodalWriterWrapper
from planit import IntermodalConverterWrapper
from planit import IntermodalReaderType
from planit import IntermodalWriterType
from planit import MatsimIntermodalWriterWrapper
from planit import MatsimNetworkWriterWrapper
from planit import NetworkReaderType
from planit import NetworkWriterType
from planit import NetworkReaderWrapper
from planit import NetworkWriterWrapper
from planit import OsmNetworkReaderWrapper
from planit import OsmIntermodalReaderWrapper
from planit import PlanitIntermodalReaderWrapper
from planit import PlanitIntermodalWriterWrapper
from planit import PlanitNetworkReaderWrapper
from planit import PlanitNetworkWriterWrapper


class _ConverterBase (metaclass=ABCMeta):
    """ Base converter class on python side exposing the convert functionality
    """
               
    @abstractmethod
    def _create_java_converter(self, readerWrapper, writerWrapper): 
        """ create java converter based on reader and writer wrapper provided in derived class implementation 
        :param readerWrapper: to use
        :param writerWrapper: to use
        :return created java converter
        """
        pass 
    
    def convert(self, reader, writer ):
        """ each converter should be able to convert from a reader to a writer
        :param readerWrapper: to use
        :param writerWrapper: to use
        """
                
        # construct java converter and perform conversion
        self._create_java_converter(reader, writer).convert()
        

class NetworkConverter(_ConverterBase):
    """ Expose the options to create network reader and writers of supported types and perform conversion between them
    """
    
    def __init__(self):
        super().__init__()   
        
    def _create_java_converter(self, readerWrapper, writerWrapper):
        """ create java network converter with reader and writer wrapper provided
        :param readerWrapper: to use
        :param writerWrapper: to use
        :return created java network converter
        """
        return GatewayState.python_2_java_gateway.jvm.org.goplanit.converter.network.NetworkConverterFactory.create(readerWrapper.java, writerWrapper.java)
    
    #####################################
    #     READER FACTORY METHODS
    #####################################
   
        
    def __create_osm_network_reader(self, country: str) -> OsmNetworkReaderWrapper:
        java_network_reader = GatewayState.python_2_java_gateway.jvm.org.goplanit.osm.converter.network.OsmNetworkReaderFactory.create(country)
        return OsmNetworkReaderWrapper(java_network_reader)
    
    def __create_planit_network_reader(self) -> PlanitNetworkReaderWrapper:
        java_network_reader = GatewayState.python_2_java_gateway.jvm.org.goplanit.io.converter.network.PlanitNetworkReaderFactory.create()
        return PlanitNetworkReaderWrapper(java_network_reader)
        
    #####################################
    #     WRITER FACTORY METHODS
    #####################################
        
    def __create_matsim_network_writer(self) -> MatsimNetworkWriterWrapper:
        java_network_writer = GatewayState.python_2_java_gateway.jvm.org.goplanit.matsim.converter.MatsimNetworkWriterFactory.create()
        return MatsimNetworkWriterWrapper(java_network_writer)
        
    def __create_planit_network_writer(self) -> PlanitNetworkWriterWrapper:
        java_network_writer = GatewayState.python_2_java_gateway.jvm.org.goplanit.io.converter.network.PlanitNetworkWriterFactory.create()
        return PlanitNetworkWriterWrapper(java_network_writer)
    
        
    def create_reader(self, network_reader_type: NetworkReaderType, country:str = "Global") -> NetworkReaderWrapper:
        """ factory method to create a network reader compatible with this converter
        :param network_reader_type: the type of reader to create
        :param country: optional argument specifying the country of the source network. Used by some readers to initialise default settings. If absent
         but required it defaults to "Global", i.e., no country specific information is used in initialising defaults if applicable
        """
        if not isinstance(network_reader_type,NetworkReaderType) : raise Exception("network reader type provided is not of NetworkReaderType, unable to instantiate")
        
        if  network_reader_type == NetworkReaderType.OSM:
            # OSM requires country to initialise default settings
            return self.__create_osm_network_reader(country)
        elif network_reader_type == NetworkReaderType.PLANIT:
            # PLANit does not utilise country information
            return self.__create_planit_network_reader() 
        else:
            raise Exception("unsupported network reader type provided, unable to instantiate")
    
    def create_writer(self, network_writer_type: NetworkWriterType) -> NetworkWriterWrapper:
        """ factory method to create a network writer compatible with this converter
        :param network_writer_type: the type of writer to create
        """
        if not isinstance(network_writer_type,NetworkWriterType) : raise Exception("network writer type provided is not of NetworkWriterType, unable to instantiate")
        
        if  network_writer_type == NetworkWriterType.MATSIM:
            return self.__create_matsim_network_writer()
        elif network_writer_type == NetworkWriterType.PLANIT:
            return self.__create_planit_network_writer() 
        else:
            raise Exception("unsupported network writer type provided, unable to instantiate")    
        
class ZoningConverter(_ConverterBase):
    """ Expose the options to create zoning reader and writers of supported types and perform conversion between them
    """
    
    def __init__(self):
        super().__init__()
        
    #TODO
        
class IntermodalConverter(_ConverterBase):
    """ Expose the options to create intermodal reader and writers of supported types and perform conversion between them
    """
        
    def __init__(self):
        super().__init__()
        
    def _create_java_converter(self, readerWrapper, writerWrapper) -> IntermodalConverterWrapper:
        """ create java intermodal converter with reader and writer wrapper provided
        :param readerWrapper: to use
        :param writerWrapper: to use
        :return created java intermodal converter
        """
        return GatewayState.python_2_java_gateway.jvm.org.goplanit.converter.intermodal.IntermodalConverterFactory.create(readerWrapper.java, writerWrapper.java)        
        
   #####################################
    #     READER FACTORY METHODS
    #####################################
           
    def __create_osm_intermodal_reader(self, country: str) -> OsmIntermodalReaderWrapper:
        java_intermodal_reader = GatewayState.python_2_java_gateway.jvm.org.goplanit.osm.converter.intermodal.OsmIntermodalReaderFactory.create(country)
        return OsmIntermodalReaderWrapper(java_intermodal_reader)
    
    def __create_planit_intermodal_reader(self) -> PlanitIntermodalReaderWrapper:
        java_intermodal_reader = GatewayState.python_2_java_gateway.jvm.org.goplanit.io.converter.intermodal.PlanitIntermodalReaderFactory.create()
        return PlanitIntermodalReaderWrapper(java_intermodal_reader)
        
    #####################################
    #     WRITER FACTORY METHODS
    #####################################
        
    def __create_matsim_intermodal_writer(self) -> MatsimIntermodalWriterWrapper:
        java_network_writer = GatewayState.python_2_java_gateway.jvm.org.goplanit.matsim.converter.MatsimIntermodalWriterFactory.create()
        return MatsimIntermodalWriterWrapper(java_network_writer)
        
    def __create_planit_intermodal_writer(self) -> PlanitIntermodalWriterWrapper: 
        java_network_writer = GatewayState.python_2_java_gateway.jvm.org.goplanit.io.converter.intermodal.PlanitIntermodalWriterFactory.create()
        return PlanitIntermodalWriterWrapper(java_network_writer)        
        
    def create_reader(self, intermodal_reader_type: IntermodalReaderType, country:str = "Global") -> IntermodalReaderWrapper:
        """ factory method to create an intermodal  reader compatible with this converter
        :param intermodal_reader_type: the type of reader to create
        :param country: optional argument specifying the country of the source network. Used by some readers to initialise default settings. If absent
         but required, it defaults to "Global", i.e., no country specific information is used in initialising defaults if applicable
        """
        if not isinstance(intermodal_reader_type,IntermodalReaderType) : raise Exception("reader type provided is not of IntermodalReaderType, unable to instantiate")
        
        if  intermodal_reader_type == IntermodalReaderType.OSM:
            # OSM requires country to initialise default settings
            return self.__create_osm_intermodal_reader(country)
        elif intermodal_reader_type == IntermodalReaderType.PLANIT:
            return self.__create_planit_intermodal_reader() 
        else:
            raise Exception("unsupported intermodal reader type provided, unable to instantiate")
    
    def create_writer(self, intermodal_writer_type: IntermodalWriterType) -> IntermodalWriterWrapper:
        """ factory method to create an intermodal writer compatible with this converter
        :param intermodal_writer_type: the type of writer to create
        """
        if not isinstance(intermodal_writer_type,IntermodalWriterType) : raise Exception("writer type provided is not of IntermodalWriterType, unable to instantiate")
        
        if  intermodal_writer_type == IntermodalWriterType.MATSIM:
            return self.__create_matsim_intermodal_writer()
        elif intermodal_writer_type == IntermodalWriterType.PLANIT:
            return self.__create_planit_intermodal_writer() 
        else:
            raise Exception("unsupported intermodal writer type provided, unable to instantiate")        
        
class ConverterFactory:
    """ Access point for all things related to converting planit inputs via the planit predefined way of performing conversions (using a compatible reader and writer and providing
    them to the apropriate converter. For example one can convert an Open Street Map network to a Planit network using this functionality
    """
    
    def __init__(self):
        """ initialise the converter, requires gateway to be up and running, if not throw exception
        """
    
    def __create_network_converter(self) -> NetworkConverter:
        """ Factory method to create a network converter proxy that allows the user to create readers and writers and exposes a convert method
        that performs the actual conversion 
        """
        return NetworkConverter()
    
    def __create_zoning_converter(self) -> ZoningConverter:
        """ Factory method to create a zoning converter proxy that allows the user to create readers and writers and exposes a convert method
        that performs the actual conversion 
        """
        
        #TODO not made available publicly
        return ZoningConverter()
    
    def __create_intermodal_converter(self) -> IntermodalConverter:
        """ Factory method to create an intermodal converter proxy that allows the user to create readers and writers and exposes a convert method
        that performs the actual conversion 
        """
        return IntermodalConverter()
        
    def create(self, converter_type: ConverterType) -> _ConverterBase:        
        """ factory method to create a converter of a given type
        :param converter_type: the convert type to create
        :param reader: to use in the converter
        :param writer: to use in the converter 
        """
        if not GatewayState.gateway_is_running: raise Exception('A ConverterFactory can only be used when connection to JVM present, it appears not to be')
        
        if not isinstance(converter_type,ConverterType) : raise Exception("converter type provided is not of ConverterType, unable to instantiate")
        
        if converter_type == ConverterType.NETWORK:
            return self.__create_network_converter()
        elif converter_type == ConverterType.ZONING:
            return self.__create_zoning_converter()
        elif converter_type == ConverterType.INTERMODAL:
            return self.__create_intermodal_converter()
        else :
             raise Exception("Invalid converter type {} provided, no converter could be created".format(converter_type))
     