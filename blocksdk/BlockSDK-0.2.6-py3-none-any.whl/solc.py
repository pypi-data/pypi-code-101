from BlockSDK.base import Base
class Solc(Base):
	def genContract(self, request = {}):
		return self.request("GET","/solc/" + request['net'] + "/" + request['type'],request)
    
    	def encodefunction(self, request = {}):
		return self.request("POST","/solc/encodefunction",request)
