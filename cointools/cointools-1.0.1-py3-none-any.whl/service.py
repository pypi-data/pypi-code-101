
__all__ = [
	"BaseServiceHandler"
]


class ServiceException(Exception) :
	pass

class BaseServiceHandler(object) : 
	_conn = None
	def __init__(self, conn, ticker) : 
		self._conn = conn 
		self._ticker = ticker 
		
		self.setup()
		print(self._conn)
		try : 
			self.action()
		except : 
			raise ServiceException()
		finally :
			self.finish()
			

	def setup(self) : 
		pass
	
	def action(self) : 
		pass

	def finish(self) : 
		pass 
