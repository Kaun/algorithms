# id 78673935
class Deque:
    def __init__(self, max_size):
        self.__queue = [None] * max_size
        self.__max_size = max_size
        self.__head = 0
        self.__tail = 0
        self.__size_now = 0

    def is_empty(self):
        return self.__size_now == 0

    def is_full(self):
        return self.__size_now == self.__max_size

    def push_front(self, value):
        if self.is_full():
            raise OverflowError("The deck is full!")
        self.__queue[self.__head-1] = value
        self.__head = (self.__head - 1) % self.__max_size
        self.__size_now += 1

    def push_back(self, value):
        if self.is_full():
            raise OverflowError("The deck is full!")
        self.__queue[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.__max_size
        self.__size_now += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError("The deck is empty!")
        res = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_size
        self.__size_now -= 1
        return res

    def pop_back(self):
        if self.is_empty():
            raise IndexError("The deck is empty!")
        self.__tail -= 1
        res = self.__queue[self.__tail]
        self.__queue[self.__tail] = None
        self.__tail = self.__tail % self.__max_size
        self.__size_now -= 1
        return res


def read_input():
    num_commands = int(input())
    size = int(input())
    queu = Deque(size)

    for _ in range(num_commands):
        command, *value = input().split()
        method = getattr(queu, command)
        try:
            res = method(*value)
        except (IndexError, OverflowError):
            res = 'error'
        if res is not None:
            print(res)


if __name__ == '__main__':
    read_input()
