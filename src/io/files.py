
def read_file(name, type='html', engine='twig'):
	'Returns the content of the specified file'
	file = open(name + '.' + type + '.' + engine, 'r', encoding='utf-8')
	return file.read(None)

def write_file(name, content, type='html', engine='twig'):
	'Writes the content into the specified file (overwrites if file exists)'
	file = open(name + '.' + type + '.' + engine, 'w', encoding='utf-8')
	file.write(content)

