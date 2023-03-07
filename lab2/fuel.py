# Pro code
km = int(input())
tank = int(input())

liter = km//15
keawLim = 50/100*tank
kwanLim = 90/100*tank
print(int(liter//keawLim)+1)
print(int(liter//kwanLim)+1)


# Mare code
import math
distkm = int(input())
capoilliter = int(input())
kw = int(distkm//(capoilliter*(50/100)*15))
kn = int(distkm//(capoilliter*(90/100)*15))
print(kw+1)
print(kn+1)