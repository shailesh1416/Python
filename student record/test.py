file = open('database2', 'r')

theRecords = list()
student = file.readline().rstrip()
for i in range(2):
    theRecords.append(student)
    student = file.readline().rstrip()
print(theRecords)
