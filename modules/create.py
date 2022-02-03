import requests
from time import sleep
from alive_progress import alive_bar
import os
import webbrowser

tech_stacks = {
	'node.js': 'krismuniz/minimal-starter',
	'svelte': 'sveltejs/template',
	'flask': 'seanpquig/dead-simple-flask-app' 
}

base_api_url = 'https://api.github.com'
base_content_api_url = 'https://raw.githubusercontent.com'


def compute():
    init = 0
    for i in range(100):
        sleep(0.01)
        yield

def create():
	print()
	print('Tech Stacks:\n> Node.js\n> Svelte\n> Flask\n')
	tech_stack = input('Enter tech stack for your project: ').lower()
	if tech_stack in tech_stacks.keys():
		project_name = input('Enter your project name: ')		
		
		root_path = os.path.join(os.getcwd().split('codr')[0], project_name)
		os.mkdir(root_path)
		
		r = requests.get(base_api_url + '/repos/' + tech_stacks[tech_stack] + '/contents')
		data = list(r.json())
		repo_structure = {}
		file_count = 0

		print('\nBuilding your project...')
		with alive_bar(100) as bar:
		    for i in compute():
		        bar()
		print()
		print('Finalizing...')
		print()

		for i in data:
		    if i['type'] == 'file':
		        repo_structure[i['name']] = i['download_url']
		        file_count += 1
		    elif i['type'] == 'dir':
		        repo_structure[i['name']] = {}
		        r = requests.get(i['url'])
		        dir_data = list(r.json())
		        for j in dir_data:
		            repo_structure[i['name']][j['name']] = j['download_url']
		            file_count += 1

		for i in repo_structure.keys():
			if type(repo_structure[i]) == str:
				r = requests.get(repo_structure[i])
				open(root_path + '/' + i, 'wb').write(r.content)
			else:
				new_path = os.path.join(root_path, i)
				os.mkdir(new_path)
				for j in repo_structure[i].keys():
					r = requests.get(repo_structure[i][j])
					open(new_path + '/' + j, 'wb').write(r.content)

		print(project_name, 'successfully built.')
		print('Path of project: ', root_path, '\n')
		webbrowser.open(root_path)
	else:
		print('\nWarning: Choose one from the given list.')
		create()
