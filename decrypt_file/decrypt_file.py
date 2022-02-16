
from cryptography.fernet import Fernet 
from subprocess import check_output
from os import remove

key = raw_input("enter the key : ")

Encrypt = Fernet(key)

def decrypt_files():

	file = open("paths.txt","r")
	read_file = file.readlines()

	for path in read_file:

		try:

			path = path.strip("\n")
			path = path.strip("\r")

			f = open(path , "rb")

			data = f.read()

			dec_data = Encrypt.decrypt(data)

			name = path.replace("[encrypted]","")

			newfile = open(name,"wb")

			newfile.write(dec_data)

			f.close()

			newfile.close()

			remove(path)

			print "decrypted -> "+path
		except:
				print "error"



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



passwand_files = ["jpg[encrypted]" , "pdf[encrypted]" , "mp3[encrypted]" , "rar[encrypted]" , "mp4[encrypted]" , "txt[encrypted]" , "html[encrypted]" , "js[encrypted]" , "php[encrypted]" , "png[encrypted]", "jpeg[encrypted]", "wmv[encrypted]"]

drives = find_drive()

f = open("paths.txt","w")

find_files(drives)

decrypt_files()

