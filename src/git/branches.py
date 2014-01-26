from subprocess import call

def create(name, base):
    'Creates a branch branching off of base'
    call('git checkout ' + base, shell=True)
    call('git checkout -b ' + name, shell=True)

def checkout(name):
    'Checkout branch name'
    call('git checkout ' + name, shell=True)

def remove(name):
    'Removes a branch from the repository'
    call('git branch -d ' + name, shell=True)

def merge(base, head):
    'Merges branch head into base'
    branches.checkout_branch(base)
    call('git merge --no-ff ' + head, shell=True)
