#!/bin/python3
import sys
import os


alphaNum = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
key = 2
newPass = ''


passwd = input("Enter a password: ")

for character in passwd:
  if character in alphaNum:
    position = alphaNum.find(character)
    newPosition = (position + key) % 70
    newCharacter = alphaNum[newPosition]
    newPass += newCharacter
  
  
print('Encrypted Password:', newPass)