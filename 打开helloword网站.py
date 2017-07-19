
from urllib import request
file = request.urlopen('http://baidu.com')
message = file.read()
print (message)
