

# 檔案說明:
    

# LAB5
## 目標:
    使用任意方法完成以下:
    1. 分別控制 LAMP_0 的開/關、LAMP_1 的開/關、ALL_ON、ALL_OFF 共六個動作
    2. 在 APP 上，顯示當前燈泡的狀態 (主動 or 被動皆可)

## 作法or步驟:  
1. 分別控制 LAMP_0 的開/關、LAMP_1 的開/關、ALL_ON、ALL_OFF 共六個動作
    
    * 在node-red server上判斷手機端傳來的action字串來決定六個動作中的其中一個![](https://i.imgur.com/4UA5XEi.png)![](https://i.imgur.com/8bE4igh.png)


    * 手機端的button function如下![](https://i.imgur.com/lXXxViz.png)

2. 在 APP 上，顯示當前燈泡的狀態 (主動)
    * 在node-red上實作讀取om2m中的2個lamp的status，並讓手機端能透過HTTP GET來取得lamps的status![](https://i.imgur.com/A4SRAE0.png)

    * 在手機端我們可以透過clock來設置timer，讓手機定時發送HTTP GET到node-red取得lamps的status；timer的秒數可以自訂。![](https://i.imgur.com/8H1voPs.png)![](https://i.imgur.com/a80S7DS.png)

3. 實際操作步驟
    1. 開始狀態![](https://i.imgur.com/PpAzKMj.png)
    2. 打開lamp0  (timer會每0.5秒抓取lamps status)![](https://i.imgur.com/oOXOH4n.png)
    3. 打開lamp1  (timer會每0.5秒抓取lamps status)![](https://i.imgur.com/2zwhN4L.png)
    4. 全關![](https://i.imgur.com/OWIEmDw.png)




 
    



