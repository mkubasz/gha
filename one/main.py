import requests
from dotenv import dotenv_values
from pprint import pprint
config = dotenv_values(".env")


url = "https://api.github.com"
headers = {
  'Authorization': f'token {config["GITHUB_API_TOKEN"]}'
}
response = requests.get(url, headers=headers)
# pprint(response.json())
# /users
# GET /users
# [] + {nazwa_zasobu: /users/add/costam, jeden_user: /users/{id}}

# /orgs/{org}/repos


# Listowanie org

org = 'OrderOfDevsTutoring'
response = requests.get(f'{url}/orgs/{org}/repos', headers=headers)
#pprint(response.json())
# Tworzenie repo
payload = '{"name": "TaskOne"}'
response = requests.post(f'{url}/orgs/{org}/repos', headers=headers, data=payload)
pprint(response.json())

# Session

cache = {
  'current_repo_name': 'TaskOne'
}

# Session
# add file

# /repos/{owner}/{repo}/contents/{path}
# "path": "notes/hello.txt",
# path parameter
# message	string	body
# Required. The commit message.
# content	string	body
# Required. The new file content, using Base64 encoding.
import base64
import json
path = 'test_file.txt'
message = "initial commit"
base64_content = None
with open(path, "rb") as file:
  base64_content = base64.b64encode(file.read())
print(base64_content)


payload = {
  "content": base64_content.decode('utf-8'),
  "message": message
}
response = requests.put(
  f"{url}/repos/{org}/{cache['current_repo_name']}/contents/{path}",
  headers=headers, data=json.dumps(payload))
print(response.json())


## Add branch
