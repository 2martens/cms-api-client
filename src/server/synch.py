from server import requests
from urllib.parse import urlencode

def check_update(domain, resource, apikey):
    'Returns true, if changes occured on the server side'
    # sends timestamp, server checks if changes have occured since then
    data = requests.build_api_data(apikey)
    data['action'] = 'check'
    response = requests.send(domain, resource, 'post', urlencode(data))
    body = response.read()
    return (body == 'yes')

def download_update(domain, resource, apikey):
    'Downloads the update data'
    data = requests.build_api_data(apikey)
    data['action'] = 'download'
    response = requests.send(domain, resource, 'post', urlencode(data))
    # response body contains the updated content texts, categories, etc, 
    # in an associative array/dictionary that is encoded (JSON, ...)
    body = response.read()
    return body

def upload_update(domain, resource, apikey, updateData):
    'Uploads the updated data'
    data = requests.build_api_data(apikey)
    data['data'] = updateData
    data['action'] = 'upload'
    response = requests.send(domain, resource, 'post', urlencode(data))
