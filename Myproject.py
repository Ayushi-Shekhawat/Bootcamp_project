import hashlib

text = 'There!'
a = hashlib.md5()
print(a.hexdigest())
a.update(b"My project!")
print(a.hexdigest())
a.update(text.encode('UTF-8'))
print(a.hexdigest())
