class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

queue = Queue()
queue.enqueue((3,"taskC"))
queue.enqueue((2,"taskA",))
queue.enqueue((1,"taskB"))

def simple_priority_queue(tasks):
    row  = []
    temprow = []
    while not queue.is_empty():
        temprow.append(queue.dequeue())
    temprow.sort()
    for priority,name in temprow:
        row.append(name)
    return row
print(simple_priority_queue(queue))

