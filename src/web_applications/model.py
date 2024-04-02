from dataclasses import dataclass
from datetime import date, time


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
class Student:
    studentid: int
    album: str
    imie: str
    nazwisko: str

    datarejestracji: date
    active: bool | None
    comment: str | None

    # ignore the fields below
    star: bool
    finid: int
    email: str
    phone: str


@dataclass
class PlanItem:
    group_id: int
    lecture_id: int
    room: str
    hour: time
    day_of_week: str
