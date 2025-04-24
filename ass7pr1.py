class Node:
    def _init_(self, data):
        self.data = data
        self.next = None
class linkedList:
    def _init__(self):
        self.head = None
    #method for display linked list    
    def display(self):
        if self.head is None:
            print("The list is empty.")
            return
        p = self.head
        while p:
            print(p.data, end="  ")
            p = p.next
       

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        p = self.head
        while p.next:
            p = p.next
        p.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, data, index):
        new_node = Node(data)
        if index == 0:
            self.insert_at_beginning(data)
            return
        p = self.head
        for _ in range(index - 1):
            if p is None:
                print("Index out of bounds.")
                return
            p = p.next
        new_node.next = p.next
        p.next = new_node

    def delete_at_index(self, index):
        if self.head is None:
            print("The list is empty.")
            return
        if index == 0:
            self.head = self.head.next
            print("Node at index 0 deleted.")
            return
        p = self.head
        prev = None
        for _ in range(index):
            if p is None or p.next is None:
                print("Index out of bounds.")
                return
            prev = p
            p = p.next
        prev.next = p.next
        print(f"Node at index {index} deleted.")

# Example Usage
if __name__ == "_main_":
    ll = linkedList()
    while True:
        print("\nChoose an option:")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Insert at index")
        print("4. Delete at index")
        print("5. Display list")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            data = int(input("Enter value to insert at beginning: "))
            ll.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter value to insert at end: "))
            ll.insert_at_end(data)
        elif choice == 3:
            data = int(input("Enter value to insert: "))
            index = int(input("Enter index: "))
            ll.insert_at_index(data, index)
        elif choice == 4:
            index = int(input("Enter index to delete: "))
            ll.delete_at_index(index)
        elif choice == 5:
            ll.display()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")