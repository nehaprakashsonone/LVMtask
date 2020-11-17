import os
import subprocess


print()
print()
os.system("tput setaf  3")
print("********Welcome To Automation of LVM Partition using python-script******")
os.system("tput setaf  7")
print()
print()
os.system("tput setaf  6")
print("\t\t\t Details of All the Hard Disk Attached:-")
os.system("tput setaf  7")
print()
print()
disk = subprocess.getoutput("fdisk  -l")
print(disk)

print()
e1 = input("Please Enter the first harddisk name,(e.g /dev/sde):  ")
print("***creating physical volume*****")
e2 = subprocess.getoutput("pvcreate {}".format(e1))
print(e2)
print()
print("\t\t\t physical volune created")
d1 = input("Do u wanted to see the physical volume created or not(y/n):  ")
if d1=="n":
	pass
else:
	e3 = subprocess.getoutput("pvdisplay {}".format(e1))
	print(e3)

print("*******Done with the first Harddisk*****")
print("----------------------------------------------------------")
print()
e4 = input("now u have to choose another harddisk name:   ")
print("***creating physical volume*****")
e5 = subprocess.getoutput("pvcreate {}".format(e4))
print(e4)
print()
print("\t\t\t physical volune created")
d2 = input("Do u wanted to see the physical volume created or not(y/n):  ")
if d2=="n":
	pass
else:
	e6 = subprocess.getoutput("pvdisplay {}".format(e4))
	print(e6)

print("*******Done with the second Harddisk*****")
print("----------------------------------------------------------")
print()

print("Creating  the Volume group ......")
vg = subprocess.getoutput("vgcreate  V_group {} {}".format(e1,e4))
print(vg)
print()

d3 = input("Do u wanted  to see the Volume group (y/n):  ")
if d3=="n":
	pass
else:
	e7 = subprocess.getoutput("vgdisplay V_group")
	print(e7)

print("-------------------------------------------------------------")
print()

print("creating logical volume from the volume group......")
size = input("Enter the size of logical volume u want:   ")
name = input("Enter the name u want to give to lv:   ")
cr1 = subprocess.getoutput("lvcreate  --size  {}G --name {} V_group".format(size,name))
print("Logical volume is created*******")
cr2 = input("do u wanted to see logical volume(y/n):  ")
if cr2=="n":
	pass
else:
	e8 = subprocess.getoutput("lvdisplay  V_group/{}".format(name))
	print(e8)

print()
print("THANK YOU")
print("--------------------------------------------------------------------------")

	


