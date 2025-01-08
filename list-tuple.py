#有序可變動列表 List
grades=[12,60,72,92,55]
print(grades[2]) #印出72
grades[0]=100
print(grades[0])
print(grades[0:2]) #印出編號為0、1個資料
grades[3:]=[] #把編號3之後的資料變成空白=刪除
print(grades)
grades+=[66,58] #grades=grades+[66,58]
print(grades)
print(len(grades)) #印出列表的長度 len(列表資料)

data=[[3,4,5],[6,7,8]]
print(data[0][1]) #印出第一層列表的編號0資料(一個列表)的編號第一個資料
data[0][0:2]=[5,5,5] #把[3,4,5]中的編號0到1的資料也就是[3,4]改成[5,5,5]
print(data)
