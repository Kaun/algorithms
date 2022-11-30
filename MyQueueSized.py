'''
Тимофею нужно написать класс MyQueueSized, который принимает параметр max_size, означающий максимально допустимое количество элементов в очереди.

Помогите ему —– реализуйте программу, которая будет эмулировать работу такой очереди. Функции, которые надо поддержать, описаны в формате ввода.

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит 5000.
Во второй строке задан максимально допустимый размер очереди, он не превосходит 5000.
Далее идут команды по одной на строке. Команды могут быть следующих видов:

push(x) — добавить число x в очередь;
pop() — удалить число из очереди и вывести на печать;
peek() — напечатать первое число в очереди;
size() — вернуть размер очереди;
При превышении допустимого размера очереди нужно вывести «error». При вызове операций pop() или peek() для пустой очереди нужно вывести «None».
'''


class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size_now = 0

    def size(self):
        return self.size_now

    def peek(self):
        if self.size_now == 0:
            return None
        return self.queue[self.head]

    def push(self, value):
        if self.size_now < self.max_size:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size_now += 1
        else:
            return 'error'

    def pop(self):
        if self.size_now == 0:
            return None
        res = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size_now -= 1
        return res


def read_input():
    num_commands = int(input())
    size = int(input())
    queu = MyQueueSized(size)
    
    for i in range(num_commands):
        command_str = input().split()
        
        if len(command_str) == 2:
            command, value = command_str
        else:
            command = command_str[0]
            
        if command == 'push':
            push = queu.push(int(value))
            if push == 'error':
                print('error')
        if command == 'pop':
            r = queu.pop()
            if r is None:
                print('None')
            else:
                print(r)
        if command == 'size':
            print(queu.size())
        if command == 'peek':
            print(queu.peek())

if __name__ == '__main__':
    read_input()


# queu = MyQueueSized(5)
# queu.push(1)
# queu.push(2)
# queu.push(3)
# queu.push(4)
# queu.push(5)
# queu.push(6)
# queu.push(7)
# print(queu.pop())
# print(queu.pop())
# print(queu.pop())
# print(queu.pop())
# print(queu.pop())
# print(queu.pop())

