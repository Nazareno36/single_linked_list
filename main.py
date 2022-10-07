
from single_linked_list import SingleLinkedList as sL

linked_list = sL()
linked_list.unshift('E')
linked_list.unshift('D')
linked_list.unshift('C')
linked_list.unshift('B')
linked_list.update_value(1,'b')
linked_list.insert_node(1,'A')
linked_list.print_values()