import matplotlib
import matplotlib.pyplot as plt
def simple(legend,*sers):
	for v,i in enumerate(sers):
		#print i
		#print i.index
		i=i.sort_index()
		plt.plot(i.index,i,data=i,label=legend[v])
	plt.show()
	
