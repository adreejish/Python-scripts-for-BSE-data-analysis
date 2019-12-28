import pandas as pd
from datetime import date
from matplotlib.dates import date2num
def candle(df):
	cseq=[]
	for i in df.index:
		i=i.strftime('%Y-%m-%d')
		newl=date2num(pd.to_datetime(i)),df[i]['Open Price'].values[0],df[i]['High Price'].values[0],df[i]['Low Price'].values[0],df[i]['Close Price'].values[0]
		cseq.append(newl)
	return cseq
