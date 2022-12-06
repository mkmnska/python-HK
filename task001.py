

l1 = ['abc', 'pqr', 'ege', '5665', 'cc']

def string_list_checker(l1):
    res = 0
    for string in l1:
        if len(string) > 2:
            if string[0] == string[-1]:
                res += 1
    return res




if __name__== '__main__':

    print(string_list_checker(l1))




