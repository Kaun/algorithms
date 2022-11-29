class StackBrackets:
    def __init__(self):
        self.opening_brack = []
        self.closing_brack = []
    
    def push_open(self, index, value):
        self.opening_brack.append((index, ord(value)))
        
    def push_close(self, index, value):
        self.closing_brack.append((index, ord(value)))
    
    def pop(self):
        return self.opening_brack.pop(), self.closing_brack.pop()
    
    def show(self):
        return self.opening_brack, self.closing_brack


def read_input():
    return input()


def is_correct_bracket_seq_old(str):
    if len(str) == 0:
        return True
    
    opening_brackets = []
    closing_brackets = []
    for i in str:
        if i in ('[', '{'):
            opening_brackets.append(ord(i)+2)
        elif i == '(':
            opening_brackets.append(ord(i)+1)
        else:
            closing_brackets.append(ord(i))
    
    print(opening_brackets)
    print(closing_brackets[::-1])
    return opening_brackets == closing_brackets[::-1]


def is_correct_bracket_seq(str):
    if len(str) == 0:
        return True
    
    if len(str) == 1:
        return False
    
    stack = StackBrackets()
    
    for i in range(len(str)):
        if str[i] in ('[', '{', '('):
            stack.push_open(i, str[i])
        else:
            stack.push_close(i, str[i])
            
    if len(stack.opening_brack) != len(stack.closing_brack):
        return False
    
    print(stack.opening_brack)
    print(stack.closing_brack)
    
    for i in range(len(stack.opening_brack)):
        opening, closing = stack.pop()
        if opening[0] > closing[0]:
            return False
        if closing[1] == opening[1] + 1 or closing[1] == opening[1] + 2:
            continue
        else:
            return False
    return True
    
    
if __name__ == '__main__':
    read = read_input()
    print(is_correct_bracket_seq(read))
    