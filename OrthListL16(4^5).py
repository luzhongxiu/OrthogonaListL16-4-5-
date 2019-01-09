import math
import numpy as np
import pyecharts as pye
import matplotlib.pyplot as plt

def L16_Karray_calculate(l):
	#计算L16(4^5)
	k=np.arange(20).reshape(4,5)
	if len(l)==16:
		for i in range(0,4):
			for j in range(0,5):
				k[i][j]=0
		for i in range(0,4):
			k[0][0]=k[0][0]+l[i]
			k[1][0]=k[1][0]+l[i+4]
			k[2][0]=k[2][0]+l[i+8]
			k[3][0]=k[3][0]+l[i+12]
		k[0][1]=l[0]+l[4]+l[8]+l[12]
		k[0][2]=l[0]+l[5]+l[10]+l[15]
		k[0][3]=l[0]+l[6]+l[11]+l[13]
		k[0][4]=l[0]+l[7]+l[9]+l[14]
		k[1][1]=l[1]+l[5]+l[9]+l[13]
		k[1][2]=l[1]+l[4]+l[11]+l[14]
		k[1][3]=l[1]+l[7]+l[10]+l[12]
		k[1][4]=l[1]+l[6]+l[8]+l[15]
		k[2][1]=l[2]+l[6]+l[10]+l[14]
		k[2][2]=l[2]+l[7]+l[8]+l[13]
		k[2][3]=l[2]+l[4]+l[9]+l[15]
		k[2][4]=l[2]+l[5]+l[11]+l[12]
		k[3][1]=l[3]+l[7]+l[11]+l[15]
		k[3][2]=l[3]+l[6]+l[9]+l[12]
		k[3][3]=l[3]+l[5]+l[8]+l[14]
		k[3][4]=l[3]+l[4]+l[10]+l[13]
	return k
def R_list_calculate(k):
	#计算每种因素对应的极差R
	R=[0]*5
	R[0]=max(k[0][0],k[1][0],k[2][0],k[3][0])-min(k[0][0],k[1][0],k[2][0],k[3][0])
	R[1]=max(k[0][1],k[1][1],k[2][1],k[3][1])-min(k[0][1],k[1][1],k[2][1],k[3][1])
	R[2]=max(k[0][2],k[1][2],k[2][2],k[3][2])-min(k[0][2],k[1][2],k[2][2],k[3][2])
	R[3]=max(k[0][3],k[1][3],k[2][3],k[3][3])-min(k[0][3],k[1][3],k[2][3],k[3][3])
	R[4]=max(k[0][4],k[1][4],k[2][4],k[3][4])-min(k[0][4],k[1][4],k[2][4],k[3][4])
	return R
def line_render(r):
	#生成趋势图
	names = ['A1','A2','A3','A4']
	x=range(1,5)
	y1=[k[0][0],k[1][0],k[2][0],k[3][0]]
	y2=[k[0][1],k[1][1],k[2][1],k[3][1]]
	y3=[k[0][2],k[1][2],k[2][2],k[3][2]]
	y4=[k[0][3],k[1][3],k[2][3],k[3][3]]
	y5=[k[0][4],k[1][4],k[2][4],k[3][4]]

	plt.plot(x,y1)
	plt.plot(x,y2)
	plt.plot(x,y3)
	plt.plot(x,y4)
	plt.plot(x,y5)

	plt.show()
	return 0
l=[31,20,19,20,18,25,26,20,26,28,9,6,13,14,23,5]
k=L16_Karray_calculate(l)
r=R_list_calculate(k)
print(k)
print(k/4)
print(r)
line_render(r)


