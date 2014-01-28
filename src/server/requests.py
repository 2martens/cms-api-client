import http.client

def send(domain, resource, method, data):
	'Sends the request and returns the response object'
	connection = http.client.HTTPConnection(domain)
	connection.request(method.upper(), resource, data)
	return connection.getresponse()

def build_api_data(apikey):
    'Builds data for sending api request'
    configFile = open('last_sync', 'r', encoding='utf-8')
    timestamp = configFile.read()
    data = {'timestamp':timestamp, 'apikey':apikey}
    return data