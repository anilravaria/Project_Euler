a = list()
j = 0
for i in range(101):
    a.append(i*i)
ssn1 = sum(a)

print(ssn1)
for i in range(101):
    j = j+i
ssn2 = j*j
print(ssn2)
dssn = ssn2-ssn1
print(dssn)
