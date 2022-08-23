# implementation of the StudentFileReder ADT using a text file as the
# input source in which each field is stored on a seperate line

class StudentFileReder:
    # create new student instance.
    def __init__(self, inputSrc):
        self._inputSrc = inputSrc
        self._inputFile = None

    # Open the connection to the file input
    def open(self):
        self._inputFile = open(self._inputSrc, 'r')

    # Close the connection to the file
    def close(self):
        self._inputFile.close()
        self._inputFile = None

    # Extract all student records and store them in a list
    def fetchAll(self):
        theRecords = list()
        student = self.fetchRecord()
        while student != None:
            theRecords.append(student)
            student = self.fetchRecord()
        return theRecords

    # Extract the next students record from file
    def fetchRecord(self):
        # Read the first line of the record
        line = self._inputFile.readline().rstrip().split()
        if line == []:
            return None
        # if there is another record, create a storage object and fill it
        student = studentRecord()
        # data = self._inputFile.readline().rstrip().split(" ")
        student.idNum = line[0]
        student.firstName = line[1]
        student.lastName = line[2]
        student.classCode = line[3]
        student.gpa = line[4]
        return student


# storage class used for an individual student record
class studentRecord:
    def __init__(self):
        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0


if __name__ == "__main__":
    sr = StudentFileReder('database2')
    sr.open()
    records = sr.fetchAll()
    sr.close()
    print("Records Found : ")
    for record in records:
        # print(record.gpa)
        print(str(record.idNum)+" "+str(record.firstName)+" " +
              str(record.lastName)+" "+str(record.classCode)+" "+str(record.gpa))
