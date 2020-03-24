
# Author : AL
# Usage  : python3 args_kwargs.py

#!/usr/bin/python3

import os, sys

# args
def test_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_args('yasoob', 'python', 'eggs', 'test')


# **kwargs
def test_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

kwargs={"arg3": 3, "arg2": "two", "arg1": 5}
test_kwargs(**kwargs)


# if you want to use all three of these in functions then the order is 
# some_func(fargs, *args, **kwargs)
def all_3args(fargs, *args, **kwargs):
	pass;			#define function body here


all_3args('fargs', 'args1', 'args2', 'args3', **kwargs)
