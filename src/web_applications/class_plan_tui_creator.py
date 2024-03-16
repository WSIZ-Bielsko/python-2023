from collections.abc import Callable

from model import *
from copy import deepcopy


def lecture_choice(lectures: list[Lecture], search_query: str) -> list[Lecture]:
    # zadanie: z listy `lectures` wybrac wszystkie takie, ktorych pole `nazwa` zawiera `search_query`;
    # posortowac po nazwie i zwrocić przez return
    matching_lectures = []

    for lec in lectures:
        if search_query.lower() in lec.nazwa.lower():
            matching_lectures.append(lec)

    matching_lectures.sort(key=lambda lec: lec.nazwa)
    return matching_lectures


def group_choice(groups: list[Group], search_query: str) -> list[Group]:
    matching = []
    for entity in groups:
        if search_query.lower() in entity.nazwa.lower() + entity.opis.lower():
            matching.append(entity)

    matching.sort(key=lambda lec: lec.nazwa)
    return matching


def teacher_choice(teachers: list[Teacher], search_query: str) -> list[Teacher]:
    """
    Funkcja z listy `teachers` wybiera wszystkich, których pole `nazwisko` i `imie` zawiera `search_query`;
    Znalezione obiekty są sortowane po `nazwisko`+`imie`.

    :param teachers: Lista przeszukiwanych obiektów
    :param search_query: Tekst szukany w każdym z obiektów
    :return: Obiekty spełniające reguły wyszukiwania
    """
    matching = []
    for lec in teachers:
        if search_query.lower() in (lec.nazwisko.lower() + lec.imie.lower()):
            matching.append(lec)

    matching.sort(key=lambda tea: lec.nazwisko + lec.imie)
    return matching


def entity_selector(entities: list, choice_restrictor: Callable[[list, str], list]) -> int:
    selected = deepcopy(entities)  # from copy import deepcopy
    while True:
        for item in selected:
            print(item)
        query = input('> ')
        if query.startswith('*'):
            print(f'Choice selected {query=}')
            return int(query[1:])
        else:
            selected = choice_restrictor(selected, query)


if __name__ == '__main__':
    l1 = Lecture(przedmiotid=111, nazwa='Technika cyfrowa')
    l2 = Lecture(przedmiotid=29, nazwa='Język angielski')
    l3 = Lecture(przedmiotid=17, nazwa='Grafika 2d')
    l4 = Lecture(przedmiotid=94, nazwa='Kompetencje interpersonalne')

    entities = [l1, l2, l3, l4]

    t1 = Teacher(wykladowcaid=6, imie='Abra', nazwisko='Weibo')
    t2 = Teacher(wykladowcaid=61, imie='Abra1', nazwisko='Kadabra')
    t3 = Teacher(wykladowcaid=16, imie='Abra2', nazwisko='Kadabra2')
    t4 = Teacher(wykladowcaid=66, imie='Abra3', nazwisko='Xiaoli')

    teachers = [t1, t2, t3, t4]

    g1 = Group(grupaid=12, nazwa='Grupa1', opis='Grupa osobowości indywidualnych', active=True, oldgrupaid=-1,
               studiastop=date(year=2026, month=3, day=31))
    g2 = Group(grupaid=24, nazwa='Grupa2', opis='Grupa indywidualności osobliwych', active=True, oldgrupaid=-1,
               studiastop=date(2027, 3, 31))

    groups = [g1, g2]

    print('------------')
    teacher_id = entity_selector(teachers, teacher_choice)
    print('------------')
    lecture_id = entity_selector(entities, lecture_choice)
    print('------------')
    grupa_id = entity_selector(groups, group_choice)
    print('------------')

