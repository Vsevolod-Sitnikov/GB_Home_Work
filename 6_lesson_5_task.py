class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print(f"Запуск отрисовки {self.title} при помощи ручки")


class Pencil(Stationery):

    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print(f"Запуск отрисовки {self.title} при помощи карандаша")

class Handle(Stationery):

    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print(f"Запуск отрисовки {self.title} при помощи маркера")

pen = Pen("листок")

pen.draw()
