import os
import subprocess
import traceback
from py4j.java_gateway import JavaGateway
from planit import GatewayUtils
from planit import GatewayState
from planit import GatewayConfig
from planit import ConverterFactory
from planit import PlanitProject
from builtins import isinstance

class Planit:
            
    def __init__(self, debug_info=False, standalone=True):
        """Constructor of PLANit python wrapper which acts as an interface to the underlying PLANit Java code
        :param project_path the path location of the XML input file(s) to be used by PLANitIO
        :param standalone when true this PLANit instance bootstraps a java gateway and closes it upon completion of the scripts when false <to be implemented>
        """  
        # explicitly set uninitialized member variables to None
        self.assignment_project = None                     
        self._converter_factory_instance = ConverterFactory()
        
        self._debug_info = debug_info
        
        if not standalone:
            raise Exception('Standalone argument can only be true at this time, server mode not yet supported')  
        self.__start_java__()

       
    def __start_java__(self):            
        """Start the gateway to Java 
        """  
        
        #find the location of this file, so that other directories can be located relative to it    
        dir_path = os.path.dirname(os.path.realpath(__file__))
        # Bootstrap the java gateway server
        if not GatewayState.gateway_is_running:
            # register dependencies (both for:
            #    - the IDE run, 
            #    - the RELEASE environment
            #    - a venv (virtual python) environment (which contains a bug that requires us to use a different path)
            dependencySet = {
                os.path.join(dir_path, GatewayConfig.IDE_SHARE_PATH,GatewayConfig.PLANIT_SHARE),
                os.path.join(dir_path, GatewayConfig.IDE_SHARE_PATH, GatewayConfig.PY4J_SHARE),
                os.path.join(GatewayConfig.RELEASE_SHARE_PATH, GatewayConfig.PLANIT_SHARE),
                os.path.join(GatewayConfig.VENV_RELEASE_SHARE_PATH,GatewayConfig.PLANIT_SHARE),                
                os.path.join(GatewayConfig.RELEASE_SHARE_PATH,GatewayConfig.PY4J_SHARE),
                os.path.join(GatewayConfig.VENV_RELEASE_SHARE_PATH, GatewayConfig.PY4J_SHARE)}
            dependencySeparator = ';'
            fullString = dependencySeparator.join(dependencySet)
            
            cmd = ['java', '-classpath', fullString, GatewayConfig.JAVA_GATEWAY_WRAPPER_CLASS]
            if self._debug_info: print('Java classpath: ' + fullString)
            GatewayState.planit_java_process = subprocess.Popen(cmd)           
             
            # now we  connect to the gateway, ask Py4J to auto convert containers between Python and Java
            GatewayState.python_2_java_gateway = JavaGateway()
            GatewayState.gateway_is_running = True            
                
            #TODO: Note we are not waiting for it to setup properly --> possibly considering some mechanism to wait for this to ensure proper connection!
            if self._debug_info: print('Java interface running with PID: '+ str(GatewayState.planit_java_process.pid))
        else:
            raise Exception('PLANit java interface already running, only a single instance allowed at this point')
            
    def __del__(self):
        """Destructor of PLANit object which shuts down the connection to Java
        """
        self.__stop_java__()
        
    def __stop_java__(self):        
        """Cleans up the gateway in Java in case this has not been done yet. It assumes a single instance available in Python tied
        to a particular self. Only that instance is allowed to terminate the gateway. In case an exception is raised indicating an instance is
        already running it is likely this method has not been called. If you are certain the object has gone out of scope, it is likely the garbage collector
        has not yet removed the object and therefore the connection still exists., use force_stop_java to achieve this if you do not want to call the garbage 
        collector
        """          
        # Let the instance that instantiated the connection also terminate it automatically
        if GatewayState.gateway_is_running:
            # Check if the process has really terminated & force kill if not.           
            try:
                GatewayState.python_2_java_gateway.shutdown()
                GatewayState.planit_java_process.terminate()
                if (GatewayState.planit_java_process.poll() != None):
                    os.kill(GatewayState.planit_java_process.pid, 0)
                    GatewayState.planit_java_process.kill()
                # Wait for zombie process to provide post-mortem information. 
                # Only after this call the subprocess will be gone and we will not receive warnings
                # that it is still alive regardless of the fact we killed it zoom
                GatewayState.planit_java_process.wait()
                GatewayState.gateway_is_running = False
                GatewayState.python_2_java_gateway = None
                if self._debug_info: print ("Forced kill of PLANitJava interface")
            except OSError:
                if self._debug_info: print ("Terminated PLANitJava interface")   
            except:
                traceback.print_exc()        
                
    def force_stop_java(self):
        """ force the java connectoind to be ended, only use when you are certain you no longer are using this Planit instance
        """
        self.__stop_java__()
                
    def create_project(self, project_path:str = None) -> PlanitProject:
        """ access to project. Once access is requested the first time, project instance is created
            and returned
            :param project_path to use, when left empty current working directory is used
            :return create and/or provide access to the planit project instance to conduct an assignment 
        """        
        if not self.assignment_project:
            self.assignment_project = PlanitProject(project_path)
        else:
            raise Exception("Cannot create a project when project is already created, only a single project allowed")
        return self.assignment_project
    
    def project(self) -> PlanitProject:
        """ access assignment project assuming it has been created. If not it is created by using 
            the current working directory as the project path. If this is not desired please use create_project
            before invoking this method            
        """
        if not self.assignment_project:
            self.create_project()
        return self.assignment_project
        
    @property
    def converter_factory(self) -> ConverterFactory:
        """ access to converter factory
        :return factory to create converters for networks, zoning, etc.
        """
        return self._converter_factory_instance