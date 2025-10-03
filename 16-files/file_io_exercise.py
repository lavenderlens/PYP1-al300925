# MANUAL P275

# ensure that your terminal is in the smae working directory a sthis script
# cretae students.dat with your names

# read from the students.dat
# assign to file_read_ref
file_read_ref = open("students.dat")
print(file_read_ref)#object

# in python, assigna. grade A-D to each student
results = []

# loop round the file_read_ref
# for each name:
    # grade = input()
    # results.append(name.strip('\n') + ", " + grade.strip('\n'))

for name in file_read_ref:
    grade = input(f"{name}: GRADE:")
    results.append(name.strip('\n') + ", " + grade.strip('\n'))
# close file_read_ref
file_read_ref.close()

# WRITE results to a file called student_grades.txt
file_write_ref = open("student_grades.txt", mode="w")

for entry in results:
    file_write_ref.write(f"{entry}\n")
file_write_ref.close()