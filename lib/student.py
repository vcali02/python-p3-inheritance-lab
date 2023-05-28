#!/usr/bin/env python

from user import User


knowledge = []


class Student(User):
    knowledge = []

   # def __init__(self, knowledge):
     #   print("Student.__init__ called.")
     #   super().__init__(knowledge)
     #   self.knowledge
    
    def learn(self, knowledge):
        self.knowledge = knowledge
        
    #    self.knowledge.append(element)
    #    return self.knowledge
