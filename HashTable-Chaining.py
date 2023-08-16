#Collision handled using Chaining method
class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [[] for _ in range(self.Max)]  
        
    def get_hash(self, key):
        hash_value = 0
        for c in key:
            hash_value += ord(c)
        return hash_value % self.Max
        
    def __setitem__(self, key, value):
        hash_value = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[hash_value]):
            if len(element) == 2 and element[0] == key:
                found = True
                self.arr[hash_value][index] = (key, value)
        if not found:
            self.arr[hash_value].append((key, value))
                
    def __delitem__(self, key):
        hash_value = self.get_hash(key)
        for index, element in enumerate(self.arr[hash_value]):
            if element[0] == key:
                del self.arr[hash_value][index]
        
    def __getitem__(self, key):
        hash_value = self.get_hash(key)
        for index, element in enumerate(self.arr[hash_value]):
            if element[0] == key:
                return element[1]  

if __name__ == '__main__':  
    ht = HashTable()
    print(ht.arr)
    
    ht['july 1'] = 100
    ht['july 11'] = 13
    ht['july 13'] = 145
    ht['july 23'] = 326
    ht['july 22'] = 757
    ht['july 16'] = 10
    ht['july 26'] = 1000
    ht['july 6'] = 525
    ht['july 3'] = 21
    ht['july 11'] = 75
    
    print(ht['july 26'])
    print(ht['july 11'])
    del ht['july 23']
    print(ht.arr)
