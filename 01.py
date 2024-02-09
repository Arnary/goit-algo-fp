class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data) 
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def reverse_linked_list(self):
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev
        return prev

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return

        sorted_head = None
        cur = self.head

        while cur:
            next_node = cur.next
            sorted_head = self.insert_into_sorted(sorted_head, cur)
            cur = next_node

        self.head = sorted_head

    def insert_into_sorted(self, sorted_head, new_node):
        if not sorted_head or new_node.data < sorted_head.data:
            new_node.next = sorted_head
            return new_node

        current = sorted_head
        while current.next and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return sorted_head

    def merge_sorted_lists(self, other_list):
        merged = LinkedList()
        other_list.insertion_sort()
        self.insertion_sort()
        current1 = self.head
        current2 = other_list.head

        while current1 and current2:
            if current1.data < current2.data:
                merged.insert_at_end(current1.data)
                current1 = current1.next
            else:
                merged.insert_at_end(current2.data)
                current2 = current2.next

        while current1:
            merged.insert_at_end(current1.data)
            current1 = current1.next

        while current2:
            merged.insert_at_end(current2.data)
            current2 = current2.next

        return merged

    def print_linked_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
