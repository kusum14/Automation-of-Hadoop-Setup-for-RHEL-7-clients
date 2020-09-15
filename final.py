import subprocess as sp
import os
print("\t\tPlease choose an option")
print("\t\t----------------------\n");


while True:
		
	print("""
	Enter 1 to print date
	Enter 2 to print calendar
	Enter 3 to make a directory
	Enter 4 to click photo
	Enter 5 to take video
	Enter 6 to open web server
	Enter 7 to configure HDFS cluster
	Enter 8 to configure MapReduce cluster
	Enter 9 to configure docker
	Enter any key to exit
	""")


	inp=input("Enter input ")


	system=input("""
Enter local to perform function on local system
Enter remote to perform function on remote system
		""")

	if(system=="local"):

		if int(inp)==1:
			output=sp.getstatusoutput("date")
			if output[0]==0:
				print(output[1])
			else:
				print("""Error
					{}""".format(output[1]))

		elif int(inp)==2:
			output=sp.getstatusoutput("cal")
			if output[0]==0:
				print(output[1])
			else:
				print("""Error
					{}""".format(output[1]))
			
		elif int(inp)==3:
			output=sp.getstatusoutput("mkdir /root/Desktop/folder")
			if output[0]==0:
				print("Folder created successfully on Desktop")
			else:
				print("""Error
					{}""".format(output[1]))
			
		elif int(inp)==4:
			output=sp.getstatusoutput("python36 /root/Desktop/code/photoclick.py")
			if output[0]==0:
				print("Photo clicked and saved on Desktop")
			else:
				print("""Error
					{}""".format(output[1]))


		elif int(inp)==5:
			output=sp.getstatusoutput("python36 /root/Desktop/code/mycam.py")
			if output[0]==0:
				print("")
			else:
				print("""Error
					{}""".format(output[1]))

		elif int(inp)==6:
			os.system("cp -f hosts /etc/ansible/hosts")

			ip=input("Enter ip ")
			f=open('/etc/ansible/hosts','a')
			string="{} ansible_user=root ansible_password=redhat".format(ip)
			f.write(string)
			f.close()
			os.system("ansible-playbook /root/Desktop/code/web.yml")


		elif int(inp)==7:
			msd=input("""
			Enter 1 to configure master node
			Enter 2 to configure slave
			Enter 3 to configure client
			Enter any key to exit
			""")


			if int(msd)==1:
				os.system("cp -f hosts /etc/ansible/hosts")
				ip=input("Enter ip ")
				f=open('/etc/ansible/hosts','a')
				string="{} ansible_user=root ansible_password=redhat".format(ip)
				f.write(string)
				f.close()
				
				os.system("ansible-playbook /root/Desktop/code/hadoop/package_install.yml")
				os.system("ansible-playbook /root/Desktop/code/hadoop/master.yml")
				
				
			elif int(msd)==2:

				os.system("cp -f hosts /etc/ansible/hosts")

				ip=input("Enter ip ")
				f=open('/etc/ansible/hosts','a')
				string="{} ansible_user=root ansible_password=redhat".format(ip)
				f.write(string)
				f.close()
				
				os.system("ansible-playbook /root/Desktop/code/hadoop/package_install.yml")
				os.system("ansible-playbook /root/Desktop/code/hadoop/slave.yml")
				
			elif int(msd)==3:

				os.system("cp -f hosts /etc/ansible/hosts")

				ip=input("Enter ip ")
				f=open('/etc/ansible/hosts','a')
				string="{} ansible_user=root ansible_password=redhat".format(ip)
				f.write(string)
				f.close()
				
				os.system("ansible-playbook /root/Desktop/code/hadoop/package_install.yml")
				os.system("ansible-playbook /root/Desktop/code/hadoop/client.yml")

			else:
				exit()


		elif int(inp)==8:
			jt=input("""Enter 1 to configure jobtracker
Enter 2 to configure tasktracker
Enter 3 to configure client node
Enter any other key to exit""")

			if int(jt)==1:
				os.system("cp -f hosts /etc/ansible/hosts")
				ip=input("Enter ip ")
				f=open('/etc/ansible/hosts','a')
				string="{} ansible_user=root ansible_password=redhat".format(ip)
				f.write(string)
				f.close()
				
				os.system("ansible-playbook /root/Desktop/code/hadoop/package_install.yml")
				os.system("ansible-playbook /root/Desktop/code/hadoop/jobtracker.yml")

			
				
			elif int(jt)==2:
				os.system=("cp hosts /etc/ansible/hosts")
				ip=input("Enter ip ")
				f=open('/etc/ansible/hosts','a')
				string="{} ansible_user=root ansible_password=redhat".format(ip)
				f.write(string)
				f.close()
				
				os.system("ansible-playbook /root/Desktop/code/hadoop/package_install.yml")
				os.system("ansible-playbook /root/Desktop/code/hadoop/tasktracker.yml")
			

				
			else:
				exit()	

		elif int(inp)==9:
			dockinp=input("""Enter 1 to install docker
Enter 2 to set up docker container
Enter any other key to exit""")


			if(int(dockinp)==1):

				os.system("cp -f hosts /etc/ansible/hosts")
				ip=input("Enter ip ")
				f=open('/etc/ansible/hosts','a')
				string="{} ansible_user=root ansible_password=redhat".format(ip)
				f.write(string)
				f.close()
				
				os.system("ansible-playbook /root/Desktop/code/docker/yumConfigure.yml")
				os.system("ansible-playbook /root/Desktop/code/docker/docker.yml")
				

			elif(int(dockinp)==2):
				type=input("""Enter 1 to start ubuntu container
Enter 2 to start centos container
Enter any other key to exit""")

				if(int(type)==1):

					os.system("cp -f hosts /etc/ansible/hosts")

					ip=input("Enter ip ")
					f=open('/etc/ansible/hosts','a')
					string="{} ansible_user=root ansible_password=redhat".format(ip)
					f.write(string)
					f.close()

					os.system("ansible-playbook /root/Desktop/code/docker/docker-ubuntuImage.yml")

				elif(int(type)==2):

					os.system("cp -f hosts /etc/ansible/hosts")
					ip=input("Enter ip ")
					f=open('/etc/ansible/hosts','a')
					string="{} ansible_user=root ansible_password=redhat".format(ip)
					f.write(string)
					f.close()
					
					os.system("ansible-playbook /root/Desktop/code/docker/docker-centosImages.yml")
					
				else:
					exit()

			
		
		else:
			exit()



	elif(system=="remote"):		

		

		if int(inp)==1:
			ip=input("Enter ip ")
			vardate=("ssh {} date".format(ip))
			output=sp.getstatusoutput(vardate)
			if output[0]==0:
				print(output[1])
			else:
				print("""Error
				{}""".format(output[1]))

		elif int(inp)==2:
			ip=input("Enter ip ")
			varcal=("ssh {} cal".format(ip))
			output=sp.getstatusoutput(varcal)
			if output[0]==0:
				print(output[1])
			else:
				print("""Error
					{}""".format(output[1]))


		elif int(inp)==3:
			ip=input("Enter ip ")
			vardir=("ssh {} mkdir /root/Desktop/folder".format(ip))
			output=sp.getstatusoutput(vardir)
			if output[0]==0:
				print("Folder created successfully on Desktop")
			else:
				print("""Error
					{}""".format(output[1]))

		elif int(inp)==4:
			ip=input("Enter ip ")
			image1=("scp /root/Desktop/code/photoclick.py {}:/root/Desktop/photoclick.py".format(ip))
			image2="ssh "+ip+" python36 /root/Desktop/photoclick.py"
			image3=("scp {}:/root/Desktop/myphoto.png /root/Desktop/photofromanotherip.png".format(ip))
			output1=sp.getstatusoutput(image1)
			os.system(image2)
			output3=sp.getstatusoutput(image3)

			
			if output3[0]==0:
				print("Photo clicked and saved on Desktop")
			else:
				print("""Error
					{}""".format(output3[1]))

			


		elif int(inp)==5:
			ip=input("Enter ip ")
			vid1=("scp /root/Desktop/code/mycam.py {}:/root/Desktop/mycam.py".format(ip))
			vid2="ssh -X "+ip+" python36 /root/Desktop/mycam.py"
			output1=sp.getstatusoutput(vid1)
			os.system(vid2)
			
			if output1[0]==0:
				print("")
			else:
				print("""Error
					{}""".format(output1[1]))
			

		elif int(inp)==6:
			os.system("cp -f hosts /etc/ansible/hosts")
			ip=input("Enter ip ")
			f=open('/etc/ansible/hosts','a')
			string="{} ansible_user=root ansible_password=redhat".format(ip)
			f.write(string)
			f.close()

			os.system("ansible-playbook /root/Desktop/code/web.yml")


		elif int(inp)==7:
			msd=input("""
Enter 1 to configure master node
Enter 2 to configure slave node
Enter 3 to configure client node
Enter any other key to exit
			""")

			

			if int(msd)==1:
				os.system("cp -f hosts /etc/ansible/hosts")
				ip=input("Enter ip ")
				f=open('/etc/ansible/hosts','a')
				string="{} ansible_user=root ansible_password=redhat".format(ip)
				f.write(string)
				f.close()

				os.system("ansible-playbook /root/Desktop/code/hadoop/package_install.yml")
				os.system("ansible-playbook /root/Desktop/code/hadoop/master.yml")
				
				
			elif int(msd)==2:
				os.system("cp -f hosts /etc/ansible/hosts")
				ip=input("Enter ip ")
				f=open('/etc/ansible/hosts','a')
				string="{} ansible_user=root ansible_password=redhat".format(ip)
				f.write(string)
				f.close()

				os.system("ansible-playbook /root/Desktop/code/hadoop/package_install.yml")
				os.system("ansible-playbook /root/Desktop/code/hadoop/slave.yml")
				
			elif int(msd)==3:
				os.system("cp -f hosts /etc/ansible/hosts")
				ip=input("Enter ip ")
				f=open('/etc/ansible/hosts','a')
				string="{} ansible_user=root ansible_password=redhat".format(ip)
				f.write(string)
				f.close()
				
				os.system("ansible-playbook /root/Desktop/code/hadoop/package_install.yml")
				os.system("ansible-playbook /root/Desktop/code/hadoop/client.yml")

			else:
				exit()

		elif int(inp)==8:
			jt=input("""Enter 1 to configure jobtracker
Enter 2 to configure tasktracker
Enter any other key to exit""")

			
			if int(jt)==1:

				os.system("cp -f hosts /etc/ansible/hosts")
				ip=input("Enter ip ")
				f=open('/etc/ansible/hosts','a')
				string="{} ansible_user=root ansible_password=redhat".format(ip)
				f.write(string)
				f.close()
				

				os.system("ansible-playbook /root/Desktop/code/hadoop/package_install.yml")
				os.system("ansible-playbook /root/Desktop/code/hadoop/jobtracker.yml")

			
				
			elif int(jt)==2:

				os.system("cp -f hosts /etc/ansible/hosts")
				ip=input("Enter ip ")
				f=open('/etc/ansible/hosts','a')
				string="{} ansible_user=root ansible_password=redhat".format(ip)
				f.write(string)
				f.close()
				
				
				os.system("ansible-playbook /root/Desktop/code/hadoop/package_install.yml")
				os.system("ansible-playbook /root/Desktop/code/hadoop/tasktracker.yml")
			

				
			else:
				exit()	


		elif int(inp)==9:
			dockinp=input("""Enter 1 to install docker
Enter 2 to set up docker container
Enter any other key to exit""")



			if(int(dockinp)==1):
				os.system("cp -f hosts /etc/ansible/hosts")
				ip=input("Enter ip ")
				f=open('/etc/ansible/hosts','a')
				string="{} ansible_user=root ansible_password=redhat".format(ip)
				f.write(string)
				f.close()
				
				os.system("ansible-playbook /root/Desktop/code/docker/yumConfigure.yml")
				os.system("ansible-playbook  /root/Desktop/code/docker/docker.yml")
				

			elif(int(dockinp)==2):
				type=input("""Enter 1 to start ubuntu container
Enter 2 to start centos container
Enter any other key to exit""")

				if(int(type)==1):
					os.system("cp -f hosts /etc/ansible/hosts")
					ip=input("Enter ip ")
					f=open('/etc/ansible/hosts','a')
					string="{} ansible_user=root ansible_password=redhat".format(ip)
					f.write(string)
					f.close()
					

					os.system("ansible-playbook  /root/Desktop/code/docker/docker-ubuntuImage.yml")

				elif(int(type)==2):

					os.system("cp -f hosts /etc/ansible/hosts")
					ip=input("Enter ip ")
					f=open('/etc/ansible/hosts','a')
					string="{} ansible_user=root ansible_password=redhat".format(ip)
					f.write(string)
					f.close()
					
					os.system("ansible-playbook  /root/Desktop/code/docker/docker-centosImages.yml")
					

				else:
					exit()

		else:
			exit()

	

	run=input("Do you want to run the program again?  ")
	if run=="no":
		break

