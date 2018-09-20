#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lesson6.1.py
#  
# 

filepath = input("Enter file name: ")
import os

filepath = os.path.join('/home/amirzohar/', filepath)
if not os.path.exists('/home/amirzohar/'):
    os.makedirs('/home/amirzohar/')
f = open(filepath, "a")

with open(filepath , 'a') as file:
	user_input=()
	while user_input != "":
		user_input=input("Write to file: ")
		file.write(user_input
		
	
