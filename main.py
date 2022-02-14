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

def init():
	print(welcome_logo)
	print('\nWelcome to codr!\n')
	display_commands()

def init_auth():
	password = input('Root Password: ')
	if password == 'tswashere':
		print('\nLogged in as root!\n')
		init()
	else:
		print('\nIncorrect Password\n')
		init_auth()

def display_commands():
	print('\nPlease use the following commands with the prefix "codr" (codr <command>)\n')
	index = 1
	for i in commands:
		print(str(index) + '.', commands[i])
		index += 1
	print()

init_auth()

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