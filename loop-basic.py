# while 迴圈
# 1+2+3...+10
n=1
sum=0 #用來記錄累加的結果
while n<=10:
    sum=sum+n
    n+=1
print(sum)

# for迴圈
for x in [3,5,1]: # x代入列表中的資料
    print(x)

for x in 'Hello': # x代入字串中的每個字元
    print(x)

for x in range(3):# range會生成列表[0,1,2]，因此印出0,1,2
    print(x)      

for x in range(3,8):# 如果range(3,8)，意思為產生從3開始不包含8的列表[3,4,5,6,7]
    print(x)

#用for迴圈1+2+3...+10
sum=0
for n in range(11):
    sum=sum+n
print(sum)