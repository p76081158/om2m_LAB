# LAB3_OM2M with Postman
## 目標:
    使用Postman分別建立以下Entities
	1. Create a "MY_SENSOR" Application
		2. Create a "DESCRIPTOR" container
			3. Create a "DESCRIPTOR contentInsances"
		4. Create a "DATA" container
			5. Create a "DATA contentInsances"
			6. Create a "Subscription" contact to localhost:1400/monitor

## 作法or步驟:
1. Create a "MY_SENSOR" Application
    * 設定Authorization(對nscl或gscl的存取權限)![](https://i.imgur.com/Ljat6le.png)

    * 設定Body(用來建立application)![](https://i.imgur.com/TG1UgHd.png)
    * 用postman將資料post到gscl_addr/applications上建立application，並接收回傳訊息(是否建立成功)![](https://i.imgur.com/mOYULHk.png)![](https://i.imgur.com/R1gQ3Qv.png)
2. Create a "DESCRIPTOR" container
    * 設定Authorization(對nscl或gscl的存取權限)![](https://i.imgur.com/fS7z1ND.png)

    * 設定Body(用來建立descriptor)![](https://i.imgur.com/LWfAL4D.png)

    * 用postman將資料post到applications/MY_SENSOR/containers上建立descriptor，並接收回傳訊息(是否建立成功)![](https://i.imgur.com/P6aQSyb.png)![](https://i.imgur.com/UENts3O.png)


3. Create a "DESCRIPTOR contentInsances"
    * 設定Authorization(對nscl或gscl的存取權限)![](https://i.imgur.com/BB6iutT.png)

    * 設定Body(用來建立contentInstances)![](https://i.imgur.com/vvQEgMk.png)

    * 用postman將資料post到applications/MY_SENSOR/containers/DESCRIPTOR/contentInstances上建立contentInstances，並接收回傳訊息(是否建立成功)![](https://i.imgur.com/zJcQmnF.png)
![](https://i.imgur.com/GRyhTif.png)

4. Create a "DATA" container
    * 設定Authorization(對nscl或gscl的存取權限)![](https://i.imgur.com/02eFDUZ.png)

    * 設定Body(用來建立container)![](https://i.imgur.com/TxmnITF.png)

    * 用postman將資料post到gscl_addr/applications/MY_SENSOR/containers上建立container，並接收回傳訊息(是否建立成功)![](https://i.imgur.com/LoEfTgR.png)![](https://i.imgur.com/YbnLDIE.png)


5. Create a "DATA contentInsances"
    * 設定Authorization(對nscl或gscl的存取權限)![](https://i.imgur.com/oRS7LFx.png)

    * 設定Body(用來建立contentInsances)![](https://i.imgur.com/IvnKcmV.png)

    * 用postman將資料post到gscl_addr/applications/MY_SENSOR/containers/DATA/contentInstances上建立contentInsances，並接收回傳訊息(是否建立成功)![](https://i.imgur.com/6b5vNx9.png)![](https://i.imgur.com/QE6B7EU.png)


6. Create a "Subscription" contact to localhost:1400/monitor
    * 設定Authorization(對nscl或gscl的存取權限)![](https://i.imgur.com/qVydqDe.png)

    * 設定Body(用來建立Subscription)![](https://i.imgur.com/ID4TFg3.png)

    * 用postman將資料post到applications/MY_SENSOR/containers/DATA/contentInstances/subscriptions上建立對DATA底下contentInstancds的Subscription，並接收回傳訊息(是否建立成功)![](https://i.imgur.com/EwaQxcY.png)![](https://i.imgur.com/wKesCDu.png)
    * 訂閱通知訊息![](https://i.imgur.com/7ScfxZL.png)






# LAB3_OM2M  GA with Node-red
## 目標:
    使用 node-red 在GSCL分別建立以下 Entities
	1. Create a "MY_SENSOR" Application
		2. Create a "DESCRIPTOR" container
			3. Create a "DESCRIPTOR contentInsances"
		4. Create a "DATA" container
			5. Create a "DATA contentInsances"
	6. 在 GA(node-red) 開啟 /sensorData Server 負責轉傳 data 到 OM2M
	

## 作法or步驟:
1. 1~5步驟在Node-red上用5個node chain來實作建立applications、container、contentInsances，結果跟postman一樣![](https://i.imgur.com/W2S5ZC8.png)
2. 在 GA(node-red) 開啟 /sensorData Server 負責轉傳 data 到 OM2M
    * node red設定![](https://i.imgur.com/6cnbkaf.png)
    * 用postman傳送HTTP POST給node-red server並藉此轉傳data給om2m![](https://i.imgur.com/zGo2QJV.png)![](https://i.imgur.com/VPLwIo0.png)







# LAB3_OM2M  NA with Node-red
## 目標:
    	

    使用 node-red 在 NSCL 分別建立以下 Entities
	1. Create a "MY_NETWORK_APPLICATION"
	2. Subscribe new contentInsatnace in the   gscl/MYSENSOR/DATA 並儲存
	3. 開啟 /getxmlfile Server 負責讀取先前儲存的資料
    
## 作法or步驟:
1. 前兩個步驟跟之前介紹的相同
    * 在node-red上的node chain為下圖![](https://i.imgur.com/ct9o1Ln.png)
    * 訂閱通知位置![](https://i.imgur.com/SScE9lZ.png)

2. 開啟 /getxmlfile Server 負責讀取先前儲存的資料
    * 將notifications存為xml放在指定的本地端位置![](https://i.imgur.com/1Xhx637.png)

    * 用postman傳送HTTP GET訊息到node-red server![](https://i.imgur.com/pFnWsIQ.png)

    * 透過node-red server讀取本地端儲存的資料![](https://i.imgur.com/hCvUo62.png)![](https://i.imgur.com/wRFNUAB.png)![](https://i.imgur.com/faVNF3P.png)


