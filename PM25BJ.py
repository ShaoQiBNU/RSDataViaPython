import time
from threading import Timer 
import pandas as pd 
import numpy as np
def delayrun():
	while True:
		file_time=time.strftime('%Y-%m-%d-%H',time.localtime(time.time()))
		file_name='C:/Users/SQ/Desktop/'+file_time+'-PM.csv'

		data=pd.read_html('http://www.86pm25.com/city/beijing.html')[0]
		data=data.ix[:,[0,1,3,4]].copy()
		data.ix[:,2]=data.ix[:,2].str.replace('μg/m³','')
		data.ix[:,3]=data.ix[:,3].str.replace('μg/m³','')
		data.to_csv(file_name,index=False)

timer_interval=3600 #delay time interval:3600s=1 hour
t=Timer(timer_interval,delayrun)  
t.start() 




