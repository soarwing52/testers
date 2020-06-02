import tablib

ds = tablib.Dataset()
ds.headers = ['phone','email']
x = [[1,1],[2,2]]
for a in x:
    ds.append(a)
print(ds)
index = ds.headers.index('phone')
new = ['','xxx']
try:
    del ds['phone']
    raise EnvironmentError
except EnvironmentError:
    pass
#ds.insert_col(index=index, col=new,header='phone')
finally:
    print(ds)
