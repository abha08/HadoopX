#! /usr/bin/python

import os,time,commands,sys,socket

options="""
press 1 to manual setup hadoop cluster :
press 2 to automatic setup hadoop cluster :
"""
print options

ch=raw_input()

if ch == '1' :
	print "Follow the Rules Please!!"
	execfile('scan.py')

else :
	print "You might have Wrong Choice"
	execfile('menu.py') 
