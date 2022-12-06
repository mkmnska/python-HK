



if __name__== '__main__':

    content1 = [15, 'abcd', 42]
    content2 = [77, [1, 2, 3], {'haslo': 'Jozef Tkaczuk'}]



    def check_for_lists(content1):
        for elem in content1:
            if isinstance (elem, list):
                return True
        return False


    print(check_for_lists(content1))
    print (check_for_lists(content2))












