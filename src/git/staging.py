from subprocess import check_output

def add(filename='.'):
    'Adds the given file to the staging index; by default recursively the whole directory'
    check_output('git add ' + filename, shell=True)

def remove(filename):
    'Marks the given file as removed in the staging index'
    check_output('git rm ' + filename, shell=True)

def reset_all():
    'Resets the complete staging index'
    check_output('git reset', shell=True)

def reset_file(filename):
    'Removes the given file from the staging index'
    check_output('git reset ' + filename, shell=True)
