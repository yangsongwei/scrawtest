import json

with open('json','r') as file:
    str=file.read()
js=json.loads(str)

with open('test.json','w') as file:
    file.write(json.dumps(js,indent=2))