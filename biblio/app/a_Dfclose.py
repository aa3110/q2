from f__init__ import file_read

def Dfclose(df='',sto2b=''): 
    def read_close(i=''):df[i]=file_read(i)['Close']
    [read_close(i) for i in sto2b]
    return df