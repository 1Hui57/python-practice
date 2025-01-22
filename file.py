# 文字檔案的讀取和儲存
# 基本語法： 檔案物件= open(檔案路徑, mode=開啟模式)
# 開啟模式： 讀取模式-r 寫入模式-w 讀寫模式 -r+
# 讀取方式： 檔案物件.read()
# 如果想要一次讀取一行，可以使用迴圈將每一行字串放到變數中
# 讀取JSON格式的資料 import json
# 寫入(儲存)檔案： 檔案物件.write(字串)
# 寫入換行符號：檔案物件.write("這是範例文字\n")
# 寫入JSON格式： import json
#               json.dump(要寫入的資料, 檔案物件)
# 關閉檔案：檔案物件.close()
# 最佳實務(使用此方式，以上區塊會自動、安全的關閉檔案)：
#  with open(檔案路徑, mode=開啟模式) as 檔案物件:讀取或寫入檔案的程式


#儲存檔案
file=open("data.txt", mode="w", encoding="utf-8") #開啟 檔案物件放在file這個變數中
#除了開啟模式之外還可以指定編碼，encoding="utf-8" 這樣可以正常處理中文
file.write("Hello File\nSecond Line") # 操作 同一個檔案打開再寫入會有覆蓋效果
file.write("測試中文\n好棒棒")
file.close() # 關閉

#最佳實務，此方式檔案寫入後會自動關閉，不需要寫檔案關閉
with open("data2.txt", mode="w", encoding="utf-8") as file2:
    file2.write("5\n3")

# 讀取檔案(已經存在的檔案)
with open("data2.txt", mode="r", encoding="utf-8") as file:
    data=file.read()
print(data)

# 把檔案中的數字資料，一行一行的讀取出來，並計算總合
sum=0
with open("data2.txt", mode="r", encoding="utf-8") as file:
    for line in file: #一行一行的讀取
        sum+=int(line) #將讀取的資料轉換成數字形式
print(sum)

# 使用JSON格式讀取，放入變數data裡面
import json
with open("config.json",mode="r") as file:
    data=json.load(file)
print(data) # data 是一個字典資料
print("name",data["name"])
print("version",data["version"])
data['name']="New Name" # 修改變數中的資料

# 把最新的資料複寫回檔案中
with open("config.json",mode="w") as file:
    json.dump(data, file)
