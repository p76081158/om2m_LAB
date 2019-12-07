

# LAB4_GA with Node-red
## 目標:
    使用 node-red 分別建立以下
	  1. Create a "Location_Gateway_Application" Application on OM2M
		2. Create a "DESCRIPTOR" container on OM2M
		    3. Create a "DESCRIPTOR contentInsances" on OM2M
		4. Create a "DATA" container on OM2M
			5. Create a "DATA contentInsances" (for testing) on OM2M
    6. Create a http node to forward data to GSCL

## 作法or步驟:  
1. 步驟1~5的node-red node flow 如下圖![](https://i.imgur.com/AnL4KYt.png)
2. 步驟6是為了藉由傳送HTTP POST指令給node-red server，轉送到GSCL來完成步驟5 Create a "DATA contentInsances" on OM2M，其node-red node flow與postman測試結果如下圖![](https://i.imgur.com/WbGmMg6.png)![](https://i.imgur.com/VjF8dSp.png)![](https://i.imgur.com/0Rne0zZ.png)![](https://i.imgur.com/zlJ7kOH.png)





    
# LAB4_App inventor Sender
## 目標:
    須完成兩個功能
      1.讀取手機(or 模擬器)的location sensor
      2.將其值交給 GA(node-red)
 
## 作法or步驟:  
1. 讀取手機(or 模擬器)的location sensor![](https://i.imgur.com/WKLBVXk.png)
2. 將其值交給 GA(藉由node-red)
    * 傳送給node-red server，如果成功會回傳200![](https://i.imgur.com/JMcrMVf.png)

    * 其結果透過node-red server轉傳到GA完成Create a "DATA contentInsances"![](https://i.imgur.com/nUkTzZ4.png)

 

       
# LAB4_NA with Node-red
# 目標:
    使用 node-red 建立以下
    1. Create a "Location_Network_Application" Application on OM2M
    2. Subscribe new contentInsatnace in the   gscl/Location_Gateway_Application/DATA  on OM2M and save recive notify
    3. Create a http node to response previously save data
    
## 作法or步驟:  
1. 步驟1是藉由node-red創建一個NA到nscl，而步驟2是訂閱gscl上GA的data，其node-red flow node如下![](https://i.imgur.com/Enj1c4y.png)![](https://i.imgur.com/qlue0Yg.png)![](https://i.imgur.com/WjoifB1.png)


2. 步驟3可以分成2個部分
    * 把訂閱的data資訊存到xml中，並且存到本地端![](https://i.imgur.com/1rGDukQ.png)


    * 藉由傳送HTTP POST到node-red server取得儲存在本地端的xml資訊![](https://i.imgur.com/TD7ZTCm.png)
    * 最後是藉由postman測試![](https://i.imgur.com/P6P96wz.png)![](https://i.imgur.com/WMIe3h3.png)





    
    
# LAB4_APP Inventor reciver
## 目標:
    須完成兩個功能
      1. http get NA(node-red) 上儲存的 data
      2. 將該 data 用來啟動 google map 並顯示位子
      
## 作法or步驟:  
1. http get NA(node-red) 上儲存的 data
透過下圖的node-red node flow讀取xml中儲存的資訊![](https://i.imgur.com/qlQDdnr.png)
    

2. 將該 data 用來啟動 google map 並顯示位子
    * 讀出來的data是LAB3透過postman儲存的資訊![](https://i.imgur.com/o7oxi7u.png)

    * 最後把她透過google map顯示位置![](https://i.imgur.com/I7iX5sa.png)

