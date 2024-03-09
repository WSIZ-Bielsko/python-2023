from plan_0 import Lecture, Teacher
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


def teacher_choice(teachers: list[Teacher], search_query: str) -> list[Teacher]:
    matching = []
    for lec in teachers:
        if search_query.lower() in (lec.nazwisko.lower() + lec.imie.lower()):
            matching.append(lec)

    matching.sort(key=lambda tea: lec.nazwisko + lec.imie)
    return matching


if __name__ == '__main__':
    l1 = Lecture(przedmiotid=111, nazwa='Technika cyfrowa')
    l2 = Lecture(przedmiotid=29, nazwa='Język angielski')
    l3 = Lecture(przedmiotid=17, nazwa='Grafika 2d')
    l4 = Lecture(przedmiotid=94, nazwa='Kompetencje interpersonalne')

    lectures = [l1, l2, l3, l4]

    t1 = Teacher(wykladowcaid=6, imie='Abra', nazwisko='Kadabra')
    t2 = Teacher(wykladowcaid=61, imie='Abra1', nazwisko='Kadabra1')
    t3 = Teacher(wykladowcaid=16, imie='Abra2', nazwisko='Kadabra2')
    t4 = Teacher(wykladowcaid=66, imie='Abra3', nazwisko='Kadabra')

    teachers = [t1, t2, t3, t4]

    # print(lectures)
    #
    # gg = lectures
    # print(gg)
    # gg[0].nazwa = 'XXX'
    #
    # print(gg)
    # print(lectures)
    #
    # print(id(lectures))
    # print(id(gg))  # jeśli id są te same, to oba obiekty są tym samym obiektem (~ alias)
    #
    # zz = [lec for lec in lectures]
    # zz[0].nazwa = 'ZZZZZZ'
    # print(id(zz))
    # zz.append('--------')
    # print(zz)
    # print(lectures)

    selected = deepcopy(lectures)  # from copy import deepcopy

    # selected[1].nazwa = 'SSSSSSSSSS'
    # print(lectures)
    # print(selected)

    while True:
        for lct in selected:
            print(lct)
        query = input('> ')
        if query.startswith('*'):
            print(f'Choice selected {query=}')
            break
        else:
            selected = lecture_choice(selected, query)

    selected = deepcopy(teachers)
    while True:
        for lct in selected:
            print(lct)
        query = input('> ')
        if query.startswith('*'):
            print(f'Choice selected {query=}')
            break
        else:
            selected = teacher_choice(selected, query)
