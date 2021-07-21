def recursive_func(i):
    if i==100:
        return
    print("재귀 함수 호출")
    recursive_func(i+1)

recursive_func(0)