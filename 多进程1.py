#方法一 直接调用import time
import time
import random
from multiprocessing import Process
def run(name):
    print('%s runing' %name)
    time.sleep(random.randint(1,5))
    print('%s running end' %name)


if __name__ == '__main__':

    p1=Process(target=run,args=('tian',)) #必须加,号
    p2=Process(target=run,args=('doinb',))
    p3=Process(target=run,args=('lwx',))
    p4=Process(target=run,args=('crips',))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    print('主线程')