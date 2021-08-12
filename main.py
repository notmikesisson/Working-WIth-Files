import os

if os.path.isfile("fileName.txt"): #check if file exists
 print('File Exists')

name = input("What is your name?: ")
address = input("What is your address?: ")
phoneNum = input("What is your phone number?: ")

with open('fileName.txt', 'w') as f:
  f.write(name + "," + address + "," + phoneNum)
  
with open('fileName.txt', 'r') as f:
  print(f.readline())

