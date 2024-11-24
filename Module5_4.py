class House:
    houses_history = [] # аргумент переменная и как бы объект класса сюда добавляем экземпляры класса
# сюда мы соберем некий список из названий наших объектов (наших ЖК)

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)
# что важно помнить в методе __new__: в *args попадут позиционные параметры, т. е в нашем случае это значания
# name и number_of_floors, поэтому чтобы в список собрать только названия наших жилых комплексов, мы должны
# указать индекс ноль (args[0]) при использовании метода .append (этот метод позволяет добавлять значения в список)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

# этот метод будет удалять экземпляры, что мы укажем и при этом выводит строку
    def __del__(self):
        print(f'{self.name}   снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)


# Удаление объектов
del h2
del h3

print(House.houses_history)