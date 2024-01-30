# Command-line Arguments
# Study documentation for sys
# use of sys.argv (argument vector)

import sys

print("hello, my name is", sys.argv[1]) 


# what is in sys.argv[0]? - the name of the program i.e; name.py

# Fix the sys.arg[1] problem
import sys 
try: 
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")

# Another way
import sys
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello my name is", sys.argv[1])


# Use of sys.exit
# To exit the program on the initiated line
    
import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello my name is", sys.argv[1])


# Use of slices

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)




    