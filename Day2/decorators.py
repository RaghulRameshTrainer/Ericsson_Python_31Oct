import time

def calc_time(func):     # func =squareIt , cubeIt
    def wrapper(*args,**kwargs):    # *agrs = nums
        start=time.time()
        res=func(*args,**kwargs)
        end=time.time()
        print(func.__name__ + ' took : '+ str((end-start)*1000) + ' milli seconds')
        return res
    return wrapper

@calc_time
def squareIt(nums):
    result=[]
    for x in nums:
        result.append(x**2)
    return result

@calc_time
def cubeIt(nums):
    result=[]
    for x in nums:
        result.append(x**3)
    return result

data=list(range(1,1000001))
squareIt(data)
cubeIt(data)