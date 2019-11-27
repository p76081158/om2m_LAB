# LAB1_GuessTheNumber

## 目標:
	隨機生成一個1~100之間的整數，讓使用者透過textbox輸入要猜測的數字，並且提示遊戲進度。
## 作法or步驟:
1. 輸入一個數字來進行猜測![](https://i.imgur.com/e6zj5MU.png)

2. 根據輸入的數字判斷是否正確，若不正確就顯示正確的數字所在範圍![](https://i.imgur.com/Z8b12D6.png)
3. 重複猜測直到找到正確數字，並顯示所用猜測次數![](https://i.imgur.com/Q8r9zed.png)



# LAB1_HttpPostApplication
## 目標:
    將textbox中的文字，經由HTTP POST的方式傳到自己定義的node-red server，並將回傳的response放置到畫面上。

## 作法or步驟:
1. 設定node-red server的ip![](https://i.imgur.com/fXvmUwj.png)
2. 在node-red中設定接收http post的node![](https://i.imgur.com/0hWO21P.png)
3. 傳送文字到node-red server並接收回傳的response![](https://i.imgur.com/4TxIGMb.png)





# LAB1_flow

## 目標:
    接收來自LAB1_POST_text的http request，回傳"Hello"加上收到訊息name
    
## 作法or步驟:
1. 在node-red中設定接收http post的node![](https://i.imgur.com/0hWO21P.png)
2. 接收http post並response "Hello + msg.payload.name"![](https://i.imgur.com/w8Y8KGI.png)![](https://i.imgur.com/78gqf6d.png)

