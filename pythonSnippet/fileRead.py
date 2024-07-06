
def fileRead(fileName):
	try:
		f = open(fileName,'r')
		print(f.readline())
	except IOError:
		print("io error")
	finally:
		f.close()

def fileRead2(fileName):
	with open(fileName, 'r') as f:
		print(f.readline())

print(fileRead2("file.txt"))