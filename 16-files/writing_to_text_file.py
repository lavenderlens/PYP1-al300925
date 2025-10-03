# execute script with cursor in this directory

# open file, same as in read, but with optional 2nd arg
# default is r for read only (why we only need one arg for file reading)
# a = append to existing
# x = creates, raises a FileExistsError if already exists
# w = writes but overwrites if exists
file = open("data2.txt", mode="w")
text = "The weather is sunny and calm"
file.write(text)
file.close()
