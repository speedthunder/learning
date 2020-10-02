
key = str                                           #定義變數型態為 str
while True:                                         #while 迴圈
    key = input ("請輸入想顯示的資料：")              #我想將input後的資料放入 key 值中，
    if key == "quit" or key == "exit":              #再判斷 key 值中是否輸入exit or quit 否則往下執行
        print ("謝謝使用")                           #顯示謝謝使用
        break                                       #停止程式
    elif key == "":                                 #再判斷是否為空字串
        print("請輸入資料，不要給我空空的")           #如果為空字串就顯示 請輸入資料，不要給我空空的
    else:
        print(key)                                  #以上判斷全不成立就顯示輸入的 key 值