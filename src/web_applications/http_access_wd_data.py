import requests

from model import *

WD_URL = 'https://wddata.wsi.edu.pl'
TOKEN = "864b0e72-0a93-4b74-a469-984225627217"


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


def get_students(token: str) -> list[Student]:
    url = f'{WD_URL}/students?onlyactive=True&wdauth={token}'
    res = requests.get(url)
    if res.status_code != 200:
        print('błąd pobierania listy studentów')
        return []
    students = res.json()
    students = [Student(**item) for item in students]
    # sort by ??
    return students


def get_plan() -> list[PlanItem]:
    plan = []
    plan.append(PlanItem(group_id=159, lecture_id=897, room="S23", hour=time(hour=13, minute=45), day_of_week='Sat'))
    plan.append(PlanItem(group_id=159, lecture_id=922, room="S12", hour=time(hour=12, minute=00), day_of_week='Sat'))
    plan.append(PlanItem(group_id=159, lecture_id=901, room="S12", hour=time(hour=12, minute=00), day_of_week='Sat'))
    return plan


# todo: to be completed after some plans are generated
#
#
# def display_plan_for_group(group_id: int):
#     TOKEN = '0bfcf58b-6e48-494a-9821-06930ce213da'
#     plan = get_plan()
#     teachers = get_teachers(TOKEN)
#     lectures = get_lectures(TOKEN)
#     # todo: use dict's to get nice verbose plan
#     for p in plan:
#         print(p)


if __name__ == '__main__':

    # todo: sort by name
    for nl in get_lectures(TOKEN):
        print(nl)

    for te in get_teachers(TOKEN):
        print(te)

    for gr in get_groups(TOKEN):
        print(gr)
    #
    # for st in get_students(TOKEN):
    #     print(st)

    print('---------')
    # display_plan_for_group(group_id=159)
