class LogMessage:
    def __init__(self,filename):
        self.filename = filename
    def read(self):
        f = open(self.filename,'r')
        lines = f.readlines()
        for each in lines:
            print(each, end='')
    def write(self,message):
        f = open(self.filename, 'a')
        f.write(message)
    
log = LogMessage('test.txt')
log.write('Testing..' + '\n')
log.write('test123' + '\n')
log.read()