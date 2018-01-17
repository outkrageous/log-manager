import os
import math

class logOperations():
    def __init__(self):
        self.logfilepath = None
        self.search_string = None

    def getLogFile(self, path_to_log):
        if os.path.isfile(path_to_log):
            self.logfilepath = path_to_log
            return self.logfilepath
        else:
            raise IOError('The file or path does not exist, was it entered correctly?')

    def getLogFileFromUser(self):
        while True:
            logfile = raw_input("What is the path to the log file?: ")

            if os.path.isfile(logfile):
                self.logfilepath = logfile
                print('File found...')
                break
            else:
                print('File does not exist. Is the path correct?')
                continue

    def getlog(self):
        if not None:
            return self.logfilepath
        else:
            print('File not read in yet')
            return False

    def getStringToSearchFor(self, string_to_find):
        if string_to_find:
            return self.search_string

    def printNumOfLines(self, search_string, logfile):
        num = self.getNumberOfInstances(search_string, logfile)
        num = str(num)
        if num == 0:
            print('String not found in file')
        else:
            print('Found ' + num + ' instances of: ' + search_string + ' in ' + logfile)

    def getNumberOfInstances(self, search_string, logfile):
        path_to_file = self.getLogFile(logfile)
        num = 0
        with open(path_to_file, 'r') as log_file:
            for line in log_file:
                if search_string in line:
                    num = num + 1
        return num

    def checkLogExists(self):
        log_file = self.getlog()
        if log_file is None:
            self.getLogFileFromUser()
        else:
            return True


    def truncateLogFile(self):
        log_file = self.getlog()
        if log_file is None:
            self.getLogFileFromUser()
            log_file = self.getlog()
        with open(log_file, 'w') as file:
            file.truncate()

    def getLogSize(self):
        self.checkLogExists()
        logfile = self.logfilepath
        size_of_file = os.path.getsize(logfile)

        if size_of_file == 0:
            return "0B"
        else:
            size_name = ("B", "KB", "MB")
            i = int(math.floor(math.log(size_of_file, 1024)))
            p = math.pow(1024, i)
            s = round(size_of_file / p, 2)

        return "%s %s" % (s, size_name[i])

    def printlogsize(self):
        size = self.getLogSize()
        print("Size of file: " + size)
