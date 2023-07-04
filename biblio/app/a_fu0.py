from s__init__ import high,low,cross,crossdown,crossup,gain,loss
from s__init__ import chan_in,chan_out,chan_it,chan_ot,chan_ib,chan_ob

def fu0(df=None,da=None,i=0): return eval(da['signal'][i])(df,da['basis'][i],da['par0'][i])