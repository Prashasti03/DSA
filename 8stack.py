class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self,value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node 

    def pop(self):
        if self.head is None:
            raise IndexError("Pop from empty stack")
        ch=self.head.data
        self.head = self.head.next
        return ch


    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp=temp.next

def reverse_string(s):
    st = Stack()
    rev_str=""
    for ch in s:
        st.push(ch)
    while st.head is not None:
        rev_str+=st.pop()
    return rev_str

st = Stack()
str = "programming"
print(reverse_string(str))
# st.push(5)
# st.push(10)
# st.push(35)
# st.push(20)
# st.push(50)
# st.display()