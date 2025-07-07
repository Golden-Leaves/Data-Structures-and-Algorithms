from runtime_utils import track_time
class Array:
    def __init__(self):
        self.length = 0
        self.data = {}
    def push(self,item):
        self.data[0] = item
        self.previous_i = None
        for i in range(0,self.length):
            self.previous_i = self.data[i]
            self.data[i+1] = self.data[i]
        