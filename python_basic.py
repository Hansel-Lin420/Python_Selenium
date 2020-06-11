# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 22:32:35 2020

@author: ASUS
"""

name = "tom"
height = 190.395
reverse =""

print("%s , %0.2f"%(name,height))
print("{0} , {1}".format(name,height))
'''
if
'''
print("-----if-----")

score= (int)(input ('請輸入成績:'))

if score >=90 :
    print("優秀")
elif score >=70:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
    '''
for
'''
print("-----for-----")
for s in "hello":
    print(s)
fruits = ['banana','apple','mango']

for fruit in fruits:
    print(fruit)
for i in range(1,10,2):
    print(i)
'''
列表
'''
print("-----列表-----")
lists = [1,2,3,'a',5]
list1=[1,2,3]
list2=[4,5]
print(lists[0])
print(lists[-1])
lists[4] = 'b'
print(lists)
lists.append('c')
print(lists)
lists.pop(0)
print(lists)
list3=list1+list2
print(list3)
'''
元組
'''
print("-----元組-----")
tup1=('a','b',3,4)
tup2=(1,2,3)
print(tup1[0])
print(tup2[0:2])
tup3=tup1+tup2
print(tup3)
tup4 = ('Hi!')
print(tup4*3)
'''
字典
'''
print("-----字典-----")

dict1 ={"username":"Hansel Lin","password":12345}
print(dict1.keys())
print(dict1.values())
dict1["age"] = 22
for k,v in dict1.items():
    print("dict1 keys is %r"%k)
    print("dict1 values is %r"%v)
dict1.pop("password")
print(dict1.items())
'''
函數
'''
print("-----函數-----")
def add(a,b):
    print(a+b)
add(3,5)

def add(a,b):
    return(a+b)
c=add(3,5)
print(c)

def add(a=1,b=2):
    return a+b
c1 = add()
c2 = add(3,5)
print(c1)
print(c2)
'''
物件
'''
print("-----物件-----")
class Myclass:
    
    def say_hello(self, name):
        return "hello, "+name
mc=Myclass()
print(mc.say_hello("tom"))

class Animal():
 def __init__(self, name):
  self.name = name
a = Animal("dog") 
print(a.name)

class A:
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
    
    def add(self):
        return self.a + self.b
count = A("4",5)
print(count.add())

class B(A):
    
    def sub(self):
        
        return self.a - self.b
print(B(2,3).add())
print(B(2,3).sub())

class C:
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
    
    def mult(self):
        return self.a * self.b
count = C(4,5)
print(count.mult())
'''
模組
'''
import time

print(time.ctime())

from time import ctime
print(ctime())

from time import time, sleep

from time import *

print(ctime())
print("休眠兩秒")
sleep(2)
print(ctime())
