from subprocess import check_output
from git import staging

def diff_head(output_form='string'):
    'Returns the output of a "git diff --cached --name-status" call.'
    staging.add()
    output = check_output('git diff --cached --name-status', shell=True, universal_newlines=True)
    staging.reset_all()

    if (output_form == 'string'):
        return output
    elif (output_form == 'list'):
        return output.splitlines()

def diff_compare(base, head, output_form='string'):
    'Returns the raw output of a "git diff --name-status base head" call'
    output = check_output('git diff --name-status ' + base + ' ' + head, shell=True, universal_newlines=True)

    if (output_form == 'string'):
        return output
    elif (output_form == 'list'):
        return output.splitlines()
