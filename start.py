#! /usr/bin/python

#Including packages which can be used
import os,commands,time,sys,socket,getpass

os.system("echo 'Welcome,You are in Hadoop Hulk' | festival --tts")
time.sleep(1)

print 'Welcome,You are in Hadoop Hulk'
print "_*_*_*_*_*_*_*_*_*_*_*_*"

#To make system wait for 2 sec
time.sleep(2)

#Taking input for username and password
user_name=raw_input("Enter your UserName:")
passwd=getpass.getpass()

#check if given username password are correct
if user_name == 'root' and passwd == 'redhat' :
	print "Access Granted!!"
	#move to other options file
	execfile('menu.py')
else :
	print "You hav Wrong Authentication!"
	exit()
