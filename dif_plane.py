import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import matplotlib.cm as cm
import pprint
from scipy.interpolate import griddata

L = input('Which depth would you like to see?\nSelect left side number from here.\n 0 :00m \n 1 :10m \n 2 :20m \n 3 :30m \n 4 :40m \n 5 :50m: \n 6 :60m \n 7 :70m \n 8 :80m: \nYour choce is :')

#CSVファイルを取り込む(乾期)
df1 = pd.read_csv('D:/nagasawa/kanagi_2periods_plane_data/kanagi_2periods_plane_data.csv')
#ファイル内の一行目の指定された名前のデータを選択
df1_2 = df1['X_TM4']
df1_3 = df1['Y_TM4']
df1_4 = df1['(R2-R1)_%s0m'%L]
df1_5 = df1['GL_%s0m'%L]
#x,y,zの値を入れていく
x1 = np.array(df1_2)
y1 = np.array(df1_3)
z1 = np.array(df1_4)
gl = np.array(df1_5)
'''
#加奈木最大最小
cb_min, cb_max = -2134, 2134
#加奈木最小，99%が収まる最大
#cb_min, cb_max = -1505, 1505
cb_div = 101
interval_of_cf = np.linspace(cb_min, cb_max, cb_div)
'''

plt.scatter(x1,y1,c=z1,marker="s",cmap = "bwr")
plt.colorbar(extend='both', label='resistivity[Ω*m]')
plt.clim(-1051.55,1051.55)
#plt.clim(-2006,2006)

#作図（見かけ比抵抗差分プロット）

'''
#マスキング1
df1_5 = df1['dLmax']
df1_6 = df1['Elev_max']
df1_7 = df1['dLmin']
df1_8 = df1['Elev_min']
a1 = np.array(df1_5)
b1 = np.array(df1_6)
c1 = np.array(df1_7)
d1 = np.array(df1_8)
#色をきめる
ax.fill(a1, b1,color="w")
ax.fill(c1, d1,color="w")
ax.set_aspect("equal")
'''

#wireframe作成{--------------------------------
Z = np.loadtxt('D:/nagasawa/kanagi/kanagi_ver1.txt')

#X,Y軸のグリッドを生成
#inputdata_linespace(xmin,xmax,---)(ymax,ymin,---)
X, Y = np.meshgrid(np.linspace(60876.95,62134.31,Z.shape[1]), np.linspace(52933.37,51566.2,Z.shape[0]))
#plt.figure(figsize=(26, 20), dpi=80, facecolor='w', edgecolor='k')


#等高線描画{-------------------------------------
#標高10m間隔で等高線を描く
elevation = range(0,1000,10)
elevation1 = range(0,1000,50)
cont = plt.contour(X, Y, Z, levels=elevation, cmap='binary', linewidths=0.5)
cont = plt.contour(X, Y, Z, levels=elevation1, cmap='binary', linewidths=0.8)
cont.clabel(fmt='%1.1f', fontsize=10)

#ラベルをつける
#cb = plt.colorbar(cont, shrink=0.5, aspect=10)
#-------------------------------------}等高線描画
plt.xlabel("X[m]")
plt.ylabel("Y[m]")
# 表示する
plt.show()
