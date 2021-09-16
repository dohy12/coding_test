# https://yganalyst.github.io/data_handling/memo_17_parallel/
# 병렬 처리 안했을 때 걸리는 속도

import time, os

def work_func(x):
    print("value %s is in PID : %s" % (x, os.getpid()))
    time.sleep(1)
    return x**5

def main():
    start = int(time.time())
    print(list(map(work_func, range(0,12))))
    print("***run time(sec) :", int(time.time()) - start)

if __name__ == "__main__":
    main()