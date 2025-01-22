# 網路連線 一般取得網頁資料
import urllib.request as request
src="https://wehelp.tw/"
with request.urlopen(src) as response:
    data=response.read() .decode("utf-8") # 取得網址的原始碼(HTML、CSS、JS)
print(data)

# 串接、擷取公開資料
import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1 "
with request.urlopen(src) as response:
    data=json.load(response) # 取得json格式的資料
print(data)

# 取得資料
spotList=data['data']['results']
print(spotList)
for spot in spotList:
    print(spot['stitle'])

# 寫入檔案中，此寫法寫入後會自動關閉
with open("soptData.txt", "w", encoding="utf-8") as file:
    for spot in spotList:
        file.write(spot["stitle"]+"\n") # \n為換行符號
