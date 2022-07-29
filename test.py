import requests
import json
from hello_world import db

def failed(num, msg):
    print(f'Challenge #{num} failed: {msg}')
    exit(1)

def passed(num):
    print(f'✓: Passed challenge #{num}')

if __name__ == "__main__":

    BASE_URL = 'http://127.0.0.1:3000'

    try:
        # Challenge 1
        result = requests.get(BASE_URL + '/hello')
        passed(1)
    except requests.exceptions.ConnectionError:
        failed(1, 'Connection to the API failed. Are you running the local dev server right now? (sam local start-api)')

    # Challenge 2
    result = requests.get(BASE_URL + '/hello')
    if not (result.status_code == 200 and json.loads(result.text) == "Hello, World!"):
        failed(2, 'The endpoint does not return the string "Hello, World!".')
    passed(2)

    # Challenge 3
    result = requests.get(BASE_URL + '/helloCustom', dict(name="Timmy"))
    if not (result.status_code == 200 and json.loads(result.text) == 'Hello, Timmy!'):
        failed(3, 'The endpoint does not return the string "Hello, Timmy!" when passed the query string parameter "name=Timmy"')
    passed(3)

    # Challenge 4
    result = requests.get(BASE_URL + '/getNames')
    if result.status_code != 200:
        failed(4, '/getNames failed (status code != 200)')
    names = json.loads(result.text)
    if not (names == [x for x in sorted(db.read_names(True)) if x]):
        failed(4, '/getNames is not returning the names in alphabetical order, or it is not removing the empty names')
    passed(4)

    # Challenge 5
    for name in ['Jamiroquai', '']:
        old_names = db.read_names(True)
        result = requests.post(BASE_URL + '/addName', json=dict(name=name))
        if result.status_code != 200:
            failed(5, f'/addName {name} failed (status code != 200)')
        if name and not (json.loads(result.text) == 'Success'):
            failed(5, f'Add name "{name}" did not add the data to the database or did not return "Success".')
        elif (not name) and (not json.loads(result.text) == 'Failure'):
            failed(5, f'Add name "{name}" did not return "Failure" when it should have.')
    passed(5)

    print("Congratulations! Your api passed.")
