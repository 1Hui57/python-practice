# 集合的運算
s1={3,4,5}

# in/not in：看資料是否在集合內，結果為布林值
print(3 in s1) 
print(10 in s1)

#交集&聯集
s1={3,4,5}
s2={4,5,6,7}
s3=s1&s2 #交集&：兩個集合中，相同的資料
s4=s1|s2 #聯集|：取兩個集合中的所有資料，但不重複取
print(s3, s4)

#差集&反交集
s3=s1-s2 #差集-：從s1中減去和s2重疊的部分
s4=s1^s2 #反交集^：取兩個集合中，不重疊的部分
print(s3, s4)

#將字串拆解為集合
s=set("Hello") #寫法 set(字串)
print(s)
print("H" in s) 

# 字典的運算 字典為建值對(Key-Value Pair)
dic={"apple":"蘋果","banana":"香蕉",'orange':'橘子' }
print(dic['apple'])
dic['apple']="小蘋果" #將apple對應值修改為小蘋果
print(dic["apple"])

#使用in & not in判斷key使否存在於字典中
dic={"apple":"蘋果","banana":"香蕉",'orange':'橘子' }
print("apple" in dic)
print("蘋果" in dic) #蘋果是value，in判斷的是key所以是false

#刪除建值對，以key當作代表，但刪的是整個建值對
del dic["apple"] 
print(dic)

#從列表的資料產生字典，寫法為 for 變數 in 列表
dic={x:x*2 for x in [3,4,5] }
print(dic)