import json

test = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}], sort_keys=True, indent=4)
print(test)
print(test[0])

data = json.loads(test)
print(data)
print(data[0])
print(data[1])
print(data[1]['bar'])