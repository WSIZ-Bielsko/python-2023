from dataclasses import dataclass
from datetime import time, date

import requests


@dataclass
class Lecture:
    przedmiotid: int
    nazwa: str
    active: bool = True


@dataclass
class Teacher:
    wykladowcaid: int
    imie: str
    nazwisko: str
    sid: int = -1
    prefix: str = ''
    suffix: str = ''
    active: bool = True


@dataclass
class Group:
    grupaid: int
    nazwa: str
    opis: str
    active: bool
    oldgrupaid: int
    studiastop: date


@dataclass
class PlanItem:
    group_id: int
    lecture_id: int
    room: str
    hour: time
    day_of_week: str


WD_URL = 'https://wddata.wsi.edu.pl'


def get_lectures(token: str) -> list[Lecture]:
    url = f'{WD_URL}/lectures?active=true&wdauth={token}'
    res = requests.get(url)
    lectures = res.json()
    nice_lectures = [Lecture(**l) for l in lectures]
    return nice_lectures


def get_teachers(token: str) -> list[Teacher]:
    url = f'{WD_URL}/teachers?wdauth={token}'
    res = requests.get(url)
    teachers = res.json()
    teachers = [Teacher(**l) for l in teachers]
    return teachers


def get_groups(token: str) -> list[Group]:
    url = f'{WD_URL}/groups?active=True&wdauth={token}'
    res = requests.get(url)
    groups = res.json()
    groups = [Group(**l) for l in groups]
    return groups



def get_plan() -> list[PlanItem]:
    plan = []
    plan.append(PlanItem(group_id=159, lecture_id=897, room="S23", hour=time(hour=13, minute=45), day_of_week='Sat'))
    plan.append(PlanItem(group_id=159, lecture_id=922, room="S12", hour=time(hour=12, minute=00), day_of_week='Sat'))
    plan.append(PlanItem(group_id=159, lecture_id=901, room="S12", hour=time(hour=12, minute=00), day_of_week='Sat'))
    return plan


# def display_plan_for_group(group_id: int):
#     TOKEN = '0bfcf58b-6e48-494a-9821-06930ce213da'
#     plan = get_plan()
#     teachers = get_teachers(TOKEN)
#     lectures = get_lectures(TOKEN)
#     # todo: use dict's to get nice verbose plan
#     for p in plan:
#         print(p)




if __name__ == '__main__':
    TOKEN = "864b0e72-0a93-4b74-a469-984225627217"

    # todo: sort by name
    for nl in get_lectures(TOKEN):
        print(nl)

    for te in get_teachers(TOKEN):
        print(te)

    for gr in get_groups(TOKEN):
        print(gr)

    print('---------')
    # display_plan_for_group(group_id=159)
