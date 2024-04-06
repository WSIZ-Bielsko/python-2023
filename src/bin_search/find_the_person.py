from faker import Faker


def gen_persons(count: int):
    fake = Faker(['pl_PL', 'en_US', 'fr_FR', ])
    w = []
    for _ in range(count):
        # print(fake.name())
        w.append(fake.name().lower())
    return w


def find_person_by_name(persons: list[str], name: str) -> str:
    # finds first person with name >= `name`
    if persons[0] >= name:
        return persons[0]
    b_min = 0   # osoba o imieniu napewno mniejszym od wymaganego
    b_max = len(persons)
    while True:
        b = (b_max + b_min) // 2
        print(f'{b_min=}, {b=}, {b_max=}')
        if persons[b] == name:
            return persons[b]
        if persons[b] < name:
            b_min = b
        else:
            b_max = b
        if b_max - b_min <= 1:
            break
    return persons[b]


if __name__ == '__main__':
    persons = gen_persons(10000)
    # persons = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    persons.sort()
    print(persons)
    print(find_person_by_name(persons, 'g'))
