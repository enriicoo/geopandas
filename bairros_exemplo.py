import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

mapa = gpd.read_file('/Limite_Bairro.shp')
mapa = mapa.astype({"CODBAIRRO": 'int64'}).astype({"Cod_RP": 'float'}).astype({"Cod_RP": 'int64'})
mapa = mapa[['CODBAIRRO','CODRA','Cod_RP','geometry']]

ax = mapa.plot(figsize=(50, 50), edgecolor='darkblue', linewidth=0.5, alpha=0.5)
ax.show()
