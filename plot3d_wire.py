import requests
import string
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#比抵抗データを3次元空間にプロットし，地形図とともに表示するプログラム．
#比抵抗データは地表面からの深度ごとで補完したものを散布図で表示する．
#地形図はDEMデータを取得し，地形等高線とワイヤーフレームにより描画する．
#wireframe作成{--------------------------------
Z = np.loadtxt('D:/nagasawa/kanagi/kanagi_ver1.txt')
#ZZ=string.replace(Z.text, u'e',u'-0.0')
#X,Y軸のグリッドを生成
#inputdata_linespace(xmin,xmax,---)(ymax,ymin,---)
X, Y = np.meshgrid(np.linspace(60876.95,62134.31,Z.shape[1]), np.linspace(52933.37,51566.2,Z.shape[0]))
fig = plt.figure(figsize=(26, 20), dpi=80, facecolor='w', edgecolor='k')
# プロット中の軸の取得。gca はGet Current Axes の略。
ax = fig.gca(projection='3d')
#wireframeを描く
ax.plot_wireframe(X, Y, Z, rstride=1, cstride=2, linewidth=0.2,color='black')
#--------------------------------}wireframe作成

#等高線描画{-------------------------------------
#標高10m間隔で等高線を描く
elevation = range(0,1000,10)
cont = plt.contour(X, Y, Z, levels=elevation, cmap='binary', linewidths=0.1)
#-------------------------------------}等高線描画

#全ての平面データplot{---------------------
#CSVファイルを取り込む
df = pd.read_csv('d:/nagasawa/plot_3d/csv_3d/uav1_coord/uav1_all.csv')
#ファイル内の一行目の指定された名前のデータを選択
df2 = df['X_TM4']
df3 = df['Y_TM4']
df4 = df['GL']
df5 = df['R']
#x,y,zの値を入れていく
x = np.array(df2)
y = np.array(df3)
z = np.array(df4)
r = np.array(df5)

#比抵抗のしきい値を設定する場合はここ．{------------------
r_reg = np.where(r > 1200, r, np.nan)
#------------------}比抵抗のしきい値を設定する場合はここ．

# カラーマップを生成
cm = plt.cm.get_cmap('rainbow')
#cm = plt.cm.get_cmap('gist_heat')
# axに散布図を描画、戻り値にPathCollectionを得る
#c=r;全ての点．c=r_reg;しきい値以上の比抵抗を持つ点．をそれぞれplot
mappable = ax.scatter(x, y, z, c=r, cmap=cm,s=30)
#mappable = ax.scatter(x, y, z, c=r_reg, cmap=cm,s=30)

fig.colorbar(mappable, ax=ax)
#----------------------}全ての平面データplot

