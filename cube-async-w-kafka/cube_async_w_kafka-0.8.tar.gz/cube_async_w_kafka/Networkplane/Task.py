from multiprocessing import Event, Manager
from ctypes import c_char_p


class Task():

    def __init__(self,):

        # Interruption: task to be done
        self.__to_do_task = Event()
        self.__to_do_task.clear()

        # Waiting event until finishing a task
        self.__finish_task = Event()
        self.__finish_task.set()

        # give an indication of a task status : success=True, failed=False
        self.__task_status = Event()
        self.__task_status.clear()

        self.__task_name=Manager().Value(c_char_p, "NONE")
        self.__instructions=Manager().dict()


    # Network plane method
    def set(self, task_name, instructions=None):

        #prepare
        self.__task_name.set(task_name)

        self.__instructions.clear()
        if isinstance(instructions, dict):
            for key, value in instructions.items():
                self.__instructions[key]=value

        self.__finish_task.clear()
        self.__task_status.clear()

        #interrupt & wait for the result
        self.__to_do_task.set()
        self.__finish_task.wait()

        #return the result after waiting for task execution
        return self.__task_status.is_set()




    # Producer method
    def success(self,):

        #clear interruption
        self.__to_do_task.clear()
        self.__task_name.set("NONE")

        self.__task_status.set()
        self.__finish_task.set()

    # Producer method
    def fail(self, ):

        self.__to_do_task.clear()
        self.__task_name.set("NONE")

        self.__task_status.clear()
        self.__finish_task.set()

    # Producer method
    def to_do(self):
        return self.__to_do_task.is_set()

    # Producer method
    def get_task(self):
        return {"name":self.__task_name.get(), "instructions":self.__instructions}





