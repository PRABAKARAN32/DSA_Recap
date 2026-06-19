from list import Node as node
from linked_list_crud import CRUD_Linked_List

class Queue:
    head = None
    count = 0
    def enqueue(self,val):
        new_node = node(val)
        
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.count += 1
        return

    def dequeue(self):
        if not self.head:
            print("Queue is Empty")
            return
        
        temp = self.head

        if not self.head.next:
            self.head = None

        else:
            while temp.next.next:
                temp = temp.next
            temp.next = None
        self.count -= 1
    
    def peek(self):
        if not self.head:
            print("Queue is Empty")
            return
        return self.head.val
    
    def is_empty(self):
        if not self.head:
            return True
        return False
    
    def size(self):
        return self.count
    


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue.size())
# itr = CRUD_Linked_List()
# itr.iterate(queue.head)
print(queue.peek())
queue.dequeue()
queue.dequeue()
queue.dequeue()

# itr.iterate(queue.head)

print(queue.size())
print(queue.peek())