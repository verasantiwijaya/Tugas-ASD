class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def display(self):
        current = self.top
        while current:
            print('-', current.data)
            current = current.next
    
    def menu(self):
        stack = Stack()
        while True:
            menumu =  input("\nMENU STACK LINKED LIST PADA TUMPUKAN BUKU\n1. OPERASI PUSH\n2. OPERASI POP\n masukkan menu: ")
            print("="*42)
            if menumu == "1":
                brp = int(input("Masukkan jumlah tumpukan: "))
                for i in range(brp):
                    nama = input("Masukkan jenis buku: ")
                    stack.push(nama)
                print("="*42)
                print("tampilkan tumpukan:") , stack.display()
            if menumu == "2":
                stack.pop()
                print("tampilkan tumpukan:") , stack.display()
            print("="*42)

if __name__ == "__main__":
    l = Stack()
    l.menu()