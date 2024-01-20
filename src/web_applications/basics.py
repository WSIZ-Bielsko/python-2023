import requests

res = requests.get(url='https://jsonplaceholder.typicode.com/todos')

print(res.status_code)
todos = res.json()
for t in todos:
    # print(t)
    # print(type(t))
    print(t['userId'], t['id'], t['title'], t['completed'])  # to już są zmienne pythona (int, int, str, bool)



