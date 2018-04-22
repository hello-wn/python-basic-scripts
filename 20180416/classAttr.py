# -*- coding: utf-8 -*-:
class Student(object):
    count = 0 
    
    def __init__(self, name):
        self.__name = name
        Student.count += 1

s1 = Student('Alice')
print(s1.count)
s2 = Student('Ben')
print(s2.count)
