import json

'''
{
    "three":{1, 2, 3},
    "one": 1,
    "two":2
}
'''




obj = {'one':1, 'two':2, 'three':[1, 2, 3]}
encoded = json.dumps(obj)
print(type(encoded))
print(encoded)
decoded = json.loads(encoded)
print(type(decoded))
print(decoded)