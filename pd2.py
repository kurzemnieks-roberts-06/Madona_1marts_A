import csv

def read_csv_column(file_name):
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 4:
                    print(row[3])
    except FileNotFoundError:
        print("Faila nav atrasts!")
    except Exception as e:
        print("Kļūda:", e)

file_name = input("Ievadiet CSV faila nosaukumu: ")
read_csv_column(file_name)