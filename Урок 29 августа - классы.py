class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age



den = Human('Денис', 20)
print(den.name, den.age)
max = Human('Максим', 21)
sem = Human('Семен', 23)
den.age = 77
print('Нов. возраст ', den.name, den.age)
den.surname = 'Сидоренко'
#print(id(den), id(max))
#print(den.name, den.age)
print(max.name, max.age)
print(sem.name, sem.age)
print(den.surname)