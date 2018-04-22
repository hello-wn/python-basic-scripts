# -*- coding: utf-8 -*- 
class Animal(object):
    def run(self):
        print("Animals are running~")

class Dog(Animal):
    def run(self):
        print("Dogs are running~")

class Cat(Animal):
    def run(self):
        print("Cats are running~")

def run_twice(something):
    something.run()

run_twice(Dog())
run_twice(Cat())
run_twice(Animal())
