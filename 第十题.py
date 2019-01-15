import time
t=time.localtime()
print(time.strftime("%H:%M:%S",t) )
time.sleep(1)
t=time.localtime()
print(time.strftime("%H:%M:%S",t) )