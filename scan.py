#! /usr/bin/python2

import commands,os,time

ip_list=[]
ip_addr="192.168.10."
for i in range(121)[-21:] :
	check=commands.getstatusoutput('ping -c 1 192.168.10.'+str(i))
	if check[0] == 0 :
		ip_list.append(ip_addr+str(i))
	else :
		print "IP Address "+str(i) + " doesnt exist"

print "Scanned IP"
time.sleep(2)

print ip_list

cpu_ip=[]
cpu_check="lscpu | grep -i 'CPU(s):' | head -1 | cut -d: -f2"
cpu_RAM="cat /proc/meminfo | grep -i 'MemTotal:' | cut -d: -f2"
for i in ip_list:
	cpu_core=commands.getoutput("sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@"+i+" "+cpu_check)
	cpu_ram=commands.getoutput("sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@"+i+" "+cpu_RAM)
	cpu_ip.append(i+cpu_core+cpu_ram)

print cpu_ip

