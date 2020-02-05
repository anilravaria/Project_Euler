num = 600851475143
# 600851475143


def LPF(number):
    for i in range(2, int(number)):

       # if(i <= 0):
        #    break
        if i % 2 == 0:
            #print("inside continue")
            # print(i)
            continue
        # print(i)
        if(number % i == 0):
            #print(str(number)+" "+str(i))
            newnumber = int(number/i)
            #print(str(newnumber)+" "+str(number)+"/"+str(i))
            print("Quotinent: "+str(newnumber))
            print("Divisor: "+str(i))
            print("Dividend: "+str(number))
            return LPF(newnumber)


LPF(num)
