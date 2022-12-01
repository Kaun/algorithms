class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size_now = 0

    def size(self):
        return self.size_now

    def push(self, value):
        if self.size_now < self.max_size:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size_now += 1
            return True
        else:
            return None

    def pop(self):
        if self.size_now == 0:
            return None
        res = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size_now -= 1
        return res
    
    def pop_front(self):
        if self.size_now == 0:
            return None
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
            push = queu.push(int(value))
            if push is None:
                print('error')
        elif command == 'push_front':
            push = queu_front.push(int(value))
            if push == 'error':
                print('error')
        elif command == 'pop_back':
            r = queu.pop_front()
            if r is None:
                r = queu_front.pop()
            if r is None:
                print('error')
            else:
                print(r)
        elif command == 'pop_front':
            r = queu_front.pop_front()
            if r is None:
                r = queu.pop_front()
            if r is None:
                print('error')
            else:
                print(r)





if __name__ == '__main__':
    read_input()
    # test()