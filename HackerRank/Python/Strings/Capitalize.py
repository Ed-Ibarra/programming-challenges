"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalized correctly as Alison Heck.
        alison heck → Alison Heck
        
Given a full name, your task is to capitalize the name appropriately.

/

Se le pide que se asegure de que el nombre y apellido de las personas comiencen con una letra mayúscula en sus pasaportes. Por ejemplo, alison heck debe escribirse correctamente en mayúsculas como Alison Heck.
        Alison Heck → Alison Heck
        
Dado un nombre completo, su tarea es poner el nombre en mayúsculas correctamente.

--------------------------------------------------------------------------------
* Sample Input
chris alan

? Sample Output
Chris Alan
--------------------------------------------------------------------------------
! Explanation: Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

"""
def func(s):
    # Split whole input and use "replace" tool in the first letter to change it by itself but capitalized
    for x in s.split():
        s = s.replace(x, x.capitalize())
    return s

if __name__ == '__main__':
    result = func(input())
    print(result)