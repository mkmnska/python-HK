



if __name__== '__main__':

    l1 =  [0, 45, 89, 'wlazl_kotek']
    l2 = ['na_plotek', 89, 'i_mruga']
    l3 = ['zaspiewaj', 966]
    l4 = ['piosenka_niedluga', 1410]

    def list_overlap_checker(l1,l2):
        for elem in l1:
            if elem in l2:
                return True
        return False


    print(list_overlap_checker(l3,l4))












