import requests
import json

def post(url, data):
    jsonstr = json.dumps(data.__dict__)
    requisicao = requests.post(f'{url}/teste/.json', data=jsonstr)
    return requisicao