# 建立函世語法 def 函式名稱(參數名稱):
#                函式內部的程式碼
def sayHello():
    print('Hello')

def say(msg):
    print(msg)

# 呼叫函式語法 函式名稱(參數資料)
sayHello()
say("mdfk")

s=("djfJhdGGG")
s=s.lower()
print(s)

def stringLower(s):
    s=s.lower()
    print(s)

value=stringLower('kl;kj') #會印出kl;kj，因為stringLower要先跑過一次才會把回傳值代入value
print('執行print印出',value) #會印出none

def add(n1,n2):
    return(n1+n2)
print(add(5,6))

#將迴圈包裝成函式
#從n1+....到n2
def calculate(n1,n2):
    result=0
    for i in range(n1,n2+1):
        result=result+i
    print (result)
    
calculate(5,8)
print(calculate(5,6)) #calculate函式沒有回傳值，因此印出none