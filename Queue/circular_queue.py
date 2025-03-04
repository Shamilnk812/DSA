
class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.queue = [None] * self.size
        self.front = -1
        self.rear = -1
    
    
    def is_empty(self):
        return self.front == -1


    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    

    def enqueue(self,data):
        if self.is_full():
            print('queue is full')
            return
        
        if self.front == -1 : # If inserting the first element
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data


    def dequeue(self):
        if self.is_empty():
            print('queue is empty')
            return

        removed_item = self.queue[self.front]   
        self.queue[self.front] = None  

        if self.front == self.rear : # If queue becomes empty after dequeue
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1)  % self.size

        return f' this {removed_item} item removed'


    def display(self):
        if self.is_empty():
            print('queue is empty cant print')
            return
        
        i = self.front
        while True:
            print(self.queue[i],end=' - ')
            if i == self.rear:
                break
            i = (i + 1) % self.size

    

q1 = CircularQueue(5)
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
q1.dequeue()
q1.enqueue(100)

q1.display()
print(q1.queue)