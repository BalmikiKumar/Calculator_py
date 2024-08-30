import threading
import time
class MyThread(threading.Thread):
    def __init__(self,name,count):
        threading.Thread.__init__(self)
        self.name=name
        self.count=count
    def run(self):
        print("\n Starting "+ self.name)
        i=0
        while i<self.count:
            display(self.name,i)
           
            time.sleep(1)
            i=i+1
        print("\n Exiting "+ self.name)
def display(threadname,i):
        print("\n",threadname,i)
        
thread1=MyThread("One",5)
thread3=MyThread("Three",5)
    
thread2=MyThread("Two",5)
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
print("\n Exiting Main Thread")


        