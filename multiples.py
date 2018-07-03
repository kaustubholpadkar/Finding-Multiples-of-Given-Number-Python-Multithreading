import threading

# thread class for producing nmultiples of given number
class Multiple (threading.Thread):
    def __init__(self, threadID, number, nmultiples):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.number = number
        self.nmultiples = nmultiples

    def run(self):
        print("Start Thread " + str(self.threadID))

        for i in range(self.nmultiples):
            print(str(self.threadID) + ' : ' + str(self.number) + ' * ' + str(i + 1) + ' = ' +  str(self.number * (i + 1)))

        print("Exit Thread " + str(self.threadID))

# create threads
thread1 = Multiple(111, 10, 20)
thread2 = Multiple(222, 2, 10)
thread3 = Multiple(333, 3, 5)

# start the threads
thread1.start()
thread2.start()
thread3.start()
