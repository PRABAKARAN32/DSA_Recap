from list import Node as node
from linked_list_crud import CRUD_Linked_List

class Stack:
    head = None
    count = 0
    def push(self,val):
        new_node = node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next =self.head
            self.head = new_node
        self.count += 1
        return
    def pop(self):
        if not self.head:
            print("Stack is Empty")
            return
        pop_val = self.head.val
        self.head = self.head.next
        self.count -= 1
        return pop_val
    
    def peek(self):
        if not self.head:
            print("Stack is Empty")
            return
        return self.head.val
    
    def is_empty(self):
        if not self.head:
            return True
        return False
    
    def size(self):
        return self.count
    

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
# print(stack.size())


# print("Peek Element = ", stack.peek() )

# stack.pop()
# stack.pop()
# print("Peek Element = ", stack.peek() )

stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
# stack.pop()
# print("Empty") if stack.is_empty() else print("Not Empty")
# stack.peek()
# ite = CRUD_Linked_List()
# ite.iterate(stack.head)

    

