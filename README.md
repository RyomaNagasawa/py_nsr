# py_nsr
卒業研究で新規に作成したプログラム．（卒論テーマ：比抵抗分布データを用いた緩み斜面抽出方法の検討）

・hokan_clim99.py
山体の比抵抗値の分布データを補完し，塗りつぶし等高線を用いて断面図として出力する．

・dif_cross_sec_dlauto.py
雨期と乾期の比抵抗値の差分を塗りつぶし等高線を用いて断面図として表示する．2時期の観測点の座標誤差を自動で補正する．

・dif_plane.py
地表面からの深度が一定である面において，雨期と乾期の比抵抗値の差分を塗りつぶし等高線を用いて平面図として表示するプログラム．

・plot3d_wire.py
比抵抗値の3次元点郡データをカラーマップを用いて散布図として，また地形をワイヤーフレームで表示するプログラム．

・cul_vert_weak.py
比抵抗データから判断される深度方向の緩み域を評価し，評価値を地形等高線とともに平面上に表示するプログラム．

実行例
-------------------------------------------------------------------------
・hokan_clim99.py

![cross section of A line](https://github.com/RyomaNagasawa/py_nsr/assets/136213180/88874bc7-4ede-4ce2-b5f4-c58fe46dfe66)

・dif_cross_sec_dlauto.py

![Difference in cross section of A survey line](https://github.com/RyomaNagasawa/py_nsr/assets/136213180/de30acc3-2c9a-468f-9112-8676a72d5437)

・dif_plane.py

![Difference of plane data at 10m depth](https://github.com/RyomaNagasawa/py_nsr/assets/136213180/4264cefe-2532-4701-a78c-ad6af3d3356f)

・plot3d_wire.py

![survey line data with wireframe](https://github.com/RyomaNagasawa/py_nsr/assets/136213180/777b2f18-c964-4caf-bc29-565f573dce73)
![plane data plot with wireframe](https://github.com/RyomaNagasawa/py_nsr/assets/136213180/41feea12-2300-4e02-a915-62dbfa55257b)
![weak  zone estimated from resistivity](https://github.com/RyomaNagasawa/py_nsr/assets/136213180/7d914efe-72d0-4cbc-9e26-ca2997e8961e)

・cul_vert_weak.py

![evaluation](https://github.com/RyomaNagasawa/py_nsr/assets/136213180/04d461a7-a7bd-4c76-a533-91873c73071f)
