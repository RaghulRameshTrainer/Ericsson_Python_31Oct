import multiprocessing
from time import sleep


def cal_square(numbers):
    for n in numbers:
        print("Square :" + str(n*n))
        sleep(1)

def cal_cube(numbers):
    for n in numbers:
        print("Cube :" + str(n*n*n))
        sleep(1)

if __name__=='__main__':
    data=[1,2,3,4,5]
    p1=multiprocessing.Process(target=cal_square,args=(data,))
    p2=multiprocessing.Process(target=cal_cube,args=(data,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("---Completed---")
