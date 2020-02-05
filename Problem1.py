number = int(input("Enter the number: "))


def SumofMuliplesof3and5(number):
    arr = set()
    for i in range(number):
        if(i % 3 == 0 or i % 5 == 0):
            arr.add(i)
    sumsof3and5 = sum(arr)
    return sumsof3and5


a = SumofMuliplesof3and5(number)
print(a)
