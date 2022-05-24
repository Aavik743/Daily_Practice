class Node:
    def __init__(self, data=None, nxt=None, prev=None):
        self.data = data
        self.nxt = nxt
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('Linked List is empty')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.nxt else str(itr.data)
            itr = itr.nxt
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.nxt:
            itr = itr.nxt
        itr.nxt = Node(data, None)

    def insert_from_list(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_beginning(data)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.nxt
        return count

    def remove_at_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Improper Index')
        if index == 0:
            self.head = self.head.nxt
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.nxt = itr.nxt.nxt
                break
            count += 1
            itr = itr.nxt

    def insert_at_index(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Improper Index')
        if index == 0:
            self.insert_at_beginning(data)
        if index == self.get_length() - 1:
            self.insert_at_end(data)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                new = Node(data, itr.nxt)
                itr.nxt = new
                break
            itr = itr.nxt
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.nxt = Node(data_to_insert, self.head.nxt)

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.nxt = Node(data_to_insert, itr.nxt)
                return
            itr = itr.nxt

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.nxt

        itr = self.head
        while itr.nxt:
            if itr.nxt.data == data:
                itr.nxt = itr.nxt.nxt
                break
            itr = itr.nxt


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(12)
    ll.print()
    ll.insert_at_beginning(23)
    ll.print()
    ll.insert_at_end(34)
    ll.print()
    list_name = ['Harry', 'Ron', 'Hermione', 'Potter', 'Wesley', 'Granger']
    ll.insert_from_list(list_name)
    ll.print()
    ll.remove_at_index(3)
    ll.print()
    ll.insert_at_index(3, 'Hermione')
    ll.print()
    after = 'Ron'
    to_insert = 'after_Ron'
    ll.insert_after_value(after, to_insert)
    ll.print()
    value = 'after_Ron'
    ll.remove_by_value(value)
    ll.print()
