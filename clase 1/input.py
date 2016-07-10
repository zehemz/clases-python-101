name = str(input("ingrese su nombre:\n"))
print(name)

#  File "python0101.py", line 1, in <module>
#    name = str(input("ingrese su nombre"))
#  File "<string>", line 1, in <module>
#NameError: name '' is not defined

#On Python 2.x you need to be using raw_input() rather than input(). On the older version of Python, input() actually evaluates what you type as a Python expression, which is why you need the quotes (as you would if you were writing the string in a Python program).
#There are many differences between Python 3.x and Python 2.x; this is just one of them. However, you could work around this specific difference with code like this:
#try:
#    input = raw_input
#except NameError:
#    pass
# now input() does the job on either 2.x or 3.x
