from base import FIFOQueue
import pandas as pd

# Empty the queue for the next round 
def empty(dataframe,queue_dist):
    p=0
    q_list = list(queue_dist.values())
    while not all(q.size == 0 for q in q_list):
        queue = q_list[p]
        dataframe = dataframe.append(queue.dequeue(), ignore_index=True)
        if p == len(q_list)-1:
            p=0
        else:
            p+=1
    return dataframe

# Initialize the list with days before shelf life 
def initialize(ordering_type,shelf_life,data,number_sku_store):
    queue_dist={}
    pointer = 0
    while any(q.size != shelf_life-1 for q in queue_dist.values()) or len(queue_dist)!= number_sku_store:
        try:
            date,store,sku,ord,demand = data.iloc[pointer]
        except IndexError as e:
            not_enough = [[q.store,q.sku,q.size] for q in queue_dist.values() if q.size !=shelf_life-1]
            print(f"The data doesn't contain at least {shelf_life-1} days of these store and sku combination ordering and demand quantities: {not_enough} ")
            return queue_dist
        if not store+str(sku) in queue_dist.keys():
            queue_dist[store+str(sku)] = FIFOQueue(sku,store,ordering_type)
        queue = queue_dist[store+str(sku)]
        
        if queue.size !=shelf_life-1: 
            queue.enqueue(name=store, ordered=ord,sku=sku,date=date,demand=demand)
            curr = queue.tail
            curr.initalize()
   
        pointer+=1
    return queue_dist


# Days that can potiental to have waste
def run_simulation(queue_dist,days,data):
    res = pd.DataFrame()
    for i in range(days): ## using number because the days are sorted it  - o(k*n) -> o(logk*n) -> o(n)
        date,store,sku,ord,demand = data.iloc[i]
        queue = queue_dist[store+str(sku)]
        expired = queue.head.ord
        queue.enqueue(name=store, ordered=ord,sku=sku,date=date,demand=demand)
        curr = queue.tail
        curr.waste(expired)
        res = res.append(queue.dequeue(), ignore_index=True)
    
    return res