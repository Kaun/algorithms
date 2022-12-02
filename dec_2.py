class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size_now = 0

    def push(self, value):
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.size_now += 1

    def pop(self):
        res = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size_now -= 1
        return res

    def pop_back(self):
        self.tail -= 1
        res = self.queue[self.tail]
        self.queue[self.tail] = None
        self.tail = self.tail % self.max_size
        self.size_now -= 1
        return res


def read_input():
    num_commands = int(input())
    size = int(input())
    queu = MyQueueSized(size)
    queu_front = MyQueueSized(size)

    for i in range(num_commands):
        command_str = input().split()

        if len(command_str) == 2:
            command, value = command_str
        else:
            command = command_str[0]

        if command == 'push_back':
            if queu.size_now + queu_front.size_now < queu.max_size:
                queu.push(int(value))
            else:
                print('error')
        elif command == 'push_front':
            if queu.size_now + queu_front.size_now < queu.max_size:
                queu_front.push(int(value))
            else:
                print('error')
        elif command == 'pop_back':
            if queu.size_now > 0:
                res = queu.pop_back()
            elif queu_front.size_now > 0:
                res = queu_front.pop()
            else:
                res = 'error'
            print(res)
        elif command == 'pop_front':
            if queu_front.size_now > 0:
                res = queu_front.pop_back()
            elif queu.size_now > 0:
                res = queu.pop()
            else:
                res = 'error'
            print(res)


if __name__ == '__main__':
    read_input()
