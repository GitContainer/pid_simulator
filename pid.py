#############
# 增量式PID #
#############

# 超参数
Kp = 0.2
T = 1
Ti = 1e9
Td = 0

A = Kp * (1 + T / Ti + Td / T)
B = Kp * (1 + 2 * Td / T)
C = Kp * (Td / T)
e0 = 0
e1 = 0
e2 = 0
set_val = 0


def PID_Init(goal):  # 初始化
    global set_val
    set_val = goal


def reInit():  # 重新初始化
    global e0, e1, e2, A, B, C, Kp, T, Ti, Td
    e0 = 0
    e1 = 0
    e2 = 0
    A = Kp * (1 + T / Ti + Td / T)
    B = Kp * (1 + 2 * Td / T)
    C = Kp * (Td / T)


def set_PID_parm(kp, ti, td, sp):
    global Kp, Ti, Td, set_val
    Kp = kp
    Ti = ti
    Td = td
    set_val = sp


def PID_Calc(now_val):  # 计算
    global set_val, e0, e1, e2, A, B, C
    e0 = set_val - now_val
    delta_u = A * e0 - B * e1 + C * e2
    e2 = e1
    e1 = e0
    return delta_u
