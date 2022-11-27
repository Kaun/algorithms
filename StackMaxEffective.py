class StackMax:
    def __init__(self):
        self.items = []
        self.max = []
    
    def pop(self):
        if len(self.items) != 0:
            self.items.pop()
            self.max.pop()
            return None
        return 'error'
            
    def push(self, item):
        self.items.append(item)
        if len(self.max) == 0:
            self.max.append(item)
        elif item > self.max[-1]:
            self.max.append(item)
        else:
            self.max.append(self.max[-1])
    
    def get_max(self):
        if len(self.items) != 0:
            return self.max[-1]
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