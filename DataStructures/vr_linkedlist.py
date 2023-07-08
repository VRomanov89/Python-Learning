import vr_node

class vr_linkedlist:
    def __init__(self):
        self.head = vr_node.vr_node()
    
    def append(self, data):
        new_node = vr_node.vr_node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print (elems)

    def get(self, index):
        if index >= self.length():
            print("Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx +=1

    def erase(self, index):
        if index >= self.length():
            print ("Out of bounds")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1

mylist = vr_linkedlist()
mylist.display()
mylist.append(1)
mylist.append(3)
mylist.append(4)
mylist.display()
print("Element at 2nd", mylist.get(1))
mylist.erase(1)
print("Element at 2nd", mylist.get(1))
