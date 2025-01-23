import urllib.request as req
def getData(url):
    request = req.Request(url, headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, likes Gecko) Chrome/131.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data= response.read() .decode("utf-8")
    # print(data)

    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")
    # print(titles) #所有title的div

    # 抓取上一頁的連結
    nextLink=root.find("a",string="‹ 上頁")
    print(nextLink)

    lottery=[] # 新增一個列表，裡面的資料型態為字典，放入文章的所有資料
    for item in titles:
        if item.a !=None:
            # print(item.a.string) # 印出標題
            href=item.a.get('href')
            # print("https://www.ptt.cc"+href) # 印出網址
            lottery.append({
                "title":item.a.string,
                "href":"https://www.ptt.cc"+href
            })

    # 找到文章的like次數
    likeList=[] #放like次數的列表
    likes=root.find_all("div", class_="nrec")
    for item in likes:
        if item.span !=None:
            # print(item.span.string)
            likeList.append(item.span.string)
    # print(likeList)

    # 在lottery列表中加入like次數
    for index,item in enumerate(likeList):
        lottery[index]["like"]=item
    # print(lottery)

    # 要拿到每個文章的發布時間
    timeURLlist={}
    for index, item in enumerate(lottery):
        timeURL=item["href"]
        timeURLlist[index]=item["href"]
    # print(timeURLlist) #為一個物件，key為文章列表index，value為文章網址
    timeList={}
    for key, value in timeURLlist.items():
        timeURL=value
        request= req.Request(timeURL, headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, likes Gecko) Chrome/131.0.0.0 Safari/537.36"
        })
        with req.urlopen(request) as response:
            data= response.read() .decode("utf-8")
        root=bs4.BeautifulSoup(data, "html.parser")
        timeSpans=root.find_all("span", class_="article-meta-value")
        if len(timeSpans)>3 and timeSpans[3] !=None:
            timeSpan=timeSpans[3].get_text()
        else:
            timeSpan=""
        # print(timeSpan) #拿到第一頁文章列表的發文時間，沒有時間的為空字串
        timeList[key]=timeSpan
    # print(timeList) #一個字典，key為文章列表的index，value為文章的發文時間，沒有則為空字串

    #將發文時間加入
    for key,value in timeList.items():
        lottery[key]["time"]=value
    print(lottery)
    return nextLink["href"]

pageURL="https://www.ptt.cc/bbs/Lottery/index.html"
count=0
while count<3:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1
getData(pageURL)
    
