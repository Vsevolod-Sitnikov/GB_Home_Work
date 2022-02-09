class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print("Запуск отрисовки при помощи ручки")


class Pencil(Stationery):

    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print("Запуск отрисовки при помощи карандаша")

class Handle(Stationery):

    def __init__(self, title):
        Stationery.__init__(self, title)

    def draw(self):
        print("Запуск отрисовки при помощи маркера")
