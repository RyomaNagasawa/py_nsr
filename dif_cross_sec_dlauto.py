import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import pprint
from scipy.interpolate import griddata

#dl補正を自動で行う



L = input('Which line would you like to culculate? \nA ~ I : ')

#CSVファイルを取り込む(乾期)
df1 = pd.read_csv('d:/nagasawa/first_sunny/%sv2_ver.csv'%L)
#ファイル内の一行目の指定された名前のデータを選択
df1_2 = df1['DL']
df1_3 = df1['Z']
df1_4 = df1['R']
df1_5 = df1['X']
df1_6 = df1['Y']
#x,y,zの値を入れていく
dl1 = np.array(df1_2)
z1 = np.array(df1_3)
n1 = np.array(df1_4)
x1 = np.array(df1_5)
y1 = np.array(df1_6)
#min,max,,,などを抽出
xmin1 = x1.min()
xmax1 = x1.max()
ymin1 = y1.min()
ymax1 = y1.max()
zmax1 = z1.max()
msize = 1


#以下繰り返し
#CSVファイルを取り込む(雨期)
df2 = pd.read_csv('d:/nagasawa/second_rain/%sv2r_ver.csv'%L)
#ファイル内の一行目の指定された名前のデータを選択
df2_2 = df2['DL']
df2_3 = df2['Z']
df2_4 = df2['R']
df2_5 = df2['X']
df2_6 = df2['Y']
#x,y,zの値を入れていく
dl2 = np.array(df2_2)
z2 = np.array(df2_3)
n2 = np.array(df2_4)
x2 = np.array(df2_5)
y2 = np.array(df2_6)#min,max,,,などを抽出
xmin2 = x2.min()
xmax2 = x2.max()
ymin2 = y2.min()
ymax2 = y2.max()
zmax2 = z2.max()
msize = 1
z1min = z1.min()
z2min = z2.min()

k1=np.sqrt((x1[0]-x2[0])**2+(y1[0]-y2[0])**2)
k2=np.sqrt((x2[0]-x1[0])**2+(y2[0]-y1[0])**2)
dl1 = np.where(x1[0]**2+y1[0]**2>x2[0]**2+y2[0]**2, dl1 - k1,dl1)
dl2 = np.where(x1[0]**2+y1[0]**2<x2[0]**2+y2[0]**2, dl2 - k2,dl2)

#min,max,,,などを抽出
dl1min = np.nanmin(dl1)
dl1max = np.nanmax(dl1)
z1min = np.nanmin(z1)
z1max = np.nanmax(z1)
n1max = np.nanmax(n1)
dl2min = np.nanmin(dl2)
dl2max = np.nanmax(dl2)
z2min = np.nanmin(z2)
z2max = np.nanmax(z2)
n2max = np.nanmax(n2)
msize = 1

adl1 = np.arange(dl1min,dl1max,msize)
az1 = np.arange(z1min,z1max,msize)
dldl1, zz1 = np.meshgrid(adl1, az1)
nz1 = griddata((dl1, z1), n1, (dldl1, zz1))
adl2 = np.arange(dl2min,dl2max,msize)
az2 = np.arange(z2min,z2max,msize)
dldl2, zz2 = np.meshgrid(adl2, az2)
nz2 = griddata((dl2, z2), n2, (dldl2, zz2))
#メッシュの整形（大を小に合わせて削る）
#最小および最大行数・列数を抽出
row1, col1 = nz1.shape
row2, col2 = nz2.shape
row_s = np.where(row1 <= row2, row1, row2)
col_s = np.where(col1 <= col2, col1, col2)
row_l = np.where(row1 >= row2, row1, row2)
col_l = np.where(col1 >= col2, col1, col2)
#削る行，列番号の数列を作成（meshdata）
row_to_del = list(range(np.where(row1 <= row2, row1, row2), np.where(row1 >= row2, row1, row2)))
col_to_del = list(range(np.where(col1 <= col2, col1, col2),  np.where(col1 >= col2, col1, col2)))


#meshdataの過剰分を削る（x,zが大きい所）
if row1>row_s:
    nz1_ver0 = np.delete(nz1, row_to_del, axis=0)
    nz2_ver0 = nz2
    ax0 = adl2
else:
    nz1_ver0 = nz1
    nz2_ver0 = np.delete(nz2, row_to_del, axis=0)
    ax0 = adl1

if col1>col_s:
    nz1_ver1 = np.delete(nz1_ver0, col_to_del, axis=1)
    nz2_ver1 = nz2_ver0
    ay0 = az2
else:
    nz1_ver1 = nz1_ver0
    nz2_ver1 = np.delete(nz2_ver0, col_to_del, axis=1)
    ay0 = az1

#様々な差分評価(B-A－1，ln(B-A)－2，ln(ln(A-B)－3，ln(B-A) or -ln(A-B)ー4，ln(B/A)ー5)
#1
#nz_dif = nz2_ver1 - nz1_ver1
#2
#nz_dif = np.log(nz2_ver1 - nz1_ver1)
#3
#nz_dif = np.log(nz1_ver1 - nz2_ver1)
#4
nz_dif = np.where(nz2_ver1 > nz1_ver1, np.log(nz2_ver1 - nz1_ver1),-np.log(nz1_ver1 - nz2_ver1))
#5
#nz_dif = np.log10(nz2_ver1 / nz1_ver1)
#6
#nz_dif = np.log(nz2_ver1 / nz1_ver1)/np.log(nz1_ver1)
#7
#nz_dif = np.log(nz1_ver1 / nz2_ver1)/np.log(nz2_ver1)

