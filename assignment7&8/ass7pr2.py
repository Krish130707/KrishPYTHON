class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, key):
        current = self.head
        prev = None
        
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        
        while current and current.data != key:
            prev = current
            current = current.next
        
        if current is None:
            print("Key not found in the list.")
            return
        
        prev.next = current.next
        current = None

# Menu-driven Interface
ll = LinkedList()
while True:
    print("\nMenu:")
    print("1. Insert a node")
    print("2. Delete a node")
    print("3. Display linked list")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        data = int(input("Enter data to insert: "))
        ll.insert(data)
    elif choice == '2':
        key = int(input("Enter data to delete: "))
        ll.delete(key)
    elif choice == '3':
        ll.display()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")
