import threading
from functools import wraps

from cointools.thread import (_NoThread, _Thread)

__all__ = [
    "BaseManagerHandler",
    "MultipleManager"
]
def connected(func) : 
    @wraps(func) 
    def check(self, *args, **kwargs) : 
        if not hasattr(self, "_conn") :
            raise ValueError("please, connect api of bitcoin service")
        
        if self._conn == None :
            raise ValueError("please, connect api of bitcoin service")

        return func(self, *args, **kwargs)

    return check

class ManagerException(Exception) : 
    pass 
 

class BaseManagerHandler(object) :
    def __init__(self, key, service_class) : 
        self._key = key
        self._service_class = service_class
        self._event = threading.Event()


    @connected 
    def start(self) :
        if self.verify_to_service() :
            self._event.clear()
            
            try :
                while True : 
                    self.start_no_block()
            except :
                raise ManagerException()
            finally : 
                self._event.set()


    
    def connect(self) :
        """
            overide

            bitcoin api and key connect.
        """
        pass

    
    def get_ticker(self) : 
        """
            overide
            
            get surveillance targets.
        """
        pass

    
    def verify_to_service(self) : 
        """
            override 
            
            it verifies the service
        """
        return True

    def verify_to_ticker(self, ticker) :
        """
            override 
            it verifies the ticker
        """
        return True

    def start_no_block(self) : 
        ticker = self.get_ticker()

        if self.verify_to_ticker(ticker) :
            try :
                self.process_service(ticker)
            except :
                self.error_handler()

    @connected
    def call(self, ticker) : 
        print(self._service_class)
        self._service_class(self._conn, ticker)

    def process_service(self, ticker) :
        """
            override 
        """
        self.call(ticker)

    
    def error_handler(self) : 
        import traceback
        traceback.print_exc()
        
    
    def __enter__(self) : 
        return self
    
    def __exit__(self, type, val, traceback) :
        self.close() 


class MultipleManager(BaseManagerHandler) :
    _threads = _NoThread()
    
    _max_thread_size = 5

    _tickers = []

    
    def __init__(self, key, service_class) : 
        BaseManagerHandler.__init__(self, key, service_class)
        
    def _run(self, ticker) : 
        try : 
            self.call(ticker)
        except :
            self.error_handler()
        finally :
            self.finish(ticker)
    
    def process_service(self, ticker):
        if hasattr(self, "_threads") :
            vars(self).setdefault("_threads", _Thread())
        else : 
            self._threads = _Thread()

        assert len(self._threads) <= self._max_thread_size

        t = threading.Thread(target = self._run, args = (ticker, )) 
        
        t.daemon = False
        self._threads.append(t)

        t.start()
    
    def set_thread_size(self, size = _max_thread_size) : 
        self._max_thread_size = size
    
    def finish(self, ticker) : 
        pass 
    
    def close(self) : 
        self._threads.join()