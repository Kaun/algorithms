'''
Мама Васи хочет знать, что сын планирует делать и когда. Помогите ей: напишите функцию solution, определяющую индекс первого вхождения передаваемого ей на вход значения в связном списке, если значение присутствует.

Формат вывода
Функция возвращает индекс первого вхождения искомого элемента в список(индексация начинается с нуля). Если элемент не найден, нужно вернуть -1.
'''


LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, value):
    count = 0 
    while node:
        if node.value == value:
            return count
        node = node.next_item
        count += 1
    return -1


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node2")
    assert idx == 2      


if __name__ == '__main__':
    test()