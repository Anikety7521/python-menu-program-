import subprocess as sp
import os
def program():
		os.system("export TERM=xterm;clear")
		print("\t\t\t\t\tWELCOME TO Menue-Program")
		print("\t\t\t\t\t-----------------------")
		print("""
			1) Press 1 For BASIC LINUX COMMANDS
			2) Press 2 For WEB SERVICES
			3) Press 3 DOCKER WORLD
			4) Press 4 Exit""")
		x = int(input("ENTER YOUR CHOICE:"))
		if x==1:
			def linux_commands():
				os.system("export TERM=xterm;clear")
				print("\t\t\t\tWELCOME TO WORLD OF LINUX")
				print("""
					A) Press 1 For Calender
					B) Press 2 For Date 
		            C) Press 3 For Calculator
		            D) Press 4 For Creating a New User
					E) Press 5 For Deleting User
					F) Press 6 To  login in another user 
					D) Press 7 For For Checking System IP
					E) Press 8 For Ping
			        F) Press 9 For Deleting Directory
		            G) Press 10 For Making Directory
					H) Press 11 For reading a file content
		            I) Press 12 For creating a file 
		            J) Press 13 For View all Disk Partitions in Linux
		            K) Press 14 For View Specific Disk Partition in Linux
		            L) Press 15 For Checking File System Disk Space Usage
		            M) Press 16 For Installing Software Using yum
		            N) Press 17 For Uninstalling  Software Using yum
		            O) Press 18 For Finding Path Of Software Installed In Linux
					P) Press 19 For Running Python Live Interpreter
		            Q) Press 20 To Run Browser
					R) Press 21 For Back""")
				print()	
				y=int(input("ENTER YOUR CHOICE : "))
				if y==1:
					print()
					os.system("cal")
				elif y==2:
					print()
					os.system("date")
				elif y==3:
					print()
					os.system("bc")   
				elif y==4:
					print()
					user_name=input("ENTER THE USER NAME : ")
					os.system(f"useradd {user_name};id {user_name}")
				elif y==5:
					print()
					user_name=input("ENTER THE USER NAME To DELETE : ")
					os.system(f"userdel {user_name}")
				elif y==6:
					print()
					user_name=input("ENTER THE USER NAME To LOGIN : ")
					os.system(f"passwd {user_name}")  
				elif y==7:
					print()
					os.system("ifconfig")
				elif y==8:
					print()
					pong = input("ENTER THE IP OR HOSTNAME YOU WANT TO PING : ")
					print()
					os.system(f"ping {pong}")
				elif y==9:
					print()
					dir1 = input("ENTER YOUR DIRECTORY NAME TO DELETE : ")
					os.system(f"rm -rf {dir1}")
				elif y==10:
					dir1 = input(" GIVE NAME OF YOUR DIRECTORY WITH PATH : ")
					os.system(f"mkdir {dir1}")
				elif y==11:
					print()
					filename = input("ENTER THE FILE PATH YOU WANT TO READ : ")
					print()
					os.system(f"cat {filename}")
				elif y==12:
					print()
					filename = input("ENTER THE FILE PATH YOU WANT TO CREATE : ")
					os.system(f"vi {filename}")
				elif y==13:
					print()
					os.system("fdisk -l")
				elif y==14:
					print()
					diskName = input("ENTER DISK NAME LIKE '/dev/sdb' : ")
					print()
					os.system(f"fdisk -l {diskName}")
				elif y==15:
					print()
					os.system("df -h")
				elif y==16:
					print()
					software_name =  input("ENTER THE SOFTWARE NAME U WANT TO INSTALL : ")
					print()   
					os.system(f"yum install {software_name}")
				elif y==17:
					print()
					software_name =  input("ENTER THE SOFTWARE NAME U WANT TO UNISTALL : ")
					print()
					os.system(f"yum remove {software_name}")
				elif y==18:
					print()
					software_name =  input("ENTER THE SOFTWARE NAME : ")
					print()
					os.system(f"rpm -q {software_name}")
				elif y==19:
					os.system("python3")
				elif y==20:
					os.system("firefox")
				elif y==21:
					program()
				else:
					print("\nYou Entered Wrong Choice ...")
					
			linux_commands()
		elif x==2:
			print("\n\n.........INSTALLING NECCESSARY FILES...........")
			sp.getoutput("rm -rf /etc/yum.repos.d/;mkdir /etc/yum.repos.d/;cd /etc/yum.repos.d/;wget https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm;wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm;wget http://rpms.famillecollet.com/enterprise/remi-release-7.rpm;wget https://www.elrepo.org/RPM-GPG-KEY-elrepo.org;wget http://repo.webtatic.com/yum/el7/webtatic-release.rpm")
			file1=open("/etc/yum.repos.d/soft.repo", 'w')
			file1.write("""[DVD1]
baseurl=file:///run/media/root/RHEL-8-1-0-BaseOS-x86_64/AppStream
gpgcheck=0

[DVD2]
baseurl=file:///run/media/root/RHEL-8-1-0-BaseOS-x86_64/BaseOS
gpgcheck=0""")
			file1.close()
			print("\n---------------INSTALLING HTTPD----------------------------------------------")
			os.system("yum install httpd")
			os.system("systemctl start httpd;systemctl stop firewalld;setenforce 0")
			print("------------------------------YOUR WEB SERVICE HAS STARTED----------------------")
		elif x==3:
			def docker():
				os.system("export TERM=xterm;clear")
				print("\t\t\t\tWELCOME TO WORLD OF DOCKER")
				print("""
					A) Press 1 For Installing Docker
					B) Press 2 For Start docker service 
					C) Press 3 For Launch Container 
					D) Press 4 For Start Container
					E) Press 5 For Stop Container
					F) Press 6 For Status Of Containers
					G) Press 7 FOR Delete Containers
					H) Press 8 For Delete Image 
					I) Press 9 For Stop docker service
					J) Press 10 For Status docker service
					K) Press 11 Back""")
				y=int(input("ENTER YOUR CHOICE : "))
				if y==1:
					os.system("cd /etc/yum.repos.d/;wget https://download.docker.com/linux/centos/docker-ce.repo;yum install docker-ce --nobest")
					print("\n\-------------------docker has been installed---------------")
				elif y==3:
					image = input("\nGIVE THE IMAGE NAME : ")
					version = input("\nENTER VERSION : ")
					os_name = input("\nENTER YOUR OS NAME : ")
					os.system(f"docker pull {image}:{version};clear;docker run -it --name {os_name} {image}:{version} ")
				elif y==4:
					os_name = input("\nENTER YOUR OS NAME TO START: ")
					os.system(f"docker start {os_name}")
				elif y==5:
					os_name = input("\nENTER YOUR OS NAME TO STOP: ")
					os.system(f"docker stop {os_name}")
				elif y==6:
					os.system("docker ps -a")
				elif y==7:
					os_name = input("\nENTER YOUR OS NAME TO DELETE: ")
					os.system(f"docker rm {os_name}")
				elif y==8:
					image_name = input("\nENTER YOUR IMAGE NAME TO DELETE: ")
					version = int(input("\nENTER VERSION : "))
					os.system(f"docker rmi {image_name}:{version}")
				elif y==9:
					os.system("systemctl stop docker;tput setaf 3;echo '---------------YOUR DOCKER SERVICE STOPPED ---------'")
				elif y==10:
					os.system("systemctl status docker")
				elif y==2:
					os.system("systemctl start docker;tput setaf 3;echo '---------------YOUR DOCKER SERVICE STARTED --------'")
				elif y==11:
					program()
				else:
					print("\nYou Entered Wrong Choice ...")
					
			docker()		
		elif x==4:
			os.system("export TERM=xterm;clear")
      			exit()

		
program()