#補間したメッシュのデータをcsvで書き出す
#pd.DataFrame(nz_dif).to_csv('D:/nagasawa/dif_2d/p1/%s_dif.csv'%L)



#作図（見かけ比抵抗差分プロット）
fig, ax = plt.subplots()


#マスキング1
df1_7 = df1['dLmin']
df1_8 = df1['Elev_min']
df1_9 = df1['Elev_max']
df1_7_ver = np.where(x1[0]**2+y1[0]**2>x2[0]**2+y2[0]**2, df1_7 -k1, df1_7)

a1 = np.array(df1_7)
b1 = np.array(df1_8)
c1 = np.array(df1_7)
d1 = np.array(df1_9)
#色をきめる
ax.fill(a1, b1,color="w")
ax.fill(c1, d1,color="w")
ax.set_aspect("equal")


#マスキング2
df2_7 = df2['dLmax']
df2_8 = df2['Elev_max']
df2_9 = df2['Elev_min']
df2_7_ver = np.where(x1[0]**2+y1[0]**2<x2[0]**2+y2[0]**2, df2_7 -k2, df2_7)
a2 = np.array(df2_7)
b2 = np.array(df2_8)
c2 = np.array(df2_7)
d2 = np.array(df2_9)
#色をきめるD:

ax.fill(a2, b2,color="w")
ax.fill(c2, d2,color="w")
ax.set_aspect("equal")

#マスキング3乾期
if L=='c':
    MX3=np.array([245,245,278,278])
elif L=='e':
    MX3=np.array([227,227,298,298])
elif L=='f':
    MX3 = np.array([156,156,276,276])
elif L=='g':
    MX3 =np.array([142,142,305,305])


if (L=='c')or(L=='e')or(L=='f')or(L=='g'):
    MX3=np.where(x1[0]**2+y1[0]**2>x2[0]**2+y2[0]**2, MX3 -k1, MX3)
    MY3 = np.array([550,250,250,550])
    a3 = np.array(MX3)
    b3 = np.array(MY3)
    #色をきめる
    ax.fill(a3, b3,color="w")
    ax.set_aspect("equal")

#マスキング4雨期
if L=='c':
    MX4 =np.array([240.99,240.99,261,261])
elif L=='f':
    MX4 = np.array([151.5,151.5,232.3,232.3])
elif L=='g':
    MX4 = np.array([140.3,140.3,220.4,220.4])


if (L=='c')or(L=='f')or(L=='g'):
    MX4=np.where(x1[0]**2+y1[0]**2<x2[0]**2+y2[0]**2, MX4 -k2, MX4)
    MY4 = np.array([550,250,250,550])
    a4 = np.array(MX3)
    b4 = np.array(MY3)
    #色をきめる
    ax.fill(a4, b4,color="w")
    ax.set_aspect("equal")

#meshgrid作成
xf, yf = np.meshgrid(ax0,ay0)

#メッシュグリッドの過剰分を削る（発生しないとこもある）
xfr, xfc = xf.shape
yfr, yfc = yf.shape
nr, nc =nz_dif.shape
row_to_del2 = list(range(np.where(xfr >= nr, nr, xfr), np.where(xfr >= nr, xfr, nr)))
col_to_del2 = list(range(np.where(xfc >= nc, nc, xfc), np.where(xfc >= nc, xfc, nc)))

xf_ver0 = np.delete(xf,row_to_del2,axis=0)
yf_ver0 = np.delete(yf,row_to_del2,axis=0)
xf_ver1 = np.delete(xf_ver0,col_to_del2,axis=1)
yf_ver1 = np.delete(yf_ver0,col_to_del2,axis=1)

#加奈木最大最小
#cb_min, cb_max = -2134, 2134
#加奈木最小，99%が収まる最大
'''
#99%sabunn{-------------------
cb_min, cb_max = -966.7, 966.7
cb_div = 101
interval_of_cf =np.linspace(cb_min, cb_max, cb_div)
plt.contourf(xf_ver1,yf_ver1,nz_dif,interval_of_cf, cmap = "bwr")
plt.colorbar(aspect=40, pad=0.08, orientation='vertical', shrink=0.62, label='resistivity[Ω*m]')
#-------------}
'''

cb_div = 101
#測線毎の最大最小{------------------
cb_min, cb_max = np.nanmin(nz_dif), np.nanmax(nz_dif)
if (np.nanmin(nz_dif))**2>(np.nanmax(nz_dif))**2:
    cb_max = -cb_min
else:
    cb_min=-cb_max
interval_of_cf =np.linspace(cb_min, cb_max, cb_div)
plt.contourf(xf_ver1,yf_ver1,nz_dif,interval_of_cf, cmap = "bwr")
plt.colorbar(aspect=40, pad=0.08, orientation='vertical', shrink=0.62, label='log10(Δr’)[Ω*m]')
#---------------------}
#軸を消すときはこれを使う
#ax.axis("off")
#cont = plt.contourf(xx,yy,nz, interval_of_cf, cmap="rainbow", extend="both")
#軸を消すときはこれを使う
#ax.axis("off")
#plt.contourf(xf_ver1,yf_ver1,nz_dif,interval_of_cf, cmap = "bwr", extend="both")

plt.xlabel("dL[m]")
plt.ylabel("Elevation[m]")
plt.show()
