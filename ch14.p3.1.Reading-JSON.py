import json
a = '{"name":"Zophie","iscat":true,"micecaught":0}'   #JSON dictionary use true not True
b = json.loads(a)
print('Python from json:')
print(b)
#{'name': 'Zophie', 'iscat': True, 'micecaught': 0}
c = {"name":"Zophie","iscat":True,"micecaught":0} #py dictionary not json
d = json.dumps(c)
print('json from python:')
print(d)
#'{"name": "Zophie", "iscat": true, "micecaught": 0}'
