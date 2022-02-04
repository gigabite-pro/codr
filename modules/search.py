import csv
import tabulate
import webbrowser

table = []

def open_file():
    open_index = input('\nEnter the index of the project you want to open: ')
    if open_index.isdigit():
        if int(open_index) <= len(table):
            webbrowser.open(table[int(open_index)-1][2])
            print('\nOpened Project :)\n')
            table.clear()
        else:
            print('\nIndex out of range.\n')
            open_file()
    else:
        print('\nInvalid index.\n')
        open_file()

def search():
    try:
        counter = 1
        print()
        query = input('Search query: ')
        with open('projects.csv', 'r') as projects:
            reader = csv.reader(projects)
            for row in reader:
                if query in row[0]:
                    row.insert(0, counter)
                    counter += 1
                    table.append(row)
        print()
        print(tabulate.tabulate(table, headers=['Index','Name', 'Path', 'Tech Stack', 'Files','Date Created'], tablefmt='grid'))
        file_input = input('\nDo you want to open any project? (y/n): ')
        if file_input.lower() == 'y':
            open_file()
        else:
            table.clear()
    except FileNotFoundError:
        print('\nNo projects to search.\n')