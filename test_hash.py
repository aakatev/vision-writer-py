import hashlib
import time

hash = hashlib.sha1()
hash.update(str(time.time()).encode('utf-8'))
print (hash.hexdigest()+'.jpg')
# print (hash.hexdigest()[:10])