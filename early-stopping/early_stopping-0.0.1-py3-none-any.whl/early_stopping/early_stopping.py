from collections import deque

class EarlyStopping:
    def __init__(self, depth, ignore, method='slope'):
        self.depth = depth
        self.ignore = ignore
        self.clock = 0
        self.method = method
        self.queue = deque(maxlen=depth)
        self.methods = {
            'slope' : self.check_slope,
            'consistency' : self.check_consistency
        }
    
    def check(self, elem):
        self.queue.append(elem)
        self.clock += 1

        if self.is_stoppable():
            return True
        return False
    
    def is_stoppable(self):
        return self.clock > self.ignore and self.methods[self.method]()

    def check_slope(self):
        x = [i for i in range(len(self.queue))]
        n = len(x)
        y = self.queue
        return (n*(sum([x[i]*y[i] for i in range(n)])) - sum(x)*sum(y))/(n*sum([v**2 for v in x]) - sum(x)**2) >= 0
    
    def check_consistency(self):
        last = self.queue[0]
        for elem in self.queue:
            if elem < last:
                return False
            last = elem
        return True
    
    def reset(self):
        self.__init__(self.depth, self.ignore)
    
    def __str__(self):
        return f'Queue: {self.queue}\nStopping conditions: {self.is_stoppable()}'