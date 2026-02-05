class Queue:
    def __init__(self):
        self.items = []

    def __is_empty(self):
        return len(self.items) == 0
    
    def insert(self, value):
        self.items.append(value)

    def pop(self):
        if self.__is_empty():
            print("Warning: Cannot pop from an empty queue.")
            return None
        return self.items.pop(0)
    
q = Queue()

q.insert(10)
q.insert(20)
q.insert(30)

print(q.pop())        
print(q.pop())        
print(q.pop())        
print(q.pop())       


import json

class QueueOutOfRangeException(Exception):
    def __init__(self, size, message="size is exceeded"):
        self.size = size
        self.message = message
        # Call the base class constructor with the message
        super().__init__(self.message)
    
    def __str__(self):
        """Return a readable string representation of the error."""
        return f'{self.message}: entered items should be less than {self.size}'

class NamedQueue(Queue):
    _queues = {} 

    def __init__(self, name, size):
        super().__init__()
        self.name = name
        self.size = size

        NamedQueue._queues[name] = self

    def insert(self, value):
        if len(self.items) >= self.size:
            raise QueueOutOfRangeException(self.size)
        super().insert(value)

    @classmethod
    def get_queue(cls, name):
        return cls._queues.get(name)

    @classmethod
    def save(cls, filename="queues.json"):
        data = {}

        for name, queue in cls._queues.items():
            data[name] = {
                "size": queue.size,
                "items": queue.items
            }

        with open(filename, "w") as f:
            json.dump(data, f, indent=4) # python -> json

    @classmethod
    def load(cls, filename="queues.json"):
        with open(filename, "r") as f:
            data = json.load(f) #json -> python

        cls._queues = {}

        for name, info in data.items():
            q = cls(name, info["size"])
            q.items = info["items"]


q1 = NamedQueue("q1", 2)
q2 = NamedQueue("q2", 2)

try:
    q1.insert(1)
    q1.insert(2)
    q1.insert(3)
except QueueOutOfRangeException as qe:
    print(qe)

q2.insert(10)

NamedQueue.save()

NamedQueue.load()

print(NamedQueue.get_queue("q1").size)  
print(NamedQueue.get_queue("q2").items)  
