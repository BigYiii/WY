#画椭圆
#用turtle
import turtle

pen = turtle.Turtle()  
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.2
        pen.lt(3)  # 向左转3度
        pen.fd(a)  # 向前走a的步长
    else:
        a = a - 0.2
        pen.lt(3)
        pen.fd(a)
print(pen)
turtle.mainloop()

 #用matlotlib
import matplotlib.pyplot as plt
import numpy as np

t=[i/np.pi for i in np.arange(0,360)]
x=2*np.cos(t)
y=np.sin(t)
plt.plot(x,y)
plt.show()