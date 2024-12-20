class Queue:
    def __init__(self):
        # initialize two empty stacks
        self.stack1 = [] # for enqueue operation
        self.stack2 = [] # for dequeue operation

    def enqueue(self, x: int) -> None:
        self.stack1.append(x)

    def dequeue(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop()) # as Queue follow FIFO, we can reverse the LIFO technique of stack_1 and store the reverse stack_1 to stack_2
        if self.stack2:
            return self.stack2.pop()
        else:
            raise IndexError("Dequeue an empty queue.")


q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
q.enqueue(3)
print(q.dequeue())  # Output: 2
