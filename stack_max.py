'''
Нужно реализовать класс StackMax, который поддерживает операцию определения максимума среди всех элементов в стеке. Класс должен поддерживать операции push(x), где x – целое число, pop() и get_max().

Формат ввода
В первой строке записано одно число n — количество команд, которое не превосходит 10000. В следующих n строках идут команды. Команды могут быть следующих видов:

push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max() нужно напечатать «None», для команды pop() — «error».

Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения. Если стек пустой, для команды get_max() напечатайте «None». Если происходит удаление из пустого стека — напечатайте «error».
'''


class StackMax:
    def __init__(self):
        self.items = []
    
    def pop(self):
        if len(self.items) != 0:
            self.items.pop()
            return None
        return 'error'
            
    def push(self, item):
        self.items.append(item)
    
    def get_max(self):
        if len(self.items) != 0:
            return max(self.items)
        return None


def read_input():
    stack = StackMax()
    num_commands = int(input())
    
    for i in range(num_commands):
        command_str = input().split()
        
        if len(command_str) == 2:
            command, value = command_str
        else:
            command = command_str[0]
            
        if command == 'push':
            stack.push(int(value))
        if command == 'pop':
            r = stack.pop()
            if r == 'error':
                print('error')
        if command == 'get_max':
            print(stack.get_max())

if __name__ == '__main__':
    read_input()