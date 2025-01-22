# 在專案要建立封包，需開啟一個封包資料夾
# 內容除了模組一、模組二之外，需要新增一個：__init__.py(雙底線)：__init__.py(雙底線)
# 使用封包基本語法： import 封包名稱.模組名稱
# 也可以建立模組別名 import 封包名稱.模組名稱 as 別名名稱

#ex. -專案資料夾
#        - package_practive.py  主程式
#        - package 封包資料夾
#               - __init__.py 封包資料夾必須要放的檔案
#               - point.py  計算點的模組
#               - line.py  計算線的模組

# import package.point
import package.point as point #直接把封包名稱+模組名稱改為別名
# result= package.point.distance(3,4)
result = point.distance(3,4)
print("距離",result)
import package.line
result= package.line.slope(1,1,3,3)
print("斜率",result)

