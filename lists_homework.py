
print ('\nvalues\n')

num1 = [2,4,8]
num2 = [3,9,27]
let1 = ['a', 'b', 'c']

l_all = num1 + num2 +let1

for n in num1 + num2 +let1:
    print(n)

print('\n*****\n')

for n in num1:
    print (n)
else:
    for m in num2:
        print(m)
    else:
        for o in let1:
         print(o)





print('\n*****\n')


for n in reversed(l_all):
    print(n)



print('\n*****\n')


for n in reversed(num1 + num2 +let1):
    print(n)

print('\n*****\n')


for n in l_all:
    print(n)
print('\none line\n')





print ('\none line\n')



print (*l_all)

#print('\nlength\n')

#print (len(l_all))

#print()

#print('\nzipped\n')

#for a,b in zip (num1, num2):
    #print(a)
   # print(b)


