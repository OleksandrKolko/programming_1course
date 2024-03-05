class Figure:

    def perimeter(self):
        pass

    def area(self):
        pass

    def exsists(self):
        pass


class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__()

        self.a = a
        self.b = b
        self.c = c

        if not self.exsists():
            raise ValueError(f"Фігури з такими параметрами не існує")

    def perimeter(self):


        return self.a + self.b + self.c


    def area(self):

        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


    def exsists(self):

        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a\
        and self.a > 0 and self.b > 0 and self.c > 0:
            return True
        else:
            return False

    def __repr__(self):

        return f"Triangle({self.a}, {self.b}, {self.c})"


class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__()

        self.a = a
        self.b = b

        if not self.exsists():
            raise ValueError(f"Фігури з такими параметрами не існує")

    def perimeter(self):

        return 2 * (self.a + self.b)


    def area(self):

        return self.a * self.b


    def exsists(self):

        if self.a > 0 and self.b > 0:
            return True
        else:
            return False

    def __repr__(self):

        return f"Rectangle({self.a}, {self.b})"


class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        super().__init__()

        self.a = a
        self.b = b
        self.c = c
        self.d = d

        if not self.exsists():
            raise ValueError(f"Фігури з такими параметрами не існує")

    def perimeter(self):

        return self.a + self.b + self.c + self.d


    def area(self):

        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c) * (p - self.d)) ** 0.5

    def exsists(self):

        if self.a > 0 and self.b > 0 and self.c > 0 and self.d > 0 and self.a != self.b \
            and self.a + self.b + self.c > self.d and self.a + self.d + self.c > self.b \
            and self.a + self.b + self.d > self.c and self.d + self.b + self.c > self.a:
            return True

        else:
            return False

    def __repr__(self):

        return f"Trapeze({self.a}, {self.b}, {self.c}, {self.d})"

class Parallelogram(Figure):

    def __init__(self, a, b, h):
        super().__init__()

        self.a = a
        self.b = b
        self.h = h

        if not self.exsists():
            raise ValueError(f"Фігури з такими параметрами не існує")

    def perimeter(self):

        return 2 * (self.a + self.b)


    def area(self):

        return self.b * self.h


    def exsists(self):

        if self.a > 0 and self.b > 0 and self.h > 0:
            return True
        else:
            return False

    def __repr__(self):

        return f"Parallelogram({self.a}, {self.b}, {self.h})"


class Circle(Figure):

    def __init__(self, r):
        super().__init__()

        self.r = r

        if not self.exsists():
            raise ValueError(f"Фігури з такими параметрами не існує")

    def perimeter(self):

        return 2 * 3.14 * self.r


    def area(self):

        return 3.14 * (self.r ** 2)


    def exsists(self):

        if self.r > 0:
            return True
        else:
            return False

    def __repr__(self):

        return f"Circle({self.r})"


shapes = {
    "Triangle" : Triangle,
    "Rectangle" : Rectangle,
    "Trapeze" : Trapeze,
    "Parallelogram" : Parallelogram,
    "Circle" : Circle
}


def figure_generator(line):
    name = line[0]
    parametrs = line[1:]
    shape = shapes[name]
    converted_params = []
    for param in parametrs:
        converted_params.append(int(param))

    return shape(*converted_params)

def max_perimeter(figures: list):
    max_per = {Triangle : 0,
               Rectangle : 0,
               Trapeze: 0,
               Parallelogram: 0,
               Circle: 0}

    for figure in figures:
        if figure.perimeter() > max_per[type(figure)]:
            max_per[type(figure)] = figure.perimeter()

    return max(max_per.values())

def max_area(figures: list):
    max_ar = {Triangle : 0,
               Rectangle : 0,
               Trapeze: 0,
               Parallelogram: 0,
               Circle: 0}

    for figure in figures:
        if figure.area() > max_ar[type(figure)]:
            max_ar[type(figure)] = figure.area()

    return max(max_ar.values())



if __name__ == "__main__":
    figures = []
    with open ("C:\\Users\\ASUS\\Downloads\\input03.txt", 'r') as file:
        for line in file:
            try:
                figures.append(figure_generator(line.split()))
            except ValueError:
                pass

    print(max_perimeter(figures))
    print(max_area(figures))