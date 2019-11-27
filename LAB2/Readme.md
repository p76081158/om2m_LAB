# LAB2_Get_Sensor_Value
## 目標:
    按下按鈕時，抓取手機上的三種sensor，Accelerometer、OrientationSensor、LocationSensor
    
## 作法or步驟:
根據手機的移動讀出不同的sensor數值![](https://i.imgur.com/O47nqug.png)![](https://i.imgur.com/qfz0ZyH.png)


    
    
    
# LAB2_ShowLocationGoogleMap
##目標:
    實現五個功能，1.抓取LocationSensor(GPS) 2.將1中的值傳到node-red顯示 3.讀取server存放的location資料 4(5).將1(3)中的資料用google map定位 

## 作法or步驟:
**設定node-red server ip**
![](https://i.imgur.com/URJohGz.png)


**功能實現**
1. 抓取LocationSensor(GPS)![](https://i.imgur.com/b0hYmKv.png)

2. 將抓取的值傳到node-red顯示![](https://i.imgur.com/jiHqA92.png)

3. 讀取server存放的location資料![](https://i.imgur.com/diCBGS7.png)

4. Google map定位My Location![](https://i.imgur.com/RWDI3CR.png)

5. Google map定位Server Location![](https://i.imgur.com/Re3jq7T.png)




    
    
    
    
# LAB2_flow.json
##目標:
    1.接受來自app的訊息，並回復response，2.回傳在server儲存的location data
    
## 作法or步驟:
1. 接收app訊息並回復response![](https://i.imgur.com/AKv5Sz0.png)
2. 回傳server儲存的location data![](https://i.imgur.com/za6EePJ.png)
3. node-red上的debug message![](https://i.imgur.com/2vPZopg.png)

