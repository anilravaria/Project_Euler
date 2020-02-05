
# for k in range(999, 999//2, -1):
#     for i in range(999, 99, -1):
#         a = list()
#         num4 = k*i
#         num5 = num4
#         while(num4 > 0):
#             num = num4 % 10
#             num4 = num4//10
#             # print(num)
#             # print(num4)
#             a.append(num)
#         num2 = ''.join([str(i)for i in a])
#         print(num5)
#         print(k)
#         print(i)
#         print(num2)
#         if(int(num2) == num5):
#             print("palindrome")
#             break
#         print("---------------------------------------------------")
a = list()
for k in range(999, 99, -1):
    for i in range(999, 99, -1):
        num3 = k*i
        num4 = num3
        print(str(k)+"*"+str(i)+"="+str(num3))
        num3 = list(str(num3))
        num3 = reversed(num3)
        num3 = ''.join([str(i) for i in num3])
        print(num3)
        if(int(num3) == int(num4)):
            a.append(str(k)+"*"+str(i)+"="+str(num3))
            print("palindrome")
            break
    if(k == 950):
        break
print(a)
