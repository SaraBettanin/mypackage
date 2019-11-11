from mypackage import myfirstmodule
from mypackage import mysecondmodule

myfirstmodule.myfirstfunction()
mysecondmodule.mysecondfunction()

# Note that imports should be all done at the beginning of the file
# I place them in the middle to help you understand the different 
# import statements

from mypackage.myfirstmodule import myfirstfunction
myfirstfunction()

from mypackage.myfirstmodule import myfirstfunction as myf
myf()

#BAD PRACTICE!
from mypackage import *
myfirstmodule.myfirstfunction()
