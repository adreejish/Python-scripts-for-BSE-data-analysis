import pandas as pd
def get_sub(start_date,end_date,df):
	start_date=pd.to_datetime(start_date)
	end_date=pd.to_datetime(end_date)	
	#print type(start_date)
	#print type(end_date)
	#print type(df)
	#print type(df.index)
	usethis = df[(df.index>start_date)&(df.index<end_date)]
	return usethis

def create_df(path):
	df=pd.read_csv(path)
	df['Date']=pd.to_datetime(df['Date'])
	df=df.set_index('Date')
	return df

#def ret_df(col,period,action,df):
#period denotes yearly, monthly or daily
#action:min-for min of period,max-for max of period,na-for all the data(period ignored)
#col-column to work with-high,low,closing

def get_col(column,df):
#pass df from get_data
	col=pd.Series(df[column])
	return col

def get_periods(period,df):
	periods=[]
	#returns available periods:eg valid months,valid years
	def get_years():
		periods=[]
		for i in df.index.year:
			periods.append(i)
		periods=set(periods)
		return periods
	def get_months():
		periods=[]
		for i in df.index.month:
			periods.append(i)
		periods=set(periods)
		return periods
 
	switcher={
		'month':get_months,
		'year':get_years
		}
	fun=switcher.get(period)
	return fun()

def get_allperiods(period,column,df):
	rel_col=get_col(column,df)
	def monthvar():
		return rel_col.index.month
	def yearvar():
		return rel_col.index.year
	switcher={
		'month':monthvar,
		'year':yearvar
	}
	fun=switcher.get(period)
	return fun()

def do_action(period,column,action,df):
	periods=[]
	if(period!='daily'):
		periods=get_periods(period,df)
	rel_col=get_col(column,df)
	rel_col_idx=get_allperiods(period,column,df)
	res_ser=pd.Series([])
	def do_max():
		res_ser=pd.Series([])
		rel_col=get_col(column,df)
	        rel_col_idx=get_allperiods(period,column,df)
		for i in periods:
			res=rel_col.loc[rel_col_idx==i].max()
			res_ser=res_ser.append(rel_col[(rel_col==res)&(rel_col_idx==i)])
		return res_ser
	def do_min():
		rel_col=get_col(column,df)
	        rel_col_idx=get_allperiods(period,column,df)
		res_ser=pd.Series([])
		for i in periods:
			res=rel_col.loc[rel_col_idx==i].min()
			res_ser=res_ser.append(rel_col[(rel_col==res)&(rel_col_idx==i)])
		return res_ser
	def do_none():
		rel_col=get_col(column,df)
		return rel_col
	
		
		
	switcher={
		'max':do_max,
		'min':do_min,
		'na':do_none
	}
	fun=switcher.get(action)
	return fun()


	
