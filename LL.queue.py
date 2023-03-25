#Berikut ini adalah contoh implementasi Python untuk struktur data queue menggunakan linked list:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def EnQueue(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def DeQueue(self):
        if self.isEmpty():
            return None
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None
        return temp.data

    def printQueue(self):
        temp = self.front
        while temp is not None:
            print(temp.data, "-->", end=" ")
            temp = temp.next

    def menu(self):
        queue = Queue()
        while True:
            menumu =  input("\nMENU QUEUE LINKED LIST PADA ANTRIAN TIKET\n1. OPERASI ENQUEUE\n2. OPERASI DEQUEUE\n masukkan menu: ")
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
            print("\n")
            print("="*42)

if __name__ == "__main__":
    l = Queue()
    l.menu()
