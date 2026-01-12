letter = '''Hello ABC
your age is years
Greeting from abc company.
date : DATE
'''

name = input("Enter your name : ")
age = input("Enter age : ")
date = input("Enter date : ")
letter = letter.replace("ABC",name)
letter = letter.replace("years",age)
letter = letter.replace("DATE",date)
print("-----------")
print(letter)
