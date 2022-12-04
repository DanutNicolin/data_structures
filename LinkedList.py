"""
A linked list is a list that stores data in random locations of memory (unlike a list which stores data in consecutive memory locations).
Each element of a linked list is a node object.
Each node has two class attributes: 
    - data (actual data to be stored) 
    - next (pointer to the next node -> takes the value of the following node data)
If next attribute of a node is None -> that is the last node.

Step by step instructions:
    1. Make node class:
        - initialize data attr
        - initialize next attr as None

    2. Make LinkedList class:
        - initialize head attr as None

        a. append()
            - make new node instance

            - check if head is None:
                    - if True then the linked list is empty
                    - assign data of new node to head and return
            
            - make last_node var == to head of the linked list
            - iterate and make last_node == last_node.next until last_node.next is None (it means you reached the last node)
            - add the new_node to the last_node.next attr (this puts the newly created node to the end of list and also keeps the last_node.next attr as None)

        b. prepend()
            - make new node instance
            - set the next attr of the head node == to new node
            - set the head == to new node

        c. insert()
            - make new node instance 
            - assign target node as self.head
            - iterate trough list node until node is == target location for the new node
            - set the next attr of new node == curent node.next
            - set curent node.next to new node
"""




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Prins list elements
    def print_list(self):
        cur_node = self.head

        while cur_node != None:
            print(cur_node.data)
            cur_node = cur_node.next

    # Insert element at the end of the list
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next
        last_node.next = new_node

    # Insert element at the begining of the list
    def prepend(self, data):
        new_node = Node(data)
        
        new_node.next = self.head
        self.head = new_node

    # Insert element after specific node
    def insert_after_node(self, target_node, data):
        new_node = Node(data)

        curent_node = self.head
        while curent_node.next != None:
            if curent_node.data == target_node:
                new_node.next = curent_node.next
                curent_node.next = new_node
                return

            curent_node = curent_node.next
        print(f'Location {target_node} does not exists in the list')

    # Delete head
    def del_head(self):
        self.head = self.head.next

    # Delete specific element
    def del_element(self, target_element):
        curent_node = self.head

        while curent_node.next != None:
            if curent_node.next.data == target_element:
                curent_node.next = curent_node.next.next
                return

            curent_node = curent_node.next

    # Delete list -- not working yet
    # def del_list(self):
    #     print(f'Deleted class {LinkedList.__name__}')
    #     del LinkedList.__name__
        

    # Delete n-th element
    def del_nth(self, element_position):
        curent_node = self.head

        counter = 0
        while curent_node.next != None:
            if counter+1 == element_position:
                curent_node.next = curent_node.next.next
                return 

            counter += 1
            if counter + 2 > element_position:
                print('List index out of range')
                return

            curent_node = curent_node.next


my_list = LinkedList()


my_list.append('1')
my_list.append('2')
my_list.append('3')
# my_list.append('3')

# my_list.del_head()
# my_list.del_element('2')
# my_list.del_nth(3)
# my_list.print_list()
# my_list.del_list()

my_list.print_list()

