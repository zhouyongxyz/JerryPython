class Log:

    @staticmethod
    def logFile(data, typeRequest):
        f = open('log.txt', 'a')
        formatLog = "Request: " + typeRequest + "\n"
        formatLog += "Content: " + data + "\n"
        f.write(formatLog)
        f.close()
