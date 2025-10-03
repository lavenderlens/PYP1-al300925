# execute script from CMD line, with cursor in this directory

# open file for reading
file = open("data.txt")
# other ways to call a relative file path
# relative to where the calling script is
# file = open("../parent_folder/data.txt")
# file = open("./folder_name/data.txt")
print(type(file))#<class '_io.TextIOWrapper'>
# about as much use as a chocolate teapot
# we must use methods of the TextIOWrapper object to read/write

# 1. read (whole file)
print(f"\n{"*" * 50}\nread whole file\n{"*" * 50}")
print(file_contents := file.read())
# super-important
file.close()

# 2. read limited characters
print(f"\n{"*" * 50}\nread limited character\n{"*" * 50}")
file = open("data.txt")
print(chars79 := file.read(79))
print("*"*50)
print(chars79 := file.read(79))#the next 79 chars
file.close()

# 2A. read limited characters and reset cursor
print(f"\n{"*" * 50}\nread limited characters and reset cursor\n{"*" * 50}")
file = open("data.txt")
print(chars79 := file.read(79))
print("*"*50)
file.close()
file = open("data.txt")
print(chars120 := file.read(120))#read 120 chars from the start again
file.close()

# 3. read line
print(f"\n{"*" * 50}\nread line\n{"*" * 50}")
file = open("data.txt")
print(line := file.readline())
file.close()

# 3. read lines
print(f"\n{"*" * 50}\nread lines\n{"*" * 50}")
file = open("data.txt")
print(lines := file.readlines())#comma sep list of strings
file.close()
