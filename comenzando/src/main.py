'''
Created on 9 jul. 2016

@author: Lucas
'''
if __name__ == '__main__':
    #name = str(input("What is your name: "))
    name = str(raw_input("What is your name: "))
    age = int(raw_input("How old are you: "))
    year = str((2014 - age)+100)
    print(name + " will be 100 years old in the year " + year)