class rectangle:
    def __init__(self, h, w):
        self.height = h
        self.width = w

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height + self.width) * 2

    def draw(self):
        for i in range(self.height):
            print('* ' * self.width)


x = int(input('Enter Rectangle Height: '))
y = int(input('Enter Rectangle Width : '))
print()

a = rectangle(x, y)
print("Rectangle area      :", a.area())
print("Rectangle perimeter :", a.perimeter())
a.draw()
print()


class square(rectangle):
    def __init__(self, side):
        self.height = side
        self.width = side

    def draw(self):
        for i in range(self.height):
            print('* ' * self.height)


x = int(input('Enter Square Side Length: '))
print()

b = square(x)
print("Square area      :", b.area())
print("Square perimeter :", b.perimeter())
b.draw()
print()


class parallelogram(rectangle):
    def __init__(self, h, b):
        self.height = h
        self.width = b

    def perimeter(self):
        return 2 * (self.width + self.height * 1.4)

    def draw(self):
        for i in range(0, self.height):
            print(' ' * (self.height - i - 1) + '* ' * self.width)

    # def perimeter(self):
    #     super().perimeter(self)


h = int(input('Parallelogram Height : '))
t = int(input('Parallelogram Base   : '))
print()

p = parallelogram(h, t)

print('Parallelogram perimeter :', round(p.perimeter()))
print('Parallelogram area      :', p.area(), '\n')
p.draw()
print()


class isosceles_triangle(parallelogram):

    def area(self):
        return (self.height * self.width) * 0.5

    def perimeter(self):
        return self.width + (self.height * 1.4) * 2

    def draw(self):
        for i in range(self.height):
            print(' ' * int(i * 0.7) + '*' * self.width)


h = int(input('Triangle Height : '))
t = int(input('Triangle Base   : '))
print()

triangle = isosceles_triangle(h, t)

print('Isosceles Triangle perimeter :', round(triangle.perimeter()))
print('Isosceles Triangle area      :', round(triangle.area()))
triangle.draw()
print()
