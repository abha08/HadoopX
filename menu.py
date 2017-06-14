#! /usr/bin/python

import os,time,commands,sys,socket

options="""
press 1 to setup Hadoop Cluster :
press 2 to setup MR :
press 3 to setup HIVE:
"""
print options

#Taking input for user choice

ch=raw_input()

if ch == '1':
	print "Hey! Let's Do the setup..Follow Me!!"
	execfile('hdfs_setup.py')

elif ch == '2':
	print "Make sure you have enough amount of CPU cores"
	execfile('mr_setup.py')

elif ch == '3':
	print "Starting your setup for HIVE"
	execfile('hive_setup.py')

else:
	print "Please read the Instructions again"
	execfile('start.py')
 
