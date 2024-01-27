from dataclasses import dataclass

import requests


@dataclass
class ToDo:
    userId: int
    id: int
    title: str
    completed: bool


def fetch_todo_list(url: str) -> list[dict]:
    res = requests.get(url)

    todos = res.json()  # list[dict]
    # for t in todos:
    # print(t)
    # print(type(t))
    # print(t['userId'], t['id'], t['title'], t['completed'])  # to już są zmienne pythona (int, int, str, bool)
    # print(t)

    return todos


def convert_dict_to_todo(row: dict) -> ToDo:
    # return ToDo(....)
    # return ToDo(userId=10, id=5, title='abra kadabra', completed=False)
    return ToDo(userId=row['userId'], id=row['id'], title=row['title'], completed=row['completed'])


def get_todos_of_user(todos: list[ToDo], user_id: int) -> list[ToDo]:
    result = []
    for td in todos:
        if td.userId == user_id:
            result.append(td)
    return result


if __name__ == '__main__':
    tt = fetch_todo_list(url='https://jsonplaceholder.typicode.com/todos')
    todos = [convert_dict_to_todo(row) for row in tt]

    users = dict()
    for td in todos:
        users[td.userId] = 1
    # print(users.keys())  # mamy userów

    team_results = []
    for uid in users.keys():
        todos_of_user = get_todos_of_user(todos, uid)
        n_completed = sum([td.completed for td in todos_of_user])
        percentage = n_completed / len(todos_of_user)
        team_results.append([uid, percentage])

    for uid, percentage in team_results:
        print(f'User id={uid} wykonał: {percentage * 100:.2f}% zadań')

    # n_completed = 0
    # n_todos = 0
    # for t in todos:
    #     if t.userId == 6:
    #         n_todos += 1
    #         print(t)
    #         if t.completed:
    #             n_completed += 1
    #
    # print(f'Użytkownik nr 6 zakończył {n_completed} z {n_todos} zaplanowanych zadań')
