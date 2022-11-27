'''
Вася решает загадать число и удалить дело, которое идёт под этим номером. Список дел представлен в виде односвязного списка. Напишите функцию solution, которая принимает на вход голову списка и номер удаляемого дела и возвращает голову обновлённого списка.
'''

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item
            

def previous_value(node, index):
    while index - 1:
        node = node.next_item
        index -= 1
    return node


def solution(node, num_deleted):
    if num_deleted == 0:
        return node.next_item
    previous_node = previous_value(node, num_deleted)
    deleted_node = previous_node.next_item
    next_node = deleted_node.next_item
    previous_node.next_item = next_node
    return node

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3
    
    
if __name__ == '__main__':
    test()