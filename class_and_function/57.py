# read csv file.

class CsvFile(object):

    def readfile(self, fileloc):
        with open(fileloc, 'r+') as file:
            data = file.read()
            return data
cf = CsvFile()
print(cf.readfile("/home/putwind/Desktop/MOCK_DATA.csv")) 