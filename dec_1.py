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

    def push(self, value):
        if self.size_now < self.max_size:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size_now += 1
            return self.tail - 1
        return None

    def pop(self, index=0):
        if self.size_now == 0:
            return None
        if index != 0:
            res = self.queue[index]
            self.queue[index] = None
            self.tail = index
            self.size_now -= 1
            return res
        else:
            print('sss')
            res = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.size_now -= 1
            return res


def read_input():
    num_commands = int(input())
    size = int(input())
    queu = MyQueueSized(size)
    head = MyQueueSized(size)
    
    for i in range(num_commands):
        command_str = input().split()
        
        if len(command_str) == 2:
            command, value = command_str
        else:
            command = command_str[0]
            
        if command == 'push_back' or command == 'push_front':
            index = queu.push(int(value))
            if index is None:
                print('error')
            else:
                head.push(index)
        elif command == 'pop_back':
            index = head.pop()
            if index is None:
                print('error')
            else:
                print(queu.pop(index))
        elif command == 'pop_front':
            index = head.pop(head.tail-1)
            if index is None:
                print('error')
            else:
                print(queu.pop(index))
        


if __name__ == '__main__':
    read_input()


