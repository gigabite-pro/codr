from modules import create, auth, view, search

prefix = 'codr'
commands = {
	'register': 'register - to create an account',
	'login': 'login - to login into your account',
	'create': 'create - to create a new project',
	'view': 'view - to view old projects',
	'search': 'search - to search for old projects',
	'help': 'help - to see the list of commands',
	'quit': 'quit - to quit the program'
}

# Structure for the project is as follows:
# main.py - main file with the menu-driven program that calls other modules and functions if the user chooses to do so
# modules folder - contains the modules files that are called by the main file
# modules/auth.py - contains the functions that authenticate the user and maintain the session
# modules/create.py - contains the functions to create a new project
# modules/view.py - contains the functions to view old projects
# modules/search.py - contains the functions to search for old projects
# auth.csv - stores the user data - username, password, and session
# projects.csv - stores the project data - project name, project description, and project date

file = open('auth.csv', 'a')
file.close()
logged_in = False


welcome_logo = '''
░█████╗░░█████╗░██████╗░██████╗░
██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║░░╚═╝██║░░██║██║░░██║██████╔╝
██║░░██╗██║░░██║██║░░██║██╔══██╗
╚█████╔╝╚█████╔╝██████╔╝██║░░██║
░╚════╝░░╚════╝░╚═════╝░╚═╝░░╚═╝'''

# Displays the menu
def display_menu():
	print(welcome_logo)
	print('\nWelcome to codr!\n')
	display_commands()

# Asks for the root password and then initializes the program
def init():
	password = input('Root Password: ')
	if password == 'csproject22':
		print('\nLogged in as root!\n')
		display_menu()
	else:
		print('\nIncorrect Password\n')
		init()

# Displays the list of commands
def display_commands():
	print('\nPlease use the following commands with the prefix "codr" (codr <command>)\n')
	index = 1
	for i in commands:
		print(str(index) + '.', commands[i])
		index += 1
	print()

init()

while True:
	any_input = input('> ')
	if type(any_input) == str:
		if any_input.startswith('codr '):
			command = any_input.split()[1]
			if command in commands.keys():
				if command == 'register':
					print()
					auth.register()
				if command == 'login':
					print()
					logged_in = auth.login()
				if command == 'create':
					if logged_in == True:
						create.create()
					else:
						print('\nPlease login to use this command.\n')
				if command == 'view':
					if logged_in == True:
						view.view()
					else:
						print('\nPlease login to use this command.\n')
				if command == 'search':
					if logged_in == True:
						search.search()
					else:
						print('\nPlease login to use this command.\n')
				if command == 'help':
					display_commands()
					print('If you have any further doubts, you can open an issue here: https://github.com/gigabite-pro/codr\n')
				if command == 'quit':
					print('\nThank you for using codr!\n')
					break