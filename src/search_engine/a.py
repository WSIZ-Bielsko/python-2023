from dataclasses import dataclass


@dataclass
class Person:
    # definicja klasy Person
    name: str
    age: int
    temperature: float


p1 = Person(name='John', age=30, temperature=36.7)  # instancje klasy Person
p2 = Person(name='Will', age=17, temperature=37.2)

print(p1)
print(p2)
print(type(p1))  # <class '__main__.Person'>

print(p1.name)  # dostęp do pól instancji
print(p2.name)

p1.name = 'Johnny'
print(p1)

persons = [p1, p2, p2]
print(persons)

for p in persons:
    print('--> ', p)