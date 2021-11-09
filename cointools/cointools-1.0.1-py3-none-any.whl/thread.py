
__all__ = [
	"_NoThread",
	"_Thread"
]

class _NoThread : 
	def append(self, thread) :
		pass
	def join(self) : 
		pass
	
class _Thread(list) :
	def append(self, thread) :
		self.reap()
		
		if thread.daemon : 
			return 
		
		super().append(thread)


	def pop_all(self) : 
		self[:], result = [], self[:]
		return result 
	
	def join(self) : 
		for thread in self.pop_all() :
			thread.join()

	def reap(self) :
		self[:] = (thread for thread in self if thread.is_alive())