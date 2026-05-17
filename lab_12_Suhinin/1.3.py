row = ["request1","request2","request3"]
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

def process_request(requests):
    queue = Queue()
    for i in requests:
        queue.enqueue(i)
    processed = []
    while not queue.is_empty():
        processed.append(queue.dequeue())
    return processed
print(process_request(row))