'''
#任意の深度の平面データplot{---------------------
#CSVファイルを取り込む
d0 = pd.read_csv('d:/nagasawa/plot_3d/csv_3d/uav1_coord/uav1_0000m.csv')
d1 = pd.read_csv('d:/nagasawa/plot_3d/csv_3d/uav1_coord/uav1_0010m.csv')
d2 = pd.read_csv('d:/nagasawa/plot_3d/csv_3d/uav1_coord/uav1_0020m.csv')
d3 = pd.read_csv('d:/nagasawa/plot_3d/csv_3d/uav1_coord/uav1_0030m.csv')
d4 = pd.read_csv('d:/nagasawa/plot_3d/csv_3d/uav1_coord/uav1_0040m.csv')
d5 = pd.read_csv('d:/nagasawa/plot_3d/csv_3d/uav1_coord/uav1_0050m.csv')
d6 = pd.read_csv('d:/nagasawa/plot_3d/csv_3d/uav1_coord/uav1_0060m.csv')
d7 = pd.read_csv('d:/nagasawa/plot_3d/csv_3d/uav1_coord/uav1_0070m.csv')
d8 = pd.read_csv('d:/nagasawa/plot_3d/csv_3d/uav1_coord/uav1_0080m.csv')
#ファイル内の一行目の指定された名前のデータを選択
d0_2 = d0['X_TM4']
d0_3 = d0['Y_TM4']
d0_4 = d0['GL']
d0_5 = d0['R']
d1_2 = d1['X_TM4']
d1_3 = d1['Y_TM4']
d1_4 = d1['GL']
d1_5 = d1['R']
d2_2 = d2['X_TM4']
d2_3 = d2['Y_TM4']
d2_4 = d2['GL']
d2_5 = d2['R']
d3_2 = d3['X_TM4']
d3_3 = d3['Y_TM4']
d3_4 = d3['GL']
d3_5 = d3['R']
d4_2 = d4['X_TM4']
d4_3 = d4['Y_TM4']
d4_4 = d4['GL']
d4_5 = d4['R']
d5_2 = d5['X_TM4']
d5_3 = d5['Y_TM4']
d5_4 = d5['GL']
d5_5 = d5['R']
d6_2 = d6['X_TM4']
d6_3 = d6['Y_TM4']
d6_4 = d6['GL']
d6_5 = d6['R']
d7_2 = d7['X_TM4']
d7_3 = d7['Y_TM4']
d7_4 = d7['GL']
d7_5 = d7['R']
d8_2 = d8['X_TM4']
d8_3 = d8['Y_TM4']
d8_4 = d8['GL']
d8_5 = d8['R']
#x,y,zの値を入れていく
x0 = np.array(d0_2)
y0 = np.array(d0_3)
z0 = np.array(d0_4)
r0 = np.array(d0_5)
x1 = np.array(d1_2)
y1 = np.array(d1_3)
z1 = np.array(d1_4)
r1 = np.array(d1_5)
x2 = np.array(d2_2)
y2 = np.array(d2_3)
z2 = np.array(d2_4)
r2 = np.array(d2_5)
x3 = np.array(d3_2)
y3 = np.array(d3_3)
z3 = np.array(d3_4)
r3 = np.array(d3_5)
x4 = np.array(d4_2)
y4 = np.array(d4_3)
z4 = np.array(d4_4)
r4 = np.array(d4_5)
x5 = np.array(d5_2)
y5 = np.array(d5_3)
z5 = np.array(d5_4)
r5 = np.array(d5_5)
x6 = np.array(d6_2)
y6 = np.array(d6_3)
z6 = np.array(d6_4)
r6 = np.array(d6_5)
x7 = np.array(d7_2)
y7 = np.array(d7_3)
z7 = np.array(d7_4)
r7 = np.array(d7_5)
x8 = np.array(d8_2)
y8 = np.array(d8_3)
z8 = np.array(d8_4)
r8 = np.array(d8_5)
# カラーマップを生成
cm = plt.cm.get_cmap('rainbow')
#下記，X,Y,Z，Rに任意の深度の十の位の値
mappable1 = ax.scatter(x1, y1, z1, c=r1, cmap=cm, s=25)
#mappable2 = ax.scatter(x3, y3, z3, c=r3, cmap=cm, s=25)
#mappable3 = ax.scatter(x5, y5, z5, c=r5, cmap=cm, s=25)
#mappable4 = ax.scatter(x7, y7, z7, c=r7, cmap=cm, s=25)
fig.colorbar(mappable1, ax=ax)
#fig.colorbar(mappable2, ax=ax)
#fig.colorbar(mappable3, ax=ax)
#fig.colorbar(mappable4, ax=ax)
#----------------------}任意の深度の平面データplot
'''
'''
#測線ごとの断面データplot{---------------------
#測線データplot
#df_l = pd.read_csv('D:/nagasawa/first_sunny/depth_3d/all_1s.csv')
df_l = pd.read_csv('D:/nagasawa/second_rain/depth_3d/all_2r.csv')

#ファイル内の一行目の指定された名前のデータを選択
df2_l = df_l['X_TM4']
df3_l = df_l['Y_TM4']
df4_l = df_l['GL']
df5_l = df_l['R']
#x,y,zの値を入れていく
x_l = np.array(df2_l)
y_l = np.array(df3_l)
z_l = np.array(df4_l)
r_l = np.array(df5_l)
# カラーマップを生成
cm = plt.cm.get_cmap('rainbow')
# axに散布図を描画、戻り値にPathCollectionを得る
mappable = ax.scatter(x_l, y_l, z_l,marker='s', c=r_l, cmap=cm,s=20)
fig.colorbar(mappable, ax=ax, shrink=0.5, aspect=10, label='resistivity[Ω*m]')
#----------------------}測線ごとの断面データplot
'''
'''
#任意の深度の平面データplot{---------------------
#CSVファイルを取り込む
d0 = pd.read_csv('d:/nagasawa/dif_3d/with_dem/ad_ver.csv')
d1 = pd.read_csv('d:/nagasawa/dif_3d/with_dem/ei_ver.csv')
#ファイル内の一行目の指定された名前のデータを選択
d0_2 = d0['X_TM4']
d0_3 = d0['Y_TM4']
d0_4 = d0['GL']
d0_5 = d0['r_ver']
d1_2 = d1['X_TM4']
d1_3 = d1['Y_TM4']
d1_4 = d1['GL']
d1_5 = d1['r_ver']
#x,y,zの値を入れていく
x0 = np.array(d0_2)
y0 = np.array(d0_3)
z0 = np.array(d0_4)
r0 = np.array(d0_5)
x1 = np.array(d1_2)
y1 = np.array(d1_3)
z1 = np.array(d1_4)
r1 = np.array(d1_5)
xf=np.concatenate([x0,x1],0)
yf=np.concatenate([y0,y1],0)
zf=np.concatenate([z0,z1],0)
rf=np.concatenate([r0,r1],0)
'''
'''
# カラーマップを生成
cm = plt.cm.get_cmap('rainbow')
#下記，X,Y,Z，Rに任意の深度の十の位の値
mappable1 = ax.scatter(xf, yf, zf, c=rf, cmap=cm, s=5)
#mappable2 = ax.scatter(x0, y0, z0, c=r0, cmap=cm, s=5)
#mappable3 = ax.scatter(x5, y5, z5, c=r5, cmap=cm, s=25)
#mappable4 = ax.scatter(x7, y7, z7, c=r7, cmap=cm, s=25)
fig.colorbar(mappable1, ax=ax)
#fig.colorbar(mappable2, ax=ax)
#fig.colorbar(mappable3, ax=ax)
#fig.colorbar(mappable4, ax=ax)
#----------------------}任意の深度の平面データplot
'''

plt.xlabel("X[m]")
plt.ylabel("Y[m]")
ax.set_zlabel('Elevation[m]')
# 表示する
plt.show()
