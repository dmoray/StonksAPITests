from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as pit
import pandas as pd
import numpy as np
from datetime import datetime, time

STARTDATE = '2022-05-01'
ENDDATE= str(datetime.now().strftime('%Y-%m-%d'))

Stock ="PGR"

def get_data(ticker):
    try:
        stockdata = data.DataReader(ticker,'yahoo',STARTDATE,ENDDATE)
        df=pd.DataFrame(stockdata)
        df.to_csv('yfin_test'+datetime.now().strftime('%Y%m%d')+str(time())+'.csv')
        
    except RemoteDataError:
        print('No data found for {t}'.format(t=ticker))
        
get_data(Stock)

print('------- Execution Completed -------')