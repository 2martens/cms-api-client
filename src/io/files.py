
def read_file(name):
	'Returns the content of the specified file'
	file = open(name, 'r', encoding='utf-8')
	return file.read(None)

def write_file(name, content):
	'Writes the content into the specified file (overwrites if file exists)'
	file = open(name, 'w', encoding='utf-8')
	file.write(content)

