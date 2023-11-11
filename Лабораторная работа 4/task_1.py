import json


INPUT_FILE = 'input.json'


def task() -> float:
    with open(INPUT_FILE) as inp:
        json_data = json.load(inp)

    return round(sum([i['score'] * i['weight'] for i in json_data]), 3)


print(task())
