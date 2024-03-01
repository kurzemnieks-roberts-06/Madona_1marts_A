def write_to_file(user_name):
    try:
        with open("lietotajs.txt", 'w') as file:
            file.write(user_name)
        print("Vārds veiksmīgi ierakstīts failā!")
    except Exception as e:
        print("Kļūda:", e)

user_name = input("Ievadiet savu vārdu: ")
write_to_file(user_name)