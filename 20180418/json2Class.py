#-*- coding: utf-8 -*-
import json

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

def student2dict(std):
    return{
        'name': std.name,
        'age': std.age
    }

#object transfer to json string
s = Student('Ben', 23)
print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))

def dict2student(d):
    return Student(d['name'], d['age'])

#json str to object
json_str = '{"age": 30, "name": "Pooh"}'
print(json.loads(json_str, object_hook=dict2student))

