# 載入內建的 sys 模組並取的資訊
import sys
print(sys.platform)
print(sys.maxsize)

# 可以操作別名 improt a as b
import sys as s
print(s.platform)

# 自訂模組
# 建立 geometry模組載入使用

import modules.geometry as geometry
result=geometry.distance(1,1,5,5) #這裡有跑一次程式，但因為沒有print所以沒有印出東西，只有回傳值
print(result) #這裡才有印出回傳值

result=geometry.slope(1,2,5,6) #同上
print(result)

# 調整搜尋模組的路徑
import sys
print(sys.path) #印出模組的搜尋路徑列表
sys.path.append("modules") #在模組的搜訊路徑列表中，新增新的搜尋路徑
