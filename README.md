# python-PM2.5-
利用python爬取PM2.5数据，两种方法
==============================

PM2.5数据来源于http://www.86pm25.com/city/beijing.html, 数据更新时间为一小时一次，历史数据网站上没有，因此无法获取，只能从当前时间向后爬取

一. 时间控件
==========
1.导入库
-------
import time <br>
from threading import Timer  <br>
import pandas as pd  <br>
import numpy as np <br>

2.爬虫函数
---------
	死循环，为了长时间爬取
while True:  <br>

	获取当前时间
file_time=time.strftime('%Y-%m-%d-%H',time.localtime(time.time())) <br>

	以当前时间命名文件
file_name='C:/Users/SQ/Desktop/'+file_time+'-PM.csv' <br>

	爬取网址上的table
data=pd.read_html('http://www.86pm25.com/city/beijing.html')[0] <br>

	得到需要的数据
data=data.ix[:,[0,1,3,4]].copy() <br>

	数据字符串做调整
data.ix[:,2]=data.ix[:,2].str.replace('μg/m³','') <br>
data.ix[:,3]=data.ix[:,3].str.replace('μg/m³','') <br>

	保存输出
data.to_csv(file_name,index=False) <br>

3.时间控件
---------

    间隔时间，设置为3600秒即1小时
timer_interval=3600 <br>
t=Timer(timer_interval,delayrun)   <br>
t.start()  <br>
