from threading import *
from time import sleep
class Hello(Thread):

    def run(self):
        self.__running = True
        for i in range(5):
            print("Hello")
            sleep(1)

    def stop(self):
        print("STOP BEEN CALLED")
        #self._stop()

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)
t1=Hello()
t2=Hi()

t1.start()
t2.start()

t1.stop()
t2.join()

print("=====DONE=====")