class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [None] * self.Max
        
    def get_hash(self,str):
        hash = 0
        for c in str:
            hash+=ord(c)
        return hash % self.Max
        
    def __setitem__(self, key, value):
        hash = self.get_hash(key)
        self.arr[hash] = value
    
    def __delitem__(self, key):
        hash = self.get_hash(key)
        self.arr[hash] = None
        
    def __getitem__(self,key):
        hash = self.get_hash(key)
        return self.arr[hash]

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
    ht['july 15'] = 75
    
    print(ht['july 26'])
    print(ht['july 23'])
    del ht['july 23']
    print(ht.arr)
    
