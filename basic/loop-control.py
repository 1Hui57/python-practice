# break的簡易範例
n=0
while n<5:
    if n==3:
        break # n=3時強制結束迴圈，因次下面的程式不會跑
    print(n) #停留在n=2時跑的迴圈，下一行n=3
    n+=1
print("最後的n:",n)

# continue 的簡易範例
n=0
for x in[0,1,2,3]:
    if x%2==0: # 0/2=0, 1/2=1, 2/2=0, 3/2=0，所以在n=0和2時，不會跑下面的程式碼
        continue
    print(x)  # 只有在x=1和3時跑下面的程式碼
    n+=1  # x=1時n=0+1=1，x=3時n=1+1=2
print('最後的n:',n) # 因此n=2

# else 的簡易範例，在迴圈結束之前要做的事
sum =0
for x in range(11):
    sum=sum+x
else:
    print(sum)

# 綜合範例：找出平方根
# 輸入9，得到3
# 輸入11得到"沒有"

x=input( "請輸入數字：")
x=int(x)
for i in range(x): #假設輸入5，i=[0,1,2,3,4]
    if i==x**0.5: #也可以寫成i*i==x
        print(i)
        break # 用break強制結束迴圈時，不會執行else區塊
else:
    print("沒有整數平方根") 



