def read_input():
    return input()


def is_correct_bracket_seq(str):
    stack = []
    if len(str) == 0:
        return True
    
    if len(str) == 1:
        return False
    
    for i in str:
        if i in ('[{('):
            stack.append(i)
        elif i in '])}':
            if stack:
                bracket_open = stack.pop()
                if bracket_open == '(' and i == ')':
                    continue
                elif bracket_open == '[' and i == ']':
                    continue
                elif bracket_open == '{' and i == '}':
                    continue
                else:
                    return False
            else:
                return False
    return len(stack) == 0
            
    
    
if __name__ == '__main__':
    read = read_input()
    print(is_correct_bracket_seq(read))
    