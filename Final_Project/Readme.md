# Final_Project

## 簡介

* 在IoT device如何不藉由GPS來判斷當前situations(功耗高)
* 用功耗較低之sensor(accelerometer)
* 參考Estimating Contextual Situations Using Indicators from Smartphone Sensor Values論文之架構![](https://i.imgur.com/nG0a5Xn.png)
* 藉由Kernel Density Estimation與Particle Filtering判斷當前situation

## Kernel Density Estimation

* 對Accelerometer的X與Y分別做kernel density estimation找出distribution，如下圖以Sitting與On_Table為例
* Sitting
![](https://i.imgur.com/PPDRhi3.png)
![](https://i.imgur.com/a7OMip7.png)
* On_Table
![](https://i.imgur.com/eGqNt4n.png)
![](https://i.imgur.com/mbzutpa.png)



## Particle Filtering

* 預測機器人的移動路徑
    1. 機器人會在某個固定範圍的二維平面上移動
    2. 在二維平面上有幾個landmarks，用來判斷跟機器人間的相對距離
    3. 在預測機器人移動的particle filtering中，每個粒子代表一個座標點(x, y)
    4. 在初始的時候會把N個粒子隨意地丟到二維平面上
    5. 每個粒子座標採亂數uniform(min, high, N)，N個亂數在min跟high之間均勻分布
    6. partical filtering預測步驟
        * 計算機器人當前為位置與landmarks間的相對距離
        * **Predict Step :** 預測每個粒子的移動
        * **Update Step :** 算出每個粒子與landmarks間的相對距離，並計算粒子的weight (與機器人的座標越靠近，weight越高)
        * **Computing the State Estimate :** 找出與weight最高之粒子
        * **Particle Resampling :** 對粒子做resampling (把粒子丟到當前機器人位置的附近)
        * 示意圖
            *    圓圈表示landmarks，+代表機器人移動位置，紅點是每次預測出來的粒子
            ![](https://i.imgur.com/6ULx2XN.png)

* 我的想法
    1. 把Accelerometer的X與Y一樣當成座標來看
    2. 每個situation都會有2個kde distribution (X與Y)
    3. 把X與Y的kde distribution組合成一組座標，並當作landmarks (N個situations有N個landmarks)
    4. partical filtering預測步驟
        * 計算sensor values(X, Y)與landmarks(kde X, kde Y)間的相對距離
        * **Predict Step :** 預測每個粒子的移動(x與y會有-0.2 ~ +0.2的偏移)
        * **Update Step :** 算出每個粒子與landmarks間的相對距離，並計算粒子的weight (與機器人的座標越靠近，weight越高)
        * **Computing the State Estimate :** 找出與weight最高之粒子
        * **Particle Resampling :** 對粒子做resampling (粒子每次都重新隨機丟)

## 開發環境

1. python 3.7.5
2. node-red
3. om2m 0.8
4. app inventor 2

## 系統架構圖

![](https://i.imgur.com/pkjVHpZ.png)

## 操作流程

1. 開啟GSCL、node-red
2. 使用node-red在GSCL上建立所需要的Applications與containers![](https://i.imgur.com/QyQquTY.png)

3. 安裝手機APP，透過手機來學習各個situations (On_Table, Sitting, Walking)，並存入GSCL
    * "注意"手機APP需自行更改node-red的ip
    * 選擇situations![](https://i.imgur.com/8J43zJm.png)![](https://i.imgur.com/DAbUuAG.png)
    * 按下"Start Learning"開始學習
    * 當每個situations都學習完後，按下"Start"開始傳送current sensor values到GSCL，讓partical filtering能夠持續讀取到sensor values並判斷當前situaions
4. 開啟python程式final_project.py(需自行更改node-red的ip)，並按下Start開始判斷當前situations![](https://i.imgur.com/Khy8Re6.png)

5. 執行結果
    * python藉由手機當前sensor values，讓partical filtering判斷當前situation![](https://i.imgur.com/ICDgSK7.png)![](https://i.imgur.com/pWjXA9B.png)![](https://i.imgur.com/ewASDO4.png)

## 參考資料
1. [Estimating Contextual Situations Using Indicators from Smartphone Sensor Values， Stefan Forsström, Victor Kardeby (1-3 Sept. 2014) ](https://ieeexplore.ieee.org/document/7059668)
2. [Kalman-and-Bayesian-Filters-in-Python](https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python/blob/master/12-Particle-Filters.ipynb)
3. [statsmodels.nonparametric.kde](https://www.statsmodels.org/stable/generated/statsmodels.nonparametric.kde.KDEUnivariate.html#statsmodels.nonparametric.kde.KDEUnivariate)
4. [sklearn.neighbors.KernelDensity](https://scikit-learn.org/stable/auto_examples/neighbors/plot_kde_1d.html#sphx-glr-auto-examples-neighbors-plot-kde-1d-py)

