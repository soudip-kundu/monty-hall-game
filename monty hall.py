#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 00:00:19 2023

@author: soudip
"""
# MONTY HALL GAME
import random  
list1=[1,2,3]
a=random.choice(list1)
list1.remove(a)
b=int(input("choose a door between 1,2,3 :"))
if a!=b:
 list1.remove(b)
c=random.choice(list1)
print("the car is not under ",c)
g=input("do you want to change your option , if yes type y ") 
if g=='y':
    b=int(input("enter your new choice "))
else:
    b=b
if b==c:
        print("are you an idiot?")
if b==a:
 print("you have won a brand new car ! congrats ")
else:
    print("better luck next time.:) " )    
    