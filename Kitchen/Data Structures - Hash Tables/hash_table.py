from runtime_utils import track_time
class Hashtable:
    def __init__(self,buckets):
        self.buckets = buckets
        self.hashmap = [[] for _ in range(self.buckets)]

    def __str__(self):
        return str(self.__dict__)

    def hash(self, key): #Andrei's version
        key = str(key)
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % self.buckets
        return hash_value
    
    @track_time
    def set(self,key,value):
        key = str(key) #Sneaky ints
        hash = self.hash(key)
        self.hashmap[hash].append([key,value]) #Linked lists(solves hash collisions)
    @track_time
    def get(self,key):
        key = str(key)
        hash = self.hash(key)
        bucket = self.hashmap[hash]
        for pair in bucket: #Linked lists(hash collisions just as Andrei said)
            if pair[0] == key:
                return pair[1]
    @track_time
    def keys(self):
        keys = []
        for i in range(len(self.hashmap)):
            for j in range(len(self.hashmap[i])): #Linked lists Imao
                key = self.hashmap[i][j][0]
                keys.append(key)
        return keys
        

my_hash_table = Hashtable(30)
my_hash_table.set(1,"yes")
my_hash_table.set("sdhs","yes")
my_hash_table.set("rjdjrej","yes")
my_hash_table.set("apple","This is an apple")
apple_value = my_hash_table.get("apple")
print(my_hash_table.keys())
print(apple_value)
print(my_hash_table.hashmap)
