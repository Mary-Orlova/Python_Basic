import requests
import json


result = requests.get('https://breakingbadapi.com/api/deaths')
if result.status_code == 200:
    json_dict = json.loads(result.text)  # десериализация
    max_death = 0

    for elem in json_dict:
        if elem['number_of_deaths'] > max_death:
            max_death = elem['number_of_deaths']
    for elem in json_dict:
        if elem['number_of_deaths'] == max_death:
            with open('max_death.json', 'w') as file:
                json.dump(elem, file, indent=4)  # серилизация JSON
    with open('max_death.json', 'r') as file:
        json_dict = json.load(file)
    for elem in json_dict:
        print(elem, ':', json_dict[elem])
