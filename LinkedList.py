#Linked List 
#creation of linked list from line 3 to line 11
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
# takes data from the user and inserts at the beginning
    def insert_at_beginning(self, data):
        beginning_node= Node(data, self.head)
        self.head = beginning_node

#prints the entire Linked List using the iterator itr
    def print(self):
        if self.head == None:
            print("Linked List is empty")
        else:
            itr = self.head
            llstr = ''
            while itr:
                llstr += '-->' + str(itr.data) 
                itr = itr.next
            print(llstr)

#insertion of element at the end
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data,None)
        else:
            itr = self.head
            while itr.next != None:
                itr = itr.next
            itr.next = Node(data, None)
#deletion of the data present in the list            
    def truncate_all_elements(self):
        self.head = None

#insertion of elements in the form list
    def insert_values(self, data_list):
        self.truncate_all_elements()
        for data in data_list:
            self.insert_at_end(data)

#length of the list
    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count+=1
            itr = itr.next
        return count

#deletion of an element present at the specified position
    def remove_at(self, index):
        if index < 0 or index >self.get_length()-1:
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index-1:
                    itr.next = itr.next.next
                    break
                itr = itr.next
                count +=1

%insertion of element at the specified position
    def insert_at(self, index, data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_beginning(data)
        
        else:
            count = 0
            itr = self.head
            while itr :
                if count == index-1:
                    node =Node(data, itr.next)
                    itr.next = node
                    break
                itr = itr.next
                count +=1
def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end(-5)
    ll.print()
    ll.insert_values(['banana','cherries','mango','orange'])
    ll.print()
    print(ll.get_length())
    ll.remove_at(3)
    ll.print()
    ll.insert_at(2,'jackfriut')
    ll.print()
    ll.insert_after_value("jackfruit","apple")
    
    
    
    
