from urllib import request as rq
url=''
r=rq.urlopen(url)
data = r.read()
f=open(url, 'wb')    #write binary data
f.write(data)
f.close() #important
print('done')
#added on remote master
