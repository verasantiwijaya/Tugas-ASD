class QueueArray:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def EnQueue(self, item):
        self.items.append(item)

    def DeQueue(self):
        if self.isEmpty():
            return None
        return self.items.pop(0)

    def printQueue(self):
        print(self.items)

    def menu(self):
            queue = QueueArray()
            while True:
                menumu =  input("\nMENU QUEUE ARRAY PADA ANTRIAN BANK\n1. OPERASI ENQUEUE\n2. OPERASI DEQUEUE\n masukkan menu: ")
                print("="*42)
                if menumu == "1":
                    brp = int(input("Masukkan jumlah antrian: "))
                    for i in range(brp):
                        nama = input("Masukkan nama pengantri: ")
                        queue.EnQueue(nama)
                    print("="*42)
                    print("tampilkan antrian:") , queue.printQueue()
                if menumu == "2":
                    queue.DeQueue()
                    print("tampilkan antrian:") , queue.printQueue()
                print("="*42)

if __name__ == "__main__":
    l = QueueArray()
    l.menu()