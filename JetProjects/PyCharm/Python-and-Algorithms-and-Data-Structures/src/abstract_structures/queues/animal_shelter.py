#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "bt3"

'''A class for an animal shelter with two queues'''


class Node(object):
    def __init__(self, animalName=None, animalKind=None, pointer=None):
        self.animalName = animalName
        self.animalKind = animalKind
        self.pointer = pointer
        self.timestamp = 0


# 动物避难所
class AnimalShelter(object):
    def __init__(self):
        self.headCat = None
        self.headDog = None
        self.tailCat = None
        self.tailDog = None
        self.animalNumber = 0

    # enqueue any animal
    def enqueue(self, animalName, animalKind):
        self.animalNumber += 1
        newAnimal = Node(animalName, animalKind)
        newAnimal.timestamp = self.animalNumber

        if animalKind == 'cat':
            if not self.headCat:
                self.headCat = newAnimal  # head指向最早加入的Node
            if self.tailCat:
                self.tailCat.pointer = newAnimal  # 指针串接
            self.tailCat = newAnimal  # tail始终指向最晚加入的Node

        elif animalKind == 'dog':
            if not self.headDog:
                self.headDog = newAnimal
            if self.tailDog:
                self.tailDog.pointer = newAnimal
            self.tailDog = newAnimal

    # dequeue methods
    def dequeueDog(self):
        if self.headDog:
            newAnimal = self.headDog
            self.headDog = newAnimal.pointer  # head后移
            return str(newAnimal.animalName)
        else:
            return 'No Dogs!'

    def dequeueCat(self):
        if self.headCat:
            newAnimal = self.headCat
            self.headCat = newAnimal.pointer
            return str(newAnimal.animalName)
        else:
            return 'No Cats!'

    def dequeueAny(self):
        if self.headCat and not self.headDog:
            return self.dequeueCat()
        elif self.headDog and not self.headCat:
            return self.dequeueDog()
        elif self.headDog and self.headCat:
            if self.headDog.timestamp < self.headCat.timestamp:
                return self.dequeueDog()
            else:
                return self.dequeueCat()
        else:
            return 'No Animals!'

    def printAnimalShelter(self):
        print("Cats:")
        cat = self.headCat
        while cat:
            print(cat.animalName, cat.animalKind)
            cat = cat.pointer

        print("Dogs:")
        dog = self.headDog
        while dog:
            print(dog.animalName, dog.animalKind)
            dog = dog.pointer


if __name__ == '__main__':
    qs = AnimalShelter()
    qs.enqueue('bob', 'cat')
    qs.enqueue('mia', 'cat')
    qs.enqueue('yoda', 'dog')
    qs.enqueue('wolf', 'dog')
    qs.printAnimalShelter()

    print("Dequeue one dog and one cat...")
    qs.dequeueDog()
    qs.dequeueCat()
    qs.printAnimalShelter()
