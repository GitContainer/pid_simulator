from pid import *
from math import atan, exp
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def input(inputs):  # 模拟系统
    global val
    val += (atan(inputs - 1.5) + 0.5) * exp(-abs(val / 100)) * 20
    return val


def Calc_Data():
    global val, input_val, sd4
    reInit()  # 重新初始化
    val = 100
    input_val = 0
    val_list = [val]
    u_list = []
    for i in range(100):
        delta_u = PID_Calc(val)  # 计算PID
        input_val += delta_u
        input(input_val)
        val_list.append(val)
        u_list.append(delta_u)
    return [val_list, u_list]


def update(val):
    set_PID_parm(sd1.val, sd2.val, sd3.val, sd4.val)
    [data1, data2] = Calc_Data()
    pic1.set_ydata(data1)
    pic2.set_ydata(data2 * 10)
    fig.canvas.draw_idle()


val = 0  # 输出值
input_val = 0  # 输入值

PID_Init(100)  # 设定目标
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)  #调整子图间距
plt.axis([0, 100, 0, 250])
[data1, data2] = Calc_Data()
pic1, = plt.plot(data1)
pic2, = plt.plot(data2 * 10)

axcolor = 'lightgoldenrodyellow'  # slider的颜色
ax1 = plt.axes([0.1, 0.20, 0.8, 0.03], facecolor=axcolor)
ax2 = plt.axes([0.1, 0.15, 0.8, 0.03], facecolor=axcolor)
ax3 = plt.axes([0.1, 0.10, 0.8, 0.03], facecolor=axcolor)
ax4 = plt.axes([0.1, 0.05, 0.8, 0.03], facecolor=axcolor)
sd1 = Slider(ax1, 'Kp', 0.01, 2, valinit=0.03)
sd2 = Slider(ax2, 'Ti', 0.01, 100, valinit=42)
sd3 = Slider(ax3, 'Td', 0.01, 100, valinit=0.01)
sd4 = Slider(ax4, 'set_val', 1, 200, valinit=100)
sd1.on_changed(update)
sd2.on_changed(update)
sd3.on_changed(update)
sd4.on_changed(update)

plt.show()
