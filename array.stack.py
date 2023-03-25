class StackArray:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def display(self):
        print(self.items)

    def menu(self):
        stack = StackArray()
        while True:
            menumu =  input("\nMENU STACK ARRAY PADA TUMPUKAN PIRING\n1. OPERASI PUSH\n2. OPERASI POP\n masukkan menu: ")
            print("="*100)
            if menumu == "1":
                brp = int(input("Masukkan jumlah tumpukan: "))
                for i in range(brp):
                    nama = input("Masukkan warna piring: ")
                    stack.push(nama)
                print("="*100)
                print("tampilkan tumpukan:") , stack.display()
            if menumu == "2":
                stack.pop()
                print("tampilkan tumpukan:") , stack.display()
            print("="*100)

if __name__ == "__main__":
    l = StackArray()
    l.menu()