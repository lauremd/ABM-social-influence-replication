from datetime import datetime

class Log:

    def __init__(self):
        pass

    def write(self, message): #append timestamped message to file
        now = datetime.now().strftime("%d-%m-%Y %H:%M:%S ")
        with open("input.txt", "a") as log:
            log.write(now + message + "\n")