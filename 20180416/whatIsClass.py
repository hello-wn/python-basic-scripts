# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def get_gender(self):
        if self.gender == 'female':
            print(self.name + " is a girl")
        elif self.gender == 'male':
            print(self.name + " is a boy")
        else:
            print(self.name + " is a different kid")

lisa = Student('Lisa', 'female')
joyce = Student('Joyce', 'middlesex')
joey = Student('Joey', 'male')

lisa.get_gender()
joyce.get_gender()
joey.get_gender()
