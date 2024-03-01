def read_file(file_name, file_format):
    try:
        if file_format == 'txt':
            read_text_file(file_name)
        elif file_format == 'csv':
            read_csv_column(file_name)
        elif file_format == 'json':
            read_json_file(file_name)
        else:
            print("Nepareizs faila formāts! Atbalstītie formāti ir: txt, csv, json")
    except Exception as e:
        print("Kļūda:", e)

file_name = input("Ievadiet faila nosaukumu: ")
file_format = input("Ievadiet faila formātu (txt, csv, json): ")
read_file(file_name, file_format)