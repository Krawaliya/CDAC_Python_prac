try:
	with open("temp.txt","r") as fp:
		print("File opem")
except FileNorDFound:
	print("Filr noy found")
	fp=open("temp1.txt","w")
	fp.close()
print("completed")

