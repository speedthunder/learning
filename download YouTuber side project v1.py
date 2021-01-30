#僅能下載 360 的畫質
#沒有顯示下載中
#這一行 [result.config(text = "影片無法下載完成")] 會顯示錯誤
########################################################################

from pytube import YouTube
import tkinter as tk

def download():
    try:
        result.set("下載中")
        YouTube(url.get()).streams.filter(subtype = "mp4",progressive = True).last().download()
        result.set("下載完成")
    except:
        result.config(text = "影片無法下載完成")

root = tk.Tk()
root.geometry("280x100")
root.title("下載 YouTube 影片")
url = tk.StringVar()
result =tk.StringVar()
label_1 = tk.Label(root,text = "請貼上影片網址： ")
label_1.pack()
entry = tk.Entry(root,textvariable=url)
entry.pack()
label_2 = tk.Label(root, textvariable=result)
label_2.pack()

button = tk.Button(root,text = "下載", command = download)
button.pack()

root.mainloop()