import json

def read_json_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print("Faila nav atrasts!")
    except Exception as e:
        print("Kļūda:", e)

file_name = input("Ievadiet JSON faila nosaukumu: ")
read_json_file(file_name)