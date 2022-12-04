# id 78515436
class MyQueueSized:
    def __init__(self, max_size):
        self.__queue = [None] * max_size
        self.__max_size = max_size
        self.__size_now = 0

    operations = {'+': (lambda x, y: x + y),
                  '-': (lambda x, y: x - y),
                  '*': (lambda x, y: x * y),
                  '/': (lambda x, y: x // y),
                  }
    
    def push(self, value):
        if self.__size_now >= self.__max_size:
            raise OverflowError("The stack is full!")
        self.__queue[self.__size_now] = value
        self.__size_now += 1

    def pop_back(self):
        if self.__size_now == 0:
            raise IndexError("The stack is empty!")
        self.__size_now -= 1
        res = self.__queue[self.__size_now]
        self.__queue[self.__size_now] = None
        return res


def read_input():
    input_list = input().split()
    size = len(input_list)
    queu = MyQueueSized(size)

    for i in input_list:
        if i in '+-*/':
            num1 = queu.pop_back()
            num2 = queu.pop_back()
            func = queu.operations.get(i)
            queu.push(func(num2, num1))
        else:
            queu.push(int(i))
    return queu.pop_back()


if __name__ == '__main__':
    print(read_input())
