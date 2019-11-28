from mypackage import myfirstmodule
from mypackage import mysecondmodule

myfirstmodule.myfirstfunction("ciao")
mysecondmodule.mysecondfunction()

# Note that imports should be all done at the beginning of the file
# I place them in the middle to help you understand the different
# import statements

from mypackage.myfirstmodule import myfirstfunction
myfirstfunction("ciao")

from mypackage.myfirstmodule import myfirstfunction as myf
myf("ciao")


birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}

def print_birthdays():
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    for name in birthdays:
        print(name)

def return_birthday(name):
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))