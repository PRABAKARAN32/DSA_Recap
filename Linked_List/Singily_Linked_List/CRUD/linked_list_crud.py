from list import Node as node

class CRUD_Linked_List:
    head = None
    def add(self,value):
        
        new_node = node(value)

        if self.head == None:
            self.head = new_node

        else:
            temp = self.head

            while temp.next:
                temp = temp.next
            temp.next = new_node
        # self.iterate(self.head)
        return self.head
    
    def update_by_position(self,place,new_val):
        print("The index start from 0")

        temp = self.head

        if place == 0:
            self.head.val = new_val
            return True
        else:
            count = 0

            while temp:
                if count == place:
                    temp.val = new_val
                    return True
                temp = temp.next
                count += 1
            print("Index Out of Bound.")
            return None

    def update_by_value(self,val,new_val):
        temp = self.head

        if not temp:
            print("No Element Present")
            return
        
        if val == temp.val:
            print("Before List : ", end=self.iterate())
            self.head.val = new_val
            print("After List : ", end=self.iterate())
            return
        while temp:
            if temp.val == val:
                print("Before List : ", end=self.iterate())
                temp.val = new_val
                print("After List : ", end=self.iterate())
                return
            temp = temp.next    
        print("No Element Found")
        return
    
    def delete_by_position(self,place):
        print("The index start from 0")

        temp = self.head

        if place == 0:
            self.head = self.head.next
            return True
        else:
            count = 0

            while temp.next:
                if count == place-1:
                    temp.next = temp.next.next
                    return True
                temp = temp.next
                count += 1
            return False


    def delete_by_value(self,val):
        temp = self.head

        if not temp:
            print("No Element Present")
            return
        
        if val == temp.val:
            print("Before List : ", end=self.iterate())
            self.head = self.head.next
            print("After List : ", end=self.iterate())
            return
        while temp.next:
            if temp.next.val == val:
                print("Before List : ", end=self.iterate())
                temp.next = temp.next.next
                print("After List : ", end=self.iterate())
                return
            temp = temp.next    
        print("No Element Found")
        return
    
    def iterate(self,head=None):
        temp = self.head if not head else head

        if not temp:
            print("List is Empty")
            return

        while temp:
            print(temp.val,end=" -> ")
            temp = temp.next
        print("None")
        return None
    
    def is_value_present(self,val,head=None):
        temp = self.head if not head else head

        while temp:
            if temp.val == val:
                return True
            temp = temp.next

        return False


# ll = CRUD_Linked_List()

# ll.add(2)
# ll.add(3)
# ll.add(4)
# ll.add(5)
# ll.add(6)

# delete by value
# print("Present") if ll.is_value_present(3) else print("Not Present")
# ll.delete_by_value(3)
# print("Present") if ll.is_value_present(3) else print("Not Present")

# #delete by place
# print("Present") if ll.is_value_present(3) else print("Not Present")
# ll.delete_by_position(0)
# print("Present") if ll.is_value_present(3) else print("Not Present")

# ll.update_by_value(6,10)
# ll.update_by_position(5,10)
# ll.iterate()