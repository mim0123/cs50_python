import cowsay
import sys

if len (sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1]) # THis will print out a cow
    cowsay.cow("hello, " + sys.argv[1])  # This will print out a trex