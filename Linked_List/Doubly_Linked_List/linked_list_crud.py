from list import Node as node


class List:

    head=None

    def add(self,val):
        new_node = node(val)

        if not self.head:
            self.head = new_node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        return
    
    def remove_by_place(self,place):
        print("The index start from zero or 0")

        if place == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        count = 0
        temp = self.head

        while temp.next:
            if count == place-1:
                temp.next = temp.next.next
                if temp.next:
                    temp.next.prev = temp
                return
            count += 1
            temp = temp.next
        print("The Element is not found.")
        return 


    def remove_by_val(self,val):

        if not self.head:
            print("List is Empty")
            return
        
        temp = self.head

        while temp:
            if temp.val == val:
                if temp.val == self.head.val:
                    self.head = self.head.next
                    self.head.prev = None
                    return
                elif not temp.next:
                    temp.prev.next = None
                    return
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    return
                
            temp = temp.next
        print("Element Not Found.")
        
    def update_by_val(self,val,new_val):

        if not self.head:
            print("List is Empty")
            return
        
        temp = self.head

        while temp:
            if temp.val == val:
                temp.val = new_val
                return
            temp = temp.next
        print("Element Not Found.")

    def update_by_place(self,place,val):
        print("The index start from zero or 0")

        count = 0
        temp = self.head

        while temp:
            if count == place:
                temp.val = val
                return
            count += 1
            temp = temp.next
        print("Index Out of Bound.")
        return 
    
    def iterate_forward(self,head=None):
        temp = self.head if not head else head

        if not temp:
            print("List is Empty")
            return
        while temp:
            print(temp.val,end=" <->")
            temp = temp.next
        print("None")
        return
    
    def iterate_revers(self):
        tail_node = self.get_tail()
        while tail_node:
            print(tail_node.val,end="<->")
            tail_node = tail_node.prev
        print("None")
        return
    

    def get_head(self):
        if not self.head:
            print("The List is Empty..")
            return
        return self.head


    def get_tail(self,head=None):
        tail = self.head if not head else head

        if not tail:
            print("The List is Empty..")
            return

        while tail.next:
            tail = tail.next
        return tail
        


ll = List()

ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)

ll.iterate_forward()
# ll.iterate_revers()

# ll.remove_by_place(5)
# ll.remove_by_val(6)
# ll.update_by_place(5,100)
# ll.update_by_val(6,100)
ll.iterate_forward()
