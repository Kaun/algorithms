'''
Вася решает загадать число и удалить дело, которое идёт под этим номером. Список дел представлен в виде односвязного списка. Напишите функцию solution, которая принимает на вход голову списка и номер удаляемого дела и возвращает голову обновлённого списка.
'''

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def next_value(node, index):
    i = 0
    while i <= index + 1:
        if i == index + 1:
            return node
        i += 1
        if node.next_item is None:
            return node
        node = node.next_item

# def del_el(node, index):
#     next_el = 

def previous_value(node, index):
    while index - 1:
        node = node.next_item
        index -= 1
    return node
    

def solution_print(node):
    while node:
        print(node.value)
        node = node.next_item

def solution(node, num_deleted):
    if num_deleted == 0:
        return node.next_item
    previous_node = previous_value(node, num_deleted)
    deleted_node = previous_node.next_item
    next_node = deleted_node.next_item
    previous_node.next_item = next_node
    return node

def test():
    node4 = Node("node4")
    node3 = Node("node3", node4)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    res = solution(node0, 0)
    solution_print(res)
    

if __name__ == '__main__':
    test()