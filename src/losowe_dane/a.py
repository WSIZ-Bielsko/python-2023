from dataclasses import dataclass
from datetime import datetime

from faker import Faker


# fake = Faker(['it_IT', 'en_US', 'ja_JP', 'pl_PL'])

@dataclass
class Person:
    pesel: str
    name: str
    phone: str
    address: str

    @staticmethod
    def to_csv(person: 'Person') -> str:
        pass  # your code

    @staticmethod
    def from_csv(line: str) -> 'Person':
        pass  # your code

    """
    usage: 
    p = Person('01234012340', 'Karramba', '+123', 'Fakapowo 13')
    line = Person.to_csv(p)
    p2 = Person.from_csv(line)
    
    """


def gen_random_ppl(n: int) -> list[Person]:
    f = Faker(['pl_PL'])
    # for _ in range(n):
    #     print(f.name())
    #     print(f.address())
    #     print(f.phone_number())
    #     print(f.pesel())
    # print('----')
    ppl = []
    for _ in range(n):
        ppl.append(Person(f.pesel(), f.name(), f.phone_number(), f.address()))
    return ppl


def contains_str(p: Person, item: str) -> bool:
    d = p.__dict__
    for val in d.values():
        if item in val:
            return True
    return False


def ts() -> float:
    return datetime.now().timestamp()


if __name__ == '__main__':
    start_ts = ts()
    ppl = gen_random_ppl(10 ** 5)
    end_ts = ts()
    print(f'generating ppl took {end_ts - start_ts:.3f}s')
    start_ts = ts()
    for p in ppl:
        if contains_str(p, ','):
            print(f'damn, {p}')
    end_ts = ts()
    print(f'checking pp took {end_ts - start_ts:.3f}s')
