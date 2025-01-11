#參數的預設資料
def power(base, exp=0): #預設exp的值為0
    print(base**exp)
power(3,2)
power(3)

#使用參數名稱對應
def divide(n1,n2):
    print(n1/n2)
divide(6,3)
divide(n2=3,n1=6)
divide(n2=6,n1=3)

#無限/不定 參數資料
def avg(*ns): # *會把參數的資料變成tuple
    total=0
    for x in ns:
        total=total+x
    print(total/len(ns))  #len(ns)為列表的長度

avg(5,3) #參數為tuple(5,3)
avg(5,-3,5,4,1)