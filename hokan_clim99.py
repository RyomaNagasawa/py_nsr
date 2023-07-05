import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import griddata

L = input('Which line would you like to see? \nA ~ I : ')

#CSVファイルを取り込む
df = pd.read_csv('d:/nagasawa/first_sunny/%sv2.csv'%L)
#df = pd.read_csv('d:/nagasawa/second_rain/%sv2r.csv'%L)
#ファイル内の一行目の指定された名前のデータを選択
df2 = df['DL']
df3 = df['Z']
df4 = df['R']
#x,y,zの値を入れていく
x = np.array(df2)
y = np.array(df3)
z = np.array(df4)
#min,max,,,などを抽出
xmin = x.min()
xmax = x.max()
ymin = y.min()
ymax = y.max()
zmax = z.max()
msize = 1

ax = np.arange(xmin,xmax,msize)
ay = np.arange(ymin,ymax,msize)
xx, yy = np.meshgrid(ax, ay)
nz = griddata((x, y), z, (xx, yy))

df5 = df['dLmax']
df6 = df['Elev_max']
df7 = df['dLmin']
df8 = df['Elev_min']

a = np.array(df5)
b = np.array(df6)
c = np.array(df7)
d = np.array(df8)

fig, ax = plt.subplots()
#色をきめる
ax.fill(a, b,color="w")
ax.fill(c, d,color="w")
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
    MY3 = np.array([550,250,250,550])
    a3 = np.array(MX3)
    b3 = np.array(MY3)
    #色をきめる
    ax.fill(a3, b3,color="w")
    ax.set_aspect("equal")

'''
#マスキング4雨期
if L=='c':
    MX4 =np.array([240.99,240.99,261,261])
elif L=='f':
    MX4 = np.array([151.5,151.5,232.3,232.3])
elif L=='g':
    MX4 = np.array([140.3,140.3,220.4,220.4])

if (L=='c')or(L=='f')or(L=='g'):
    MY4 = np.array([550,250,250,550])
    a4 = np.array(MX3)
    b4 = np.array(MY3)
    #色をきめる
    ax.fill(a4, b4,color="w")
    ax.set_aspect("equal")
'''
#contourfの範囲を設定．(rmin,rmax, 分割数)
#加奈木最大最小
#cb_min, cb_max = 41, 2798
#加奈木最小，99%が収まる最大
cb_min, cb_max = 41.80856, 1504.669
cb_div = 100
interval_of_cf =np.linspace(cb_min, cb_max, cb_div)
#軸を消すときはこれを使う
#ax.axis("off")
cont = plt.contourf(xx,yy,nz, interval_of_cf, cmap="rainbow", extend="both")

plt.colorbar(aspect=40, pad=0.08, orientation='vertical',shrink=0.62, label='resistivity[Ω*m]')
plt.xlabel("dL[m]")
plt.ylabel("Elevation[m]")
plt.show()
