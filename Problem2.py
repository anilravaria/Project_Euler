def SumofEvenFibonacciNumbers():
    firstNum = 1
    SecondNum = 2
    arr = set()
    arr.add(SecondNum)
    while True:
        ThirdNum = firstNum+SecondNum
        if(ThirdNum > 4_000_000):
            break
        firstNum = SecondNum
        SecondNum = ThirdNum
        if(ThirdNum % 2 == 0):
            arr.add(ThirdNum)
    sumsofEvenFibonacciNumbers = sum(arr)
    return sumsofEvenFibonacciNumbers


Fn = SumofEvenFibonacciNumbers()
print(Fn)
