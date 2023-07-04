from f__init__ import file_read

def fread(df=None,da=None,i=0):
    if i==0:df=file_read(da['stock'][i])
    else:
        if da['stock'][i]!=da['stock'][i-1]: df=file_read(da['stock'][i])
    return df