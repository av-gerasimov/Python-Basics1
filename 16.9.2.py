class Rectangle:
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth

    def get_area(self):
        return self.width * self.heigth


rectangle = Rectangle(50, 100)
print(f'Площадь прямоугольника:', rectangle.get_area())