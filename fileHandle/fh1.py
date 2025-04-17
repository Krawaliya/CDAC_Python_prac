##create the new file
fp = open("new_file.txt","w")
#w :: write open
#it always open given file as empty file
#if file doesn't exist then new file created
#close the file 
fp.close
###
#how to write in file
#write function writes given string into the file
fp = open("new_file.txt","w")
fp.write("Hello my name is krish ")
fp.close

################################################
#how to append the file 
# bcoz w wipe all existing content of file

fp=open("new_file.txt","a")
fp.write("this is new line in file")
fp.close()

#how to read the file
#open file in read mode
#read mode::allow to read the complete file

#read() :: read function ral all contentes
#of the file in a single string

fp=open("new_file.txt","r")
contents=fp.read()
print(contents)
fp.close

###############################
###############################
################################
#############################
################################



#open binary file
#to read binary file :: rb mode
# to write into binary file :: wb mode



#####################################
#syntax for file op using with construct
#with construct
#it is given by python to make sure that close() function is always called

# read the file using with construct

with open("new_file.txt","r") as fp:
	contents = fp,read()
#when we come of woith :: file is automatically close by PVM

print(contents)
new_contents=" these are new contents \n next line"
with open("new_file.text","w") as 
