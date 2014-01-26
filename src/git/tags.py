from subprocess import call

def create_tag(name, comment=''):
	'Creates a tag with the given name and optionally comment'
	if (comment):
		call('git tag -m ' + comment + ' ' + name, shell=True)
	else:
		call('git tag ' + name, shell=True)

def delete_tag(name):
	'Deletes a tag with the given name'
	call('git tag -d ' + name)