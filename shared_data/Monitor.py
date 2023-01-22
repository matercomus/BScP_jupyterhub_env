# This script is an intro into the Knowledge Engine REST Developer API
# see https://gitlab.inesctec.pt/interconnect-public/knowledge-engine/-/blob/main/openapi-sc.yaml

import httpx
import json
import re

# function for preety printing JSON
def print_json(json_string):
    print(json.dumps(json.loads(json_string), indent=4))

# function for preety printing RDF
def displayRDFString(string):
    return re.sub(r'(\.\s)', r'\1\n', string)

# set the URL
URL = "https://ke.interconnectproject.eu/rest/"

# GET request /sc - Either get all available Smart Connectors or a specific one if the Knowledge-Base-Id is provided.
headers = {
    'accept': 'application/json; charset=UTF-8',
    'Knowledge-Base-Id': '',
}
# r = httpx.get(URL + "sc", headers=headers)

# GET request /sc/ki - Get all KnowledgeInteractions for a given Knowledge-Base-Id
headers = {
    'accept': 'application/json; charset=UTF-8',
    'Knowledge-Base-Id': 'https://ke.interconnectproject.eu/adapter/evtd-kb',
}
r = httpx.get(URL + "sc/ki", headers=headers)

# print the response
print_json(r.text)

# print the first argumentGraphPattern
print('argumentGraphPattern\n')
argumentGraphPattern = json.loads(r.text)[0]['argumentGraphPattern']
print(displayRDFString(argumentGraphPattern))

print()

# print the first resultGraphPattern
print('resultGraphPattern\n')
resultGraphPattern = json.loads(r.text)[0]['resultGraphPattern']
print(displayRDFString(resultGraphPattern))
