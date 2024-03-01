def read_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Faila nav atrasts!")
    except Exception as e:
        print("Kļūda:", e)

file_name = input("Ievadiet teksta faila nosaukumu: ")
read_text_file(file_name)