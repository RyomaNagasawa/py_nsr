import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import matplotlib.cm as cm
import pprint
from scipy.interpolate import griddata

#雨期・乾期の比抵抗分布データを用いて上空から緩みを評価し，可視化するプログラム
#乾期高比抵抗かつ比抵抗低下部を抽出,表示，リストに書き出す

#CSVファイルを取り込む(差分)
df = pd.read_csv('d:/nagasawa/kanagi_2periods_plane_data/kanagi_2periods_plane_data.csv')

#ファイル内の一行目の指定された名前のデータを選択
dfx = df['X_TM4']
dfy = df['Y_TM4']
df00 = df['GL_10m']
df01 = df['R1_00m']
df02 = df['(R2-R1)_00m']
df03 = df['log10(R2/R1)_00m']
df10 = df['GL_10m']
df11 = df['R1_10m']
df12 = df['(R2-R1)_10m']
df13 = df['log10(R2/R1)_10m']
df20 = df['GL_20m']
df21 = df['R1_20m']
df22 = df['(R2-R1)_20m']
df23 = df['log10(R2/R1)_20m']
df30 = df['GL_30m']
df31 = df['R1_30m']
df32 = df['(R2-R1)_30m']
df33 = df['log10(R2/R1)_30m']
df40 = df['GL_40m']
df41 = df['R1_40m']
df42 = df['(R2-R1)_40m']
df43 = df['log10(R2/R1)_40m']
df50 = df['GL_50m']
df51 = df['R1_50m']
df52 = df['(R2-R1)_50m']
df53 = df['log10(R2/R1)_50m']
df60 = df['GL_60m']
df61 = df['R1_60m']
df62 = df['(R2-R1)_60m']
df63 = df['log10(R2/R1)_60m']
df70 = df['GL_70m']
df71 = df['R1_70m']
df72 = df['(R2-R1)_70m']
df73 = df['log10(R2/R1)_70m']
df80 = df['GL_80m']
df81 = df['R1_80m']
df82 = df['(R2-R1)_80m']
df83 = df['log10(R2/R1)_80m']



#Numpy配列へ変換
X= np.array(dfx)
Y= np.array(dfy)
GL_00m = np.array(df00)
R1_00m  = np.array(df01)
nz1_00m = np.array(df02)
nz2_00m = np.array(df03)
GL_00m = np.array(df10)
R1_10m = np.array(df11)
nz1_10m= np.array(df12)
nz2_10m= np.array(df13)
GL_00m = np.array(df20)
R1_20m = np.array(df21)
nz1_20m= np.array(df22)
nz2_20m= np.array(df23)
GL_00m = np.array(df30)
R1_30m = np.array(df31)
nz1_30m= np.array(df32)
nz2_30m= np.array(df33)
GL_00m = np.array(df40)
R1_40m = np.array(df41)
nz1_40m= np.array(df42)
nz2_40m= np.array(df43)
GL_00m = np.array(df50)
R1_50m = np.array(df51)
nz1_50m= np.array(df52)
nz2_50m= np.array(df53)
GL_00m = np.array(df60)
R1_60m = np.array(df61)
nz1_60m= np.array(df62)
nz2_60m= np.array(df63)
GL_00m = np.array(df70)
R1_70m = np.array(df71)
nz1_70m= np.array(df72)
nz2_70m= np.array(df73)
GL_00m = np.array(df80)
R1_80m = np.array(df81)
nz1_80m= np.array(df82)
nz2_80m= np.array(df83)


#乾期に高比抵抗（しきい値を設定）かつ比抵抗低下部分を抽出
#高比抵抗のしきい値，→比抵抗値25％と設定，条件１をパス→d1=1, or 0
third_quartile =695.6609
d1_00m = np.where(R1_00m>third_quartile,1,0)
d1_10m = np.where(R1_10m>third_quartile,1,0)
d1_20m = np.where(R1_20m>third_quartile,1,0)
d1_30m = np.where(R1_30m>third_quartile,1,0)
d1_40m = np.where(R1_40m>third_quartile,1,0)
d1_50m = np.where(R1_50m>third_quartile,1,0)
d1_60m = np.where(R1_60m>third_quartile,1,0)
d1_70m = np.where(R1_70m>third_quartile,1,0)
d1_80m = np.where(R1_80m>third_quartile,1,0)
'''
#低下量のしきい値，大きく低下→低下量上位25％と設定，条件１をパス→d1=1, or 0
#第1四分位数
#first_quartile=-116.899
#平均
first_quartile=-12.39149177
d2_00m = np.where(nz1_00m<first_quartile,1,0)
d2_10m = np.where(nz1_10m<first_quartile,1,0)
d2_20m = np.where(nz1_20m<first_quartile,1,0)
d2_30m = np.where(nz1_30m<first_quartile,1,0)
d2_40m = np.where(nz1_40m<first_quartile,1,0)
d2_50m = np.where(nz1_50m<first_quartile,1,0)
d2_60m = np.where(nz1_60m<first_quartile,1,0)
d2_70m = np.where(nz1_70m<first_quartile,1,0)
d2_80m = np.where(nz1_80m<first_quartile,1,0)
'''

#低下量のしきい値，大きく低下→低下量上位25％と設定，条件１をパス→d1=1, or 0
#第1四分位数
log10_1st_quartile=-0.12500849975
#平均
#log10_1st_quartile=0.0000310311636351109
d2_00m = np.where(nz2_00m<log10_1st_quartile,1,0)
d2_10m = np.where(nz2_10m<log10_1st_quartile,1,0)
d2_20m = np.where(nz2_20m<log10_1st_quartile,1,0)
d2_30m = np.where(nz2_30m<log10_1st_quartile,1,0)
d2_40m = np.where(nz2_40m<log10_1st_quartile,1,0)
d2_50m = np.where(nz2_50m<log10_1st_quartile,1,0)
d2_60m = np.where(nz2_60m<log10_1st_quartile,1,0)
d2_70m = np.where(nz2_70m<log10_1st_quartile,1,0)
d2_80m = np.where(nz2_80m<log10_1st_quartile,1,0)

#2条件をパス→d3=2
d3_00m = d1_00m+d2_00m
d3_10m = d1_10m+d2_10m
d3_20m = d1_20m+d2_20m
d3_30m = d1_30m+d2_30m
d3_40m = d1_40m+d2_40m
d3_50m = d1_50m+d2_50m
d3_60m = d1_60m+d2_60m
d3_70m = d1_70m+d2_70m
d3_80m = d1_80m+d2_80m

#判定
e_00m = np.where(d3_00m==2,1,0)
e_10m = np.where(d3_10m==2,1,0)
e_20m = np.where(d3_20m==2,1,0)
e_30m = np.where(d3_30m==2,1,0)
e_40m = np.where(d3_40m==2,1,0)
e_50m = np.where(d3_50m==2,1,0)
e_60m = np.where(d3_60m==2,1,0)
e_70m = np.where(d3_70m==2,1,0)
e_80m = np.where(d3_80m==2,1,0)

e_all = e_00m + e_10m + e_20m + e_30m + e_40m + e_50m + e_60m + e_70m + e_80m

#結果をファイルに出力
table = []
table.append(X)
table.append(Y)
table.append(e_all)
table_ver = np.array(table).T.tolist()
f = open('D:/nagasawa/深度方向差分評価/差分平均比抵抗_4.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(['X_TM4', 'Y_TM4','NumOfWeakPoints'])
writer.writerows(table_ver)
f.close()


plt.scatter(X,Y,c=e_all,marker="s",cmap = "Reds")
plt.colorbar()
#plt.clim(-966.7,966.7)
#plt.clim(-2134,2134)

#作図（見かけ比抵抗差分プロット）
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
