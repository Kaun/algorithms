# id 77712944

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
        else:
            return 'error'

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
    input_list = input().split()
    size = len(input_list)
    queu = MyQueueSized(size)
    
    for i in input_list:
        if i in '+-*/':
            num1 = queu.pop_back()
            num2 = queu.pop_back()
            if i == '+':
                res = num2 + num1
            elif i == '-':
                res = num2 - num1
            elif i == '*':
                res = num2 * num1
            elif i == '/':
                res = num2 // num1
            queu.push(res)
        else:
            queu.push(int(i))
    return queu.pop_back()

if __name__ == '__main__':
    print(read_input())