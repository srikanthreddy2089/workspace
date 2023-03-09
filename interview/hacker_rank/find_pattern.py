
def check_substring(i,j):
    if j in i:
        return True
    else:
        return False

def process(first, second):
    if '*' not in second:
        return check_substring(first,second)
    if second.startswith('*'):
        return check_substring(first[1:],second[1:])
    elif second.endswith('*'):
        return check_substring(first[:-1],second[:-1])
    else:
        while True:
            second_list = [x.strip() for x in second.split('*')]
            if check_substring(first,second_list[0]):
                index1 = first.index(second_list[0])
                first = first[index1+len(second_list[0]):]
                if first[1:].startswith(second_list[1]):
                    return True
            else:
                return False
        
if __name__ == '__main__':
    first = 'abcabcabcdef'
    second = 'z'
    print process(first, second)