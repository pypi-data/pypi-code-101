from abc import ABC, abstractmethod
class IQueue(ABC):

    @abstractmethod
    def enqueue(self, item):
        raise NotImplementedError

    @abstractmethod
    def dequeue(self):
        raise NotImplementedError

    @abstractmethod
    def peek(self):
        raise NotImplementedError

  

class Node:
    """ This class represents each day of operations. 
        Given a store and sku, this class will hold the available, remaining, demand, and lastly ordering quantity
    """
    def __init__(self, name:str[None], ordered:int[None],demand:int[None],date= None,sku=None):
        """Initilazes an day with ordering quantity and demand
            

        Args:
            ordered (int): the amount of chicken ordered for a given sku and resturaent
            demand (int): the demand of the chicken for a given sku and restuarent
    
        """
        self.re = None
        self.ava = None
        self.ord = ordered
        self.demand = demand 
        self.date = date
        self.sku = sku 
        self.name = name
        self._waste = 0
        self.next = None
        self.prev = None


    def _prev_remaining(self):
        """Receives the previous days remaining food (Must be the same sku)

        """
        if self.prev != None:
            return self.prev.re
        return 0
    
    def _sum_demand(self):
        """ Calculates the sum of demand over all days before the shelf-life 
            e.g. shelf life = 3 : Demand (day1) = 20 , Demand( Day 2) = 30

        Returns:
            int: sum of the demand (e.g. 50)
        """
        num = 0
        prev = self.prev
        while prev != None:
            num += prev.demand
            prev = prev.prev
        return num
    
    def _curr_remaining(self):
        """Updates the amount of chicken left over after end of day 
        """
        self.re = self.ava - self.demand
    
    def _waste_remaining(self,expired):
        self._curr_remaining()
        self.re -= expired - self._sum_demand()

    
    
    def _waste_criteria(self,expired):
        if self._sum_demand() > expired:
            self._curr_remaining()
        else:
           self._waste_remaining(expired)
           return expired - self._sum_demand()


        
    
    def _cal_available(self):
        if self._prev_remaining() > 0:
            self.ava = self._prev_remaining() + self.ord
        else:
            self.ava = self.ord
    
    def initalize(self):
        """ Initializes the days that are before the shelf-life
        """
        self._cal_available()
        self._curr_remaining()
    
    def waste(self,expired):
        """ Calculates the waste for days that equal or greater than the shelf-life

        Args:
            expired (int): 
        """
        self._cal_available()
        if self._waste_criteria(expired) != None:
            self._waste = self._waste_criteria(expired)
       
         
        

    


class FIFOQueue(IQueue):
    def __init__(self,sku,store,ordering_type):
        self.head = None
        self.tail = None
        self.size = 0
        self.sku = sku
        self.store = store
        self.ord_type= ordering_type

    def enqueue(self, name ,ordered,demand,sku,date):
        if self.size == 0:
            # if the queue is empty, initialize both
            # head and tail to the item
            node = Node(
                name=name,
                ordered = ordered,
                demand = demand,
                sku = sku,
                date = date
                )
            self.tail = self.head = node
        else:
            # append the item at the end of the queue
            # i.e. put the item in line (FIFO)

            prev = self.tail
            self.tail.next = Node(
                name=name,
                ordered = ordered,
                demand = demand,
                sku = sku,
                date = date
            )
            if prev.date != date or prev.sku != sku:
                self.tail = self.tail.next
                self.tail.prev = prev

            
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError 

        # get the current head i.e. the FIRST in
        node = self.head
        # set the head to the next in line
        self.head = self.head.next
        if self.head != None:
            self.head.prev = None

        self.size -= 1

        if self.size == 0:
            # set the tail to empty
            self.tail = None

        # return the ordering quantity of the beginning of the shelf life 
        return {"Date":node.date,"store":node.name,f"{self.ord_type}_waste": node._waste,"sku": int(node.sku)}

    def peek(self):
        if self.size == 0:
            raise IndexError
        return self.head.value
    
    def empty(self):
        if self.size == 0:
            raise IndexError
        while self.size != 0:
            self.dequeue()
        