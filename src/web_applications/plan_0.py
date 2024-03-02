from dataclasses import dataclass
from datetime import time

import requests


@dataclass
class Lecture:
    przedmiotid: int
    nazwa: str
    active: bool


@dataclass
class Teacher:
    wykladowcaid: int
    sid: int
    imie: str
    nazwisko: str
    prefix: str
    suffix: str
    active: bool


"""
create table plan(
    group_id int,
    lecture_id int,
    room text,
    hour time,
    day_of_week text
);

"""


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


def login(album: str, password: str) -> str:
    pass


def get_plan() -> list[PlanItem]:
    plan = []
    plan.append(PlanItem(group_id=159, lecture_id=897, room="S23", hour=time(hour=13, minute=45), day_of_week='Sat'))
    plan.append(PlanItem(group_id=159, lecture_id=922, room="S12", hour=time(hour=12, minute=00), day_of_week='Sat'))
    plan.append(PlanItem(group_id=159, lecture_id=901, room="S12", hour=time(hour=12, minute=00), day_of_week='Sat'))
    return plan


def display_plan_for_group(group_id: int):
    TOKEN = '0bfcf58b-6e48-494a-9821-06930ce213da'
    plan = get_plan()
    teachers = get_teachers(TOKEN)
    lectures = get_lectures(TOKEN)
    # todo: use dict's to get nice verbose plan
    for p in plan:
        print(p)


if __name__ == '__main__':
    TOKEN = '0bfcf58b-6e48-494a-9821-06930ce213da'

    # todo: sort by name
    for nl in get_lectures(TOKEN):
        print(nl)

    for te in get_teachers(TOKEN):
        print(te)

    url = f'{WD_URL}/groups?active=true&wdauth={TOKEN}'
    res = requests.get(url)
    for g in res.json():
        print(g)
    # print(url)
    print('---------')
    display_plan_for_group(group_id=159)
