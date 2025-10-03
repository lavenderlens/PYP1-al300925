# execute from CMD line, ensure cursor is in this directory

with open("data.txt") as file:
    print(file)
    for line in file:
        print(line)
# no need to close!
# no need to call individual read methods
# the file IS the context (hence term context manager)
# under the hood, "with...as" calls dunder methods of file object "TextIOWrapper"
# __enter__ and __exit__
# when error handling, the __exit__ method will handle ALL errors
# no need for try-except blocks
# optionally, we may write our own context managers