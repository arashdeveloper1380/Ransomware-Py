
from subprocess import check_output

def find_drive():

	drive = ["A:","B:","D:","E:","F:","G:","H:","Z:","N:","K:","L:","X:","P:","U:","J:","S:","R:","W:","Q:","T:","Y:","I:","O:","V:","M:"] 

	system_drive = []

	cmd = check_output("net share",shell=True)

	for i in drive:

		if i in cmd:
			system_drive.append(i)

	return system_drive

def find_files(drives):

		for p in passwand_files:
				try:
					cmd = check_output("cd / && dir /S /B *."+p,shell=True)
					f.writelines(cmd)
					print p
				except:
						pass

		for d in drives:
			for p in passwand_files:

					try:
						cmd = check_output(d+" && dir /S /B *."+p,shell=True)
						f.writelines(cmd)
						print d+" ----- "+p

					except:
							pass

		f.close()



passwand_files = ["jpg" , "pdf" , "mp3" , "rar" , "mp4" , "txt" , "html" , "js" , "php" , "png"]

drives = find_drive()

f = open("paths.txt","w")

find_files(drives)

