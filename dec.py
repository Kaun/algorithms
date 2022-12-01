class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size_now = 0

    def push_back(self, value):
        if self.size_now < self.max_size:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size_now += 1
        else:
            return 'error'

    def push_front(self, value):
        if self.size_now < self.max_size:
            self.queue.insert(0, value)
            self.head = 0
            self.tail = (self.tail + 1) % self.max_size
            self.size_now += 1
        else:
            return 'error'

    def pop_front(self):
        if self.size_now == 0:
            return 'error'
        res = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head - 1) % self.max_size
        self.size_now -= 1
        return res
    
    def pop_back(self):
        if self.size_now == 0:
            return 'error'
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
    
    for i in range(num_commands):
        command_str = input().split()
        
        if len(command_str) == 2:
            command, value = command_str
        else:
            command = command_str[0]
            
        if command == 'push_back':
            push = queu.push_back(int(value))
            if push == 'error':
                print('error')
        if command == 'push_front':
            push = queu.push_front(int(value))
            if push == 'error':
                print('error')
        if command == 'pop_front':
            r = queu.pop_front()
            if r == 'error':
                print('error')
            else:
                print(r)
        if command == 'pop_back':
            r = queu.pop_back()
            if r == 'error':
                print('error')
            else:
                print(r)


def test():
    queu = MyQueueSized(4)
    queu.push_back(10)
    queu.push_back(20)
    queu.push_back(30)
    queu.pop_front()
    queu.pop_back()


if __name__ == '__main__':
    read_input()
    # test()

