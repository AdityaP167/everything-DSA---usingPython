# Collision handled using Linear Probing Method
#linear probing
class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [None] * self.Max
        
    def get_hash(self, key):
        hash = 0 
        for char in key:
            hash+=ord(char)
        return hash % self.Max
        
    def __setitem__(self, key, value):
        hash_value = self.get_hash(key)
        if self.arr[hash_value] == None:
            self.arr[hash_value] = (key, value)
            return
        else:
            for i in range(1,self.Max):
                index = (hash_value + i) % self.Max
                if self.arr[index] == None:
                    self.arr[index] = (key, value)
                    return
            print(f"Can't add '{key}' due to lack of empty space. Please increase array size.")
                
    def __getitem__(self,key):
        for element in self.arr:
            if element[0] == key:
                return element[1]
        print(f"'{key}' not present")
                
    def __delitem__(self, key):
        for i in range(self.Max):
            if self.arr[i][0] == key:
                self.arr[i] = None
                return
        
        print("Key not present")
                
                    
if __name__ == '__main__':
    ht = HashTable()
    print(ht.arr)
    ht['jan 1'] = 100
    ht['jan 2'] = 200
    ht['jan 3'] = 300
    ht['jan 4'] = 400
    ht['jan 5'] = 500
    ht['jan 6'] = 600
    ht['jan 7'] = 700
    ht['jan 8'] = 800
    ht['jan 9'] = 900
    ht['jan 10'] = 1000
    ht['jan 11'] = 1100
    ht['jan 12'] = 1200
    
    print(ht.arr)

    ht['jan 8']
    del ht['jan 8']
