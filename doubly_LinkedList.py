class Node:
    def __init__(self, data=None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
      
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def traverse_forward(self):
        if self.head == None:
            print("LL is empty")
        else:
            itr = self.head
            forward_str = ''
            while itr:
                forward_str +='-->' + str(itr.data)
                itr = itr.next
            print(forward_str)
        
    def traverse_backward(self):
        if self.head == None:
            print("LL is empty")
        else:
            itr = self.last_node()
            backward_str = ''
            while itr:
                backward_str += str(itr.data)+'-->'
                itr = itr.prev
            print(backward_str)
        
    def last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr
        
    def insert_at_beginning(self, data):
        node = Node(data, self.head, None)
        if self.head != None:
            self.head.prev = node
        self.head = node
        
    def insert_at_end(self, data):
        if self.head == None:
            node = Node(data, None, self.head)
            self.head = node
        else:
            itr = self.last_node()
            node = Node(data, None, itr)
            itr.next = node
            
    def get_length(self):
        if self.head is None:
            return 0
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count
        
    def insert_at(self, data, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index-1:
                    node = Node(data, itr.next, itr)
                    if node.next:
                        node.next.prev = node
                        itr.next = node
                        break
                itr = itr.next
                count+=1
                
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    itr.next = itr.next.next
                    itr.next.next.prev = itr
                    return
                itr = itr.next
                count+=1
        
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_at_beginning(5)
    dll.insert_at_beginning(15)
    dll.insert_at_beginning(25)
    dll.insert_at_beginning(35)
    dll.insert_at_beginning(45)
    dll.insert_at_beginning(55)
    dll.traverse_forward()
    dll.traverse_backward()
    dll.insert_at_end(-5)
    dll.insert_at_end(-15)
    dll.traverse_forward()
    dll.insert_at(100000, 0)
    dll.insert_at(200000000, 4)
    dll.traverse_forward()
    dll.remove_at(4)
    dll.traverse_forward()
    dll.insert_values(['banana','apple','cherry','mango'])
    dll.traverse_forward()
