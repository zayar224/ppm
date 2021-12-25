import pkg_resources as pkr
import os, sys, stat
import subprocess as subp

''' This is the starting point.
Two option for user. (1) Collect Installed Package?
(2) Install Your Previous Package?'''

print("Please Select Following Option.\n(1) Collect The Installed Package? (2) Install Your Previous Package?\nPlease Type The Number....")

option = int(input())

if not type(option) is int:
	raise TypeError("Please Type Only Integer Number")

if type(option) is int:
	if option == 1:
		PackageList = [p.project_name for p in pkr.working_set]
		dependencies = open("PackageDependcy.txt", "a")
		for i in PackageList:
			dependencies.write(i + '\n')
		dependencies.close()
		os.chmod("PackageDependcy.txt", stat.S_IWRITE) #Change File Permission To Write Owner Mode
		print("We Collect Your Installed Package List.")

	#Install Packages From PackageDependcy.txt
	if option == 2:
		#Change Mode To Read File
		os.chmod("PackageDependcy.txt", stat.S_IREAD)
		#Open File
		readFile = open("PackageDependcy.txt", "r")
		rPackages = readFile.read()
		readFile.close()

		#Remove The \n
		FileList = rPackages.split("\n")

		#Install The Packages From Dependcy
		#for pack in FileList:
		try:
			for pack in FileList:
				subp.check_call([sys.executable, '-m', 'pip', 'install', pack])
		except Exception:
			pass

			print("Installed All Packages.")
		#Change Back File To Write Mode
		os.chmod("PackageDependcy.txt", stat.S_IWRITE)

