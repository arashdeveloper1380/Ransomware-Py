
from subprocess import check_output

def find_drive():

	drive = ["A:","B:","C:","D:","E:","F:","G:","H:","Z:","N:","K:","L:","X:","P:","U:","J:","S:","R:","W:","Q:","T:","Y:","I:","O:","V:","M:"] 

	system_drive = []

	cmd = check_output("net share",shell=True)

	for i in drive:

		if i in cmd:
			system_drive.append(i)

	return system_drive

drives = find_drive()

print drives







