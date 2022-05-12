# -*- coding: utf-8 -*-
"""
Created on Thu May 12 12:06:15 2022

@author: Killshot
"""
def unique_list(lista):
    lista=list(set(lista))
    lista_po=[]
    for filtered in lista:
        if type(filtered) == int:
            if filtered<3:
                lista_po.append(filtered)
    return lista_po


lista=[1, 2,1,2,3,3,6,8,5,3, 'str']

lista_po=unique_list(lista)
print(lista_po)

#%%
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def make_older(self):
        self.age+=5
        

        
h1=Person('Patryk', 21)
print(h1.name, h1.age)
h1.make_older()

print(h1.name, h1.age)
