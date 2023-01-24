import math
class triangle:
    def __init__(self, a, b):
            self.a = a
            self.b = b

    def hypotenuse(self):
            return (math.sqrt (a**2 + b**2))

if __name__ == '__main__':
    a = input('Podaj przyprostokatna a trojkata! \n')
    b = input('Podaj przyprostokatna b  trojkata! \n')

    a = float(a)
    b = float(b)

    our_triangle = triangle(a,b)

    print (f'Przeciwprostokatna wynosi {our_triangle.hypotenuse()}')


