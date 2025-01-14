import numpy as np
import matplotlib.pyplot as plt
import time
M=2048


# 定义0 F2 F3 F4......FM
#    0 0  F3 F4......FM
#
#
#    0 0  0   0 ......0


vec_F=np.zeros(M)
for i in range(1, M):
    vec_F[i] = (i + 1) / i

#定义初始n向量（00000000.....1）
n0=np.zeros(M)
n0[M-1]=1
#定义1/k向量
vec_i=np.zeros(M)
for i in range(0, M):
    vec_i[i]=1/(i+1)
    i+=1
# print(vec_i)
#计算向量与向量之间的元素之间的乘积
def vec_vec(A,B):
    i=0
    C=np.zeros(M)
    while(i<M):
        C[i]=A[i]*B[i]
        i+=1
    return (C)
#计算矩阵和向量的某种特殊乘积
def matvec(A,B):
    C=np.zeros(M)
    i=M-1
    while(i>0):
        C[i-1]=C[i]+A[i]*B[i]
        i=i-1
    return (C)


def solve_fragmentation(vec_F,n,vec_i):
    MATVEC=matvec(vec_F,n)
    # print(MATVEC)
    n_k=-vec_vec(vec_F,n)+ vec_vec(MATVEC,vec_i)
    # print( vec_vec(MATVEC,vec_i))
    # print(-vec_vec(vec_F,n))
    return n_k

timestep=0.001

n_k=[n0]
time_points=[0]
n_M1=[1]
n_M2=[0]
n_M3=[0]
n_M4=[0]
n_M5=[0]
n_M6=[0]
n_1=[0]
n_2=[0]
n_3=[0]
def make_solution(time_step):
  n_k_now=n0
  time=0
  while time<1:
    n_k_now=n_k_now+solve_fragmentation(vec_F,n_k_now,vec_i)*time_step
    n_k.append(n_k_now)
    n_M1.append(n_k_now[M - 1])
    n_M2.append(n_k_now[M - 2])
    n_M3.append(n_k_now[M - 3])
    n_M4.append(n_k_now[M - 4])
    n_M5.append(n_k_now[M - 5])
    n_M6.append(n_k_now[M - 6])
    n_1.append(n_k_now[0])
    n_2.append(n_k_now[1])
    n_3.append(n_k_now[2])
    time+=time_step
    time_points.append(time)

time_start=time.time()
make_solution(timestep)
# print(n_k)
time_end=time.time()
total_time=time_end-time_start
print(total_time)


plt.plot(time_points, n_M1, label='c2048')
plt.xlabel('Time')
plt.ylabel('c')
plt.legend()
plt.show()
# plt.plot(time_points, n_M2, label='n_M-1')
# plt.plot(time_points, n_M3, label='n_M-2')
# plt.plot(time_points, n_M4, label='n_M-3')
# plt.plot(time_points, n_M5, label='n_M-4')
# plt.plot(time_points, n_M6, label='n_M-5')
plt.plot(time_points, n_1, label='c1')
plt.plot(time_points,n_2,label='c2')
plt.plot(time_points,n_3,label='c3')
plt.xlabel('Time')
plt.ylabel('c')
plt.legend()
plt.show()

plt.plot(time_points, n_M2, label='c2047')
plt.xlabel('Time')
plt.ylabel('c')
plt.legend()
plt.show()







