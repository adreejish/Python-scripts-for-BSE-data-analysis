import matplotlib
import matplotlib.pyplot as plt
def simple(legend,*sers):
	for v,i in enumerate(sers):
		#print i
		#print i.index
		i=i.sort_index()
		plt.plot(i.index,i,data=i,label=legend[v])
	plt.show()
	

def candle(seq):
	ax1=plt.gca()
	candlestick_ohlc(ax1,seq)
	ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	plt.show()

def roll(ser,*periods):
	roll1=ser
	#rollres
	for v,i in enumerate(periods):
		rollres=roll1.rolling(i,center=True).mean()
		plt.plot(rollres.index,rollres,data=rollres,label=str(i))
		#print i
	plt.plot(ser.index,ser,data=ser,label="original")
	plt.legend()
	plt.show()
		
