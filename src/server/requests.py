import http.client

def send_request(domain, resource, method, data):
	'Sends the request and returns the response object'
	connection = http.client.HTTPConnection(domain)
	connection.request(method, resource, data)
	return connection.getresponse()

