from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current == self.capacity:
             # adds item to tail
            self.storage.add_to_tail(item)
            # save current head so we can change pointers
            old_head = self.storage.head
            # set head to the one that was next of head
            self.storage.head = old_head.next
            # make it so that the head can point back to the tail
            self.storage.head.prev = self.storage.tail
            # make it so that the tail can point to the head
            self.storage.tail.next = self.storage.head
        else:
            self.storage.add_to_tail(item)
            self.current += 1

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # TODO: Your code here
        curr = self.storage.head
        tail = self.storage.tail
        list_buffer_contents.append(curr.value)
        while(curr is not tail):
            list_buffer_contents.append(curr.next.value)
            curr = curr.next
        return list_buffer_contents


newRingBuffer = RingBuffer(5)
# [1, 3, 4, 7, 9] -> [3, 4, 7, 9, 10]
newRingBuffer.append(1)
newRingBuffer.append(3)
newRingBuffer.append(4)
newRingBuffer.append(7)
newRingBuffer.append(9)
newRingBuffer.append(10)
newRingBuffer.append(12)
newRingBuffer.append(15)
print(newRingBuffer.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
