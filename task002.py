



if __name__== '__main__':

    l1 = [10, 73, 10, 67, 40, 73, 50, 50, 67]
    def dupl_remover(l1):
        result = []
        for elem in l1:
            if elem not in result:
                result.append(elem)
        result.sort()
        return result


    print(dupl_remover(l1))












