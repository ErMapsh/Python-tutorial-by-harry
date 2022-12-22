import time
from functools import lru_cache
import inspect
'''
@lru_cache(maxsize=3)
def some_work(n):
    """Some task taking a seconds"""
    time.sleep(n)
    return n



if __name__ == "__main__":
    print("Now running some work")
    some_work(2)
    print("Done..Calling again")
    some_work(6)
    print("Now running some work")
    some_work(3)
    print("Done..Calling again0")
    input()
    some_work(4)
    print("Done..Calling again1")
    some_work(6)
    print("Done..Calling again2")
    some_work(2)#here maxsize is 3 , previous 3 fucntion calling dont have 2 but if maxsize is larger then is possible

'''

#Excersie 

no = int(input("Enter the maximum size of lru cache:"))
@lru_cache(maxsize = no)
def cache_fuc(n):
    ans = time.ctime(n) 
    time.sleep(5)
    return ans

if __name__ == "__main__":
     #identify which day or time using random second give as input to coverttime function
    print(cache_fuc(1242424242))
    print(cache_fuc(3242424142))
    print(cache_fuc(1242424242))
