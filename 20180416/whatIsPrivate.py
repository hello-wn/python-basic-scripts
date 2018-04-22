# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        if self.__gender in ['female', 'male', 'middlesex'] :
            return self.__gender

bart = Student('Bart', 'male')
bart.set_gender('middlesex')
print(bart.get_gender())
