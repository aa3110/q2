from bib__init__ import file_read,stock_update,file_save,high,low,cross,crossdown,crossup,gain,loss
from bib__init__ import chan_in,chan_out,chan_it,chan_ot,chan_ib,chan_ob,alpha_there,fu0,fu1,fread,eva1
from bib__init__ import multibbh,multibbl,multibbm,multisma
import pandas as pd
(df0,df1)=(None,None)

stock_update('alert')

da=file_read('alert').sort_values(by=['stock']).reset_index(drop=True)
file_save('alert',da)
(db0,db1)=(da.copy(),da.copy());(db0['sig'],db1['sig'])=(None,None)
(db0,db1)=(db0[db0['par1'].isna()].drop(columns=['par1']).reset_index(drop=True),db1.dropna().reset_index(drop=True))
db0['par0'].apply(str);[db1[p1].apply(str) for p1 in ('par0','par1')]

for i in range(db0.shape[0]): df0=fread(df0,db0,i)
for i in range(db1.shape[0]): df1=fread(df1,db1,i)

[eva1(df0,db0,'par0',i) for i in range(db0.shape[0])]

[[eva1(df1,db1,p1,i) for p1 in ('par0','par1')] for i in range(db1.shape[0])]
 
for i in range(db0.shape[0]): db0['sig'][i]=fu0(df0,db0,i)
for i in range(db1.shape[0]): db1['sig'][i]=fu1(df1,db1,i)
 
file_save('sig',pd.concat([db1.dropna(),db0.dropna()]))