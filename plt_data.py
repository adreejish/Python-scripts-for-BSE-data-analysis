import matplotlib
import matplotlib.pyplot as plt
def simple(*sers):
	for i in sers:
		#print i
		#print i.index
		i=i.sort_index()
		plt.plot(i.index,i,data=i)
	plt.show()
	
