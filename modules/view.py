import csv
import tabulate

def view():
    table = []
    with open('projects.csv', 'r') as projects:
        reader = csv.reader(projects)
        for row in reader:
            row[4] = row[4][:19]
            table.append(row)
    print()
    print(tabulate.tabulate(table, headers=['Name', 'Path', 'Tech Stack', 'Files','Date Created'], tablefmt='grid'))
    print()
    