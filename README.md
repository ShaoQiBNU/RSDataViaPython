利用python爬取PM2.5数据
==============================

> PM2.5数据来源于http://www.86pm25.com/city/beijing.html, 数据更新时间为一小时一次，历史数据网站上没有，因此无法获取，只能从当前时间向后爬取

# 一. 时间控件

## 1.导入库

```python
import time
from threading import Timer 
import pandas as pd 
import numpy as np
```

## 2.爬虫函数

```python
# 死循环，为了长时间爬取
while True: 

# 获取当前时间
file_time=time.strftime('%Y-%m-%d-%H',time.localtime(time.time()))

# 以当前时间命名文件
file_name='C:/Users/SQ/Desktop/'+file_time+'-PM.csv'

# 爬取网址上的table
data=pd.read_html('http://www.86pm25.com/city/beijing.html')[0]

# 得到需要的数据
data=data.ix[:,[0,1,3,4]].copy()

# 数据字符串做调整
data.ix[:,2]=data.ix[:,2].str.replace('μg/m³','')
data.ix[:,3]=data.ix[:,3].str.replace('μg/m³','')

# 保存输出
data.to_csv(file_name,index=False)
```

## 3.时间控件

```python
# 间隔时间，设置为3600秒即1小时
timer_interval=3600
t=Timer(timer_interval,delayrun)  
t.start() 
```


# 二.睡眠

## 1.导入库

```python
import time
import pandas as pd 
import numpy as np
```

## 2.爬虫

```python

# 死循环，为了长时间爬取
while True: 

# 获取当前时间
file_time=time.strftime('%Y-%m-%d-%H',time.localtime(time.time()))

# 以当前时间命名文件
file_name='C:/Users/SQ/Desktop/'+file_time+'-PM.csv'

# 爬取网址上的table
data=pd.read_html('http://www.86pm25.com/city/beijing.html')[0]

# 得到需要的数据
data=data.ix[:,[0,1,3,4]].copy()

# 数据字符串做调整
data.ix[:,2]=data.ix[:,2].str.replace('μg/m³','')
data.ix[:,3]=data.ix[:,3].str.replace('μg/m³','')

# 保存输出
data.to_csv(file_name,index=False)

# 睡眠时间
time.sleep(3600)
```
