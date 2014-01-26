from subprocess import check_output

def create(name, base):
    'Creates a branch branching off of base'
    check_output('git checkout ' + base, shell=True)
    check_output('git checkout -b ' + name, shell=True)

def checkout(name):
    'Checkout branch name'
    check_output('git checkout ' + name, shell=True)

def remove(name):
    'Removes a branch from the repository'
    check_output('git branch -d ' + name, shell=True)

def merge(base, head):
    'Merges branch head into base'
    branches.checkout_branch(base)
    check_output('git merge --no-ff ' + head, shell=True)
