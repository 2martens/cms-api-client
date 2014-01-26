from subprocess import call

def add(filename='.'):
	'Adds the given file to the staging index; by default recursively the whole directory'
	call('git add ' + filename, shell=True)

def remove(filename):
	'Marks the given file as removed in the staging index'
	call('git rm ' + filename, shell=True)

def reset():
	'Resets the complete staging index'
	call('git reset', shell=True)

def reset(filename):
	'Removes the given file from the staging index'
	call('git reset ' + filename, shell=True)