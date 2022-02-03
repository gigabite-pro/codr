from modules import create
from modules import auth

prefix = 'codr'
commands = {
	'register': 'register - to create an account',
	'login': 'login - to login into your account',
	'create': 'create - to create a new project',
	'search': 'search - to search for old projects',
	'view': 'view - to view an old project',
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
	print('Please use the following commands with the prefix "codr" (codr <command>)\n')
	display_commands()

def display_commands():
	index = 1
	for i in commands:
		print(str(index) + '.', commands[i])
		index += 1
	print('\n')

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
				if command == 'quit':
					print('\nThank you for using codr!')
					break