# 抓取PTT八卦版的網頁原始碼(HTML)
import urllib.request as req
def getData(url):
    # 建立一個Request物件，附加Headers的資訊
    # 如果是18歲才能進入的網站，可能會有一個cookie:顯示滿18才能進到網頁
    request = req.Request(url, headers={
        "cookie":"over18=1",#滿18的cookie
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    })
    # 利用request物件去打開網址
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    # print(data)

    #解析原始碼，取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser") #用bs4套件的BeautifulSoup功能解析data資料(以html格式)
    titles=root.find_all("div", class_="title") #尋找所有class="title" 的div標籤
    # print(titles.a.string) #a是div裡面的a，要再拿到裡面的字串寫string
    # print(titles) #titles是一個字串
    for title in titles:
        if title.a !=None: #如果標題包含 a 標籤 (沒有被刪除)，印出來
            print(title.a.string)
    # 抓取上一頁的連結
    nextLink=root.find("a",string="‹ 上頁")
    # print(nextLink)
    return nextLink["href"]
pageURL="https://www.ptt.cc/bbs/sex/index.html"
count=0
while count<3:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1
getData(pageURL)