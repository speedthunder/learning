#抓取 PTT python 的網頁原始碼(HTML)
import urllib.request as req
def getData(url):
    #url="https://www.ptt.cc/bbs/python/index.html"
    # 建立一個 Request 物件，附加 Request Headers 的資訊
    request = req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36"})
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    #print(data)
    # 解析原始碼，取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    #print(root.title.string)
    #root(根目錄).title(標籤).string(文字)
    titles=root.find_all("div",class_="title")   #尋找class="title" 的 div 標籤
    #print(titles.a.string)
    #print(titles)
    for title in titles:
        if title.a != None: #如果標題包含 a 標籤 (沒有被刪除)，印出來
            print(title.a.string)

    #找到內文是 ‹ 上頁 的 a 標籤
    nextlink=root.find("a", string="‹ 上頁")
    return nextlink["href"]

#抓取一個頁面的標題

pageURL = "https://www.ptt.cc/bbs/python/index.html"
#pageURL=getData(pageURL)
count=0
countpage=int(input("輸入要抓取的頁數："))
while count < countpage:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1
#print(pageURL)