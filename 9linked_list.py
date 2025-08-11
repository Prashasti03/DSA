class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0   # used in remove middle function

    def append(self,value):
        new_node = Node(value)
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        else:
            self.head = new_node
        self.size+=1

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def sum_nodes(self):
        temp = self.head
        sum = 0
        while temp:
            sum+=temp.data
            temp = temp.next
        print("Sum of nodes: ",sum)

    def sum_alternate_nodes(self):  # alternatively it can be called sum of nodes at odd positions
        temp = self.head
        sum = 0
        while temp:
            sum+=temp.data
            if temp.next!=None:
                temp = temp.next.next
            else:
                temp = temp.next
        print("Sum of alternate nodes: ",sum)

    def print_reverse(self):
        arr=[]
        temp  = self.head
        while temp:
            arr.append(temp.data)
            temp = temp.next
        print(arr[::-1])

    def remove_middle(self):
        mid = self.size//2
        temp = self.head
        i=0
        while(i!=mid-1):
            temp = temp.next
            i+=1
        temp.next = temp.next.next

    # Swap pairs in ll
    def swap_pairs(self):
        temp = self.head
        while temp!=None and temp.next!=None:
            temp.data, temp.next.data = temp.next.data, temp.data
            temp = temp.next.next
        print()

ll = LinkedList()
ll.append(23)
ll.append(54)
ll.append(65)
ll.append(55)
ll.append(23)
ll.append(88)
ll.display()
ll.sum_nodes()
ll.sum_alternate_nodes()
ll.print_reverse()
ll.remove_middle()
ll.display()
ll.swap_pairs()
ll.display()