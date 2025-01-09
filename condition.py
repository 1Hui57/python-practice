# 判斷式

#取得字串形式的使用者輸入資料
x=input("請輸入數字：")
#將字串型態轉換成數字型態
x=int(x)
if x >200:
    print("大於200")
elif x>100:
    print('大於100')
else :
    print('小於100')

# 四則運算
n1=int(input('請輸入數字：'))
n2=int(input('請輸入數字：'))
op=input('請輸入運算：')
if op =="+":
    print(n1+n2)
elif op=='-':
    print(n1-n2)
elif op=='*':
    print(n1*n2)
elif op=='/':
    print(n1/n2)
else :
    print('無法運算')