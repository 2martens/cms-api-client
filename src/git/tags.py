from subprocess import check_output

def create(name, comment=''):
    'Creates a tag with the given name and optionally comment'
    if (comment):
        check_output('git tag -m ' + comment + ' ' + name, shell=True)
    else:
        check_output('git tag ' + name, shell=True)

def remove(name):
    'Deletes a tag with the given name'
    check_output('git tag -d ' + name)